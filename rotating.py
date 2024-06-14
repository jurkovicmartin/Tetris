import pygame

def rotate_shape(matrix, shape, state) -> int:
    """
    Returns new rotation state.

    Shapes:
    0 = I
    1 = square
    2 = J
    3 = L
    4 = 4
    5 = Z
    6 = T
    """
    # Find rotating point
    rotating_point = None
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == 2:
                rotating_point = [y, x]
                break
        if rotating_point is not None:
            break

    
    if shape == 0:
        return rotate_I(matrix, state, rotating_point)
    else:
        raise Exception("Unexpected error")
        

def rotate_I(matrix, state, point) -> int:
    """
    Returns new rotation state.
    """
    max_row = len(matrix) - 1
    max_cell = len(matrix[0]) - 1
    if state == 0:
        # Check for field border
        if point[0] + 3 > max_row:
            return state
        # Check for another block collision
        for i in range(1, 4):
            if matrix[point[0] + i][point[1]] == 1:
                return state
        
        # Removing original shape
        for i in range(1, 4):
            matrix[point[0]][point[1] + i] = 0
        # Putting rotated shape
        for i in range(1, 4):
            matrix[point[0] + i][point[1]] = 2
        return 1
        
    elif state == 1:
        # Check for field border
        if point[1] + 3 > max_cell:
            return state
        # Check for another block collision
        for i in range(1, 4):
            if matrix[point[0]][point[1] + i] == 1:
                return state
            
        # Removing original shape
        for i in range(1, 4):
            matrix[point[0] + i][point[1]] = 0
        # Putting rotated shape
        for i in range(1, 4):
            matrix[point[0]][point[1] + i] = 2
        return 0            
    else: raise Exception("Unexpected error")