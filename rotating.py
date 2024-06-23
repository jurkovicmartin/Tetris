import pygame

def rotate_shape(matrix, shape: str, state: int) -> int:
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

    Parameters
    ----
    matrix: game field matrix
    """
    # Find first block of the shape
    first_point = None
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == 2:
                first_point = [y, x]
                break
        if first_point is not None:
            break

    
    if shape == 0:
        return rotate_I(matrix, state, first_point)
    elif shape == 1:
        pass
    elif shape == 2:
        return rotate_J(matrix, state, first_point)
    elif shape == 3:
        return rotate_L(matrix, state, first_point)
    elif shape == 4:
        return rotate_4(matrix, state, first_point)
    elif shape == 5:
        return rotate_Z(matrix, state, first_point)
    elif shape == 6:
        return rotate_T(matrix, state, first_point)
    else:
        raise Exception("Unexpected error")
        

def rotate_I(matrix, state: int, point) -> int:
    """
    Returns new rotation state.

    Parameters
    ----
    matrix: game field matrix
    """
    max_row = len(matrix) - 1
    max_cell = len(matrix[0]) - 1
    if state == 0:
        # Rotate point
        y, x = point[0], point[1] + 1
        # Check for field border
        if y + 2 > max_row:
            return state
        # Check for another block collision
        if matrix[y - 1][x] == 1 or matrix[y + 1][x] == 1 or matrix[y + 2][x] == 1:
            return state
        
        # Removing original shape
        matrix[y][x - 1] = 0
        matrix[y][x + 1] = 0
        matrix[y][x + 2] = 0
        # Putting rotated shape
        matrix[y - 1][x] = 2
        matrix[y + 1][x] = 2
        matrix[y + 2][x] = 2

        return 1
        
    elif state == 1:
        # Rotate point
        y, x = point[0] + 1, point[1]
        # Check for field border
        if x - 1 < 0:
            return state
        elif x + 2 > max_cell:
            return state
        # Check for another block collision
        if matrix[y][x - 1] == 1 or matrix[y][x + 1] == 1 or matrix[y][x + 2] == 1:
            return state
            
        # Removing original shape
        matrix[y - 1][x] = 0
        matrix[y + 1][x] = 0
        matrix[y + 2][x] = 0
        # Putting rotated shape
        matrix[y][x - 1] = 2
        matrix[y][x + 1] = 2
        matrix[y][x + 2] = 2

        return 0            
    else: raise Exception("Unexpected error")


def rotate_Z(matrix, state: int , point) -> int:
    """
    Returns new rotation state.

    Parameters
    ----
    matrix: game field matrix
    """
    max_row = len(matrix) - 1
    max_cell = len(matrix[0]) - 1
    if state == 0:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if x + 1 > max_cell:
            return state
        # Check for another block collision
        if matrix[y][x - 1] == 1 or matrix[y + 1][x + 1] == 1:
            return state
        
        # Removing original shape
        matrix[y + 1][x - 1] = 0
        matrix[y + 2][x - 1] = 0
        # Putting rotated shape
        matrix[y][x - 1] = 2
        matrix[y + 1][x + 1] = 2

        return 1
    
    elif state == 1:
        # Rotate point
        y, x = point[0], point[1] + 1
        # Check for field border
        if point[0] + 2 > max_row:
            return state
        elif point[1] - 1 < 0:
            return state
        # Check for another block collision
        if matrix[y + 1][x - 1] == 1 or matrix[y + 2][x - 1] == 1:
            return state
            
        # Removing original shape
        matrix[y][x - 1] = 0
        matrix[y + 1][x + 1] = 0
        # Putting rotated shape
        matrix[y + 1][x - 1] = 2
        matrix[y + 2][x - 1] = 2

        return 0    
    else: raise Exception("Unexpected error")


def rotate_4(matrix, state: int, point) -> int:
    """
    Returns new rotation state.

    Parameters
    ----
    matrix: game field matrix
    """
    max_row = len(matrix) - 1
    max_cell = len(matrix[0]) - 1
    if state == 0:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if x - 1 < 0:
            return state
        # Check for another block collision
        if matrix[y][x + 1] == 1 or matrix[y + 1][x - 1] == 1:
            return state
        
        # Removing original shape
        matrix[y + 1][x + 1] = 0
        matrix[y + 2][x + 1] = 0
        # Putting rotated shape
        matrix[y][x + 1] = 2
        matrix[y + 1][x - 1] = 2

        return 1
    
    elif state == 1:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if y + 2 > max_row:
            return state
        # Check for another block collision
        if matrix[y + 1][x + 1] == 1 or matrix[y + 2][x + 1] == 1:
            return state
            
        # Removing original shape
        matrix[y][x + 1] = 0
        matrix[y + 1][x - 1] = 0
        # Putting rotated shape
        matrix[y + 1][x + 1] = 2
        matrix[y + 2][x + 1] = 2

        return 0    
    else: raise Exception("Unexpected error")


def rotate_T(matrix, state: int, point) -> int:
    """
    Returns new rotation state.

    Parameters
    ----
    matrix: game field matrix
    """
    max_row = len(matrix) - 1
    max_cell = len(matrix[0]) - 1
    if state == 0:
        # Rotate point
        y, x = point[0] + 1, point[1]
        # Check for field border
        if x - 1 < 0:
            return state
        # Check for another block collision
        if  matrix[y][x - 1] == 1:
            return state
        
        # Removing original shape
        matrix[y - 1][x] = 0
        # Putting rotated shape
        matrix[y][x - 1] = 2

        return 1
    
    elif state == 1:
        # Rotate point
        y, x = point[0], point[1] + 1
        # Check for another block collision
        if matrix[y - 1][x] == 1:
            return state
            
        # Removing original shape
        matrix[y][x + 1] = 0
        # Putting rotated shape
        matrix[y - 1][x] = 2

        return 2
    
    elif state == 2:
        # Rotate point
        y, x = point[0] + 1, point[1]
        # Check for field border
        if x + 1 > max_cell:
            return state
        # Check for another block collision
        if matrix[y][x + 1] == 1:
            return state
            
        # Removing original shape
        matrix[y + 1][x] = 0
        # Putting rotated shape
        matrix[y][x + 1] = 2

        return 3
    
    elif state == 3:
        # Rotate point
        y, x = point[0] + 1, point[1]
        # Check for field border
        if y + 1 > max_row:
            return state
        # Check for another block collision
        if matrix[point[0]][point[1] + 1] == 1 or matrix[point[0] - 1][point[1]] == 1:
            return state
            
        # Removing original shape
        matrix[y][x - 1] = 0
        # Putting rotated shape
        matrix[y + 1][x] = 2

        return 0
    
    else: raise Exception("Unexpected error")


def rotate_J(matrix, state: int, point) -> int:
    """
    Returns new rotation state.

    Parameters
    ----
    matrix: game field matrix
    """
    max_row = len(matrix) - 1
    max_cell = len(matrix[0]) - 1
    if state == 0:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if x + 2 > max_cell:
            return state
        # Check for another block collision
        if matrix[y + 1][x + 1] == 1 or matrix[y + 1][x + 2] == 1:
            return state
        
        # Removing original shape
        matrix[y + 2][x] = 0
        matrix[y + 2][x - 1] = 0
        # Putting rotated shape
        matrix[y + 1][x + 1] = 2
        matrix[y + 1][x + 2] = 2

        return 1
    
    elif state == 1:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if y + 2 > max_row:
            return state
        # Check for another block collision
        if matrix[y][x + 1] == 1 or matrix[y + 2][x] == 1:
            return state
            
        # Removing original shape
        matrix[y + 1][x + 1] = 0
        matrix[y + 1][x + 2] = 0
        # Putting rotated shape
        matrix[y][x + 1] = 2
        matrix[y + 2][x] = 2

        return 2
    
    elif state == 2:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if x + 2 > max_cell:
            return state
        # Check for another block collision
        if matrix[y][x + 2] or matrix[y + 1][x + 2] == 1:
            return state
            
        # Removing original shape
        matrix[y + 1][x] = 0
        matrix[y + 2][x] = 0
        # Putting rotated shape
        matrix[y][x + 2] = 2
        matrix[y + 1][x + 2] = 2

        return 3
    
    elif state == 3:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if y + 2 > max_row:
            return state
        elif x - 1 < 0:
            return state
        # Check for another block collision
        if matrix[y + 1][x] == 1 or matrix[y + 2][x] == 1 or matrix[y + 2][x - 1] == 1:
            return state
            
        # Removing original shape
        matrix[y][x + 1] = 0
        matrix[y][x + 2] = 0
        matrix[y + 1][x + 2] = 0
        # Putting rotated shape
        matrix[y + 1][x] = 2
        matrix[y + 2][x] = 2
        matrix[y + 2][x - 1] = 2

        return 0
    
    else: raise Exception("Unexpected error")


def rotate_L(matrix, state: int, point) -> int:
    """
    Returns new rotation state.

    Parameters
    ----
    matrix: game field matrix
    """
    max_row = len(matrix) - 1
    max_cell = len(matrix[0]) - 1
    if state == 0:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if x + 2 > max_cell:
            return state
        # Check for another block collision
        if matrix[y][x + 1] == 1 or matrix[y][x + 2] == 1:
            return state
        
        # Removing original shape
        matrix[y + 2][x] = 0
        matrix[y + 2][x + 1] = 0
        # Putting rotated shape
        matrix[y][x + 1] = 2
        matrix[y][x + 2] = 2

        return 1
    
    elif state == 1:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if y + 2 > max_row:
            return state
        # Check for another block collision
        if matrix[y + 1][x + 1] == 1 or matrix[y + 2][x + 1] == 1:
            return state
            
        # Removing original shape
        matrix[y + 1][x] = 0
        matrix[y][x + 2] = 0
        # Putting rotated shape
        matrix[y + 1][x + 1] = 2
        matrix[y + 2][x + 1] = 2

        return 2
    
    elif state == 2:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if x - 2 < 0:
            return state
        # Check for another block collision
        if matrix[y + 1][x] or matrix[y + 1][x - 1] == 1 or matrix[y + 1][x - 2] == 1:
            return state
            
        # Removing original shape
        matrix[y][x + 1] = 0
        matrix[y + 1][x + 1] = 0
        matrix[y + 2][x + 1] = 0
        # Putting rotated shape
        matrix[y + 1][x] = 2
        matrix[y + 1][x - 1] = 2
        matrix[y + 1][x - 2] = 2

        return 3
    
    elif state == 3:
        # Rotate point
        y, x = point[0], point[1]
        # Check for field border
        if y + 2 > max_row:
            return state
        elif x + 1 > max_cell:
            return state
        # Check for another block collision
        if matrix[y + 2][x] == 1 or matrix[y + 2][x + 1] == 1:
            return state
            
        # Removing original shape
        matrix[y + 1][x - 1] = 0
        matrix[y + 1][x - 2] = 0
        # Putting rotated shape
        matrix[y + 2][x] = 2
        matrix[y + 2][x + 1] = 2

        return 0
    
    else: raise Exception("Unexpected error")