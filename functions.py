import pygame

def draw_frame(surface, rect, color, border_color, border_width: int):
    # Frame background
    pygame.draw.rect(surface, color, rect)
    # Frame border
    pygame.draw.rect(surface, border_color, rect, border_width)


def draw_grid(surface, width: int, heigth: int, size: int, position, board):
    x_postion, y_postion = position
    for y in range(heigth):
        for x in range(width):
            pygame.draw.rect(surface, (0, 0, 0), (x * size + x_postion, y * size + x_postion, size, size), 0)
            pygame.draw.rect(surface, (40, 40, 40), (x * size + x_postion, y * size + y_postion, size, size), 1)


def new_shape(matrix, shape):
    """
    Shapes:
    0 = I
    1 = square
    2 = J
    3 = L
    4 = 4
    5 = Z
    6 = T
    """
    if shape == 0:
        matrix[0][3] = 2
        matrix[0][4] = 2
        matrix[0][5] = 2
        matrix[0][6] = 2
    elif shape == 1:
        matrix[0][4] = 2
        matrix[0][5] = 2
        matrix[1][4] = 2
        matrix[1][5] = 2
    elif shape == 2:
        matrix[0][5] = 2
        matrix[1][5] = 2
        matrix[2][5] = 2
        matrix[2][4] = 2
    elif shape == 3:
        matrix[0][4] = 2
        matrix[1][4] = 2
        matrix[2][4] = 2
        matrix[2][5] = 2
    elif shape == 4:
        matrix[0][4] = 2
        matrix[1][4] = 2
        matrix[1][5] = 2
        matrix[2][5] = 2
    elif shape == 5:
        matrix[0][5] = 2
        matrix[1][5] = 2
        matrix[1][4] = 2
        matrix[2][4] = 2
    elif shape == 6:
        matrix[0][4] = 2
        matrix[1][4] = 2
        matrix[2][4] = 2
        matrix[1][5] = 2
    else:
        raise Exception("Unexpected error")

def draw_shape(surface, matrix, gridsize: int):
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == 1 or cell == 2:
                pygame.draw.rect(surface, (255, 0, 0), (x * gridsize + 55, y * gridsize + 55, gridsize, gridsize), 0)
                pygame.draw.rect(surface, (0, 0, 0), (x * gridsize + 55, y * gridsize + 55, gridsize, gridsize), 1)

def move_shape(matrix, direction)-> bool|None:
    """
    Returns True if new shape has to be created.
    """

    # Find current shape
    cells = []

    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell == 2:
                cells.append([y, x])
                row[x] = 0

    if direction == "left":
        # Move current shape
        for i, cell in enumerate(cells):
            valid_move = validate_move(matrix, cells)
            # Left border
            if valid_move == "left":
                matrix[cells[i][0]][cells[i][1]] = 2
            else:
                matrix[cells[i][0]][cells[i][1] - 1] = 2

    elif direction == "right":
        # Move current shape
        for i, cell in enumerate(cells):
            valid_move = validate_move(matrix, cells)
            # Right border
            if valid_move == "right":
                matrix[cells[i][0]][cells[i][1]] = 2
            else:
                matrix[cells[i][0]][cells[i][1] + 1] = 2

    elif direction == "down":
        # Move current shape
        new = False
        for i, cell in enumerate(cells):
            valid_move = validate_move(matrix, cells)
            # Bottom
            if valid_move == "bottom":
                matrix[cells[i][0]][cells[i][1]] = 1
                new = True
            else:
                matrix[cells[i][0] + 1][cells[i][1]] = 2
        return new

    else:
        raise Exception("Unexpected error")
    

def validate_move(matrix, cells):
    max_row = len(matrix) - 1
    max_cell = len(matrix[0]) - 1

    for cell in cells:
        # Bottom
        if cell[0] == max_row:
            return "bottom"
        # Another block collision
        elif matrix[cell[0] + 1][cell[1]] == 1:
            return "bottom"
        else:
            pass

    for cell in cells:
        # Left border
        if cell[1] == 0:
            return "left"
        # Another block collision
        elif matrix[cell[0]][cell[1] - 1] == 1:
            return "left"
        # Right border
        elif cell[1] == max_cell:
            return "right"
        # Another block collision
        elif matrix[cell[0]][cell[1] + 1] == 1:
            return "right"
        else:
            pass


def check_lines(count: int, matrix) -> int:
    for y, row in enumerate(matrix):
        # Detect full layer
        if all(i == 1 for i in row):
            # Remove the full layer
            matrix[y] = [0 for _ in row]
            # Move others block one layer lower
            for i in range(y, -1, -1):
                for j, value in enumerate(matrix[i]):
                    if value == 1:
                        matrix[i][j] = 0
                        matrix[i+1][j] = 1

            return count + 1
    # No adding lines
    return count
        

def draw_next_shape(surface, shape, gridsize):
    """
    Shapes:
    0 = I
    1 = square
    2 = J
    3 = L
    4 = 4
    5 = Z
    6 = T
    """
    if shape == 0:
        for i in range(1, 5):
            pygame.draw.rect(surface, (255, 0, 0), (400 + i * gridsize, 69 + 2 * gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + i * gridsize , 69 + 2 * gridsize, gridsize, gridsize), 1)

    elif shape == 1:
        for i in range(2, 4):
            for j in range(2, 4):
                pygame.draw.rect(surface, (255, 0, 0), (400 + i * gridsize, 55 + j *gridsize, gridsize, gridsize), 0)
                pygame.draw.rect(surface, (0, 0, 0), (400 + i * gridsize , 55 + j * gridsize, gridsize, gridsize), 1)

    elif shape == 2:
        for i in range(1, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 69 + i * gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 69 + i * gridsize, gridsize, gridsize), 1)
        pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 69 + 3 * gridsize, gridsize, gridsize), 0)
        pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 69 + 3 * gridsize, gridsize, gridsize), 1)

    elif shape == 3:
        for i in range(1, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 69 + i * gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 69 + i * gridsize, gridsize, gridsize), 1)
        pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 69 + 3 * gridsize, gridsize, gridsize), 0)
        pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 69 + 3 * gridsize, gridsize, gridsize), 1)

    elif shape == 4:
        for i in range(1, 3):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 69 + i *gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 69 + i * gridsize, gridsize, gridsize), 1)
        for i in range(2, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 69 + i *gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 69 + i * gridsize, gridsize, gridsize), 1)

    elif shape == 5:
        for i in range(1, 3):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 69 + i *gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 69 + i * gridsize, gridsize, gridsize), 1)
        for i in range(2, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 69 + i *gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 69 + i * gridsize, gridsize, gridsize), 1)

    elif shape == 6:
        for i in range(1, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 69 + i * gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 69 + i * gridsize, gridsize, gridsize), 1) 
        pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 69 + 2 * gridsize, gridsize, gridsize), 0)
        pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 69 + 2 * gridsize, gridsize, gridsize), 1)

    else:
        raise Exception("Unexpected error")
    

def show_score(surface, score):

    font = pygame.font.Font(None, 40)
    text = font.render(f"Lines: {score}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400 + 75, 250 + 38))
    surface.blit(text, text_rect)
