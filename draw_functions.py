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
    font = pygame.font.Font(None, 30)
    text = font.render(f"Lines: {score}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(400 + 75, 400 + 25))
    surface.blit(text, text_rect)


def show_start(surface, screen_size):
    x_size, y_size = screen_size
    font = pygame.font.Font(None, 45)
    text = font.render("Press SPACE to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(x_size / 2, y_size / 2 - 40))
    surface.blit(text, text_rect)
    # Controls
    font = pygame.font.Font(None, 30)
    text = font.render("Use WASD / arrows to control", True, (255, 255, 255))
    text_rect = text.get_rect(center=(x_size / 2, y_size / 2 + 25))
    surface.blit(text, text_rect)
    font = pygame.font.Font(None, 30)
    text = font.render("ESC - quit", True, (255, 255, 255))
    text_rect = text.get_rect(center=(x_size / 2, y_size / 2 + 60))
    surface.blit(text, text_rect)




def show_pause(surface, screen_size):
    x_size, y_size = screen_size
    font = pygame.font.Font(None, 40)
    text = font.render("PAUSED", True, (255, 255, 255))
    text_rect = text.get_rect(center=(x_size / 2, y_size / 2))
    surface.blit(text, text_rect)


def show_game_over(surface, screen_size, score):
    x_size, y_size = screen_size
    font = pygame.font.Font(None, 40)
    text = font.render("GAME OVER", True, (255, 255, 255))
    text_rect = text.get_rect(center=(x_size / 2, y_size / 2 - 40))
    surface.blit(text, text_rect)
    text = font.render(f"Your final score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(x_size / 2, y_size / 2))
    surface.blit(text, text_rect)
    text = font.render("Press R to play again", True, (255, 255, 255))
    text_rect = text.get_rect(center=(x_size / 2, y_size / 2 + 40))
    surface.blit(text, text_rect)


def draw_hold_shape(surface, shape, gridsize):
    """
    Shapes:
    None = none
    0 = I
    1 = square
    2 = J
    3 = L
    4 = 4
    5 = Z
    6 = T
    """
    if shape is None:
        pass
    elif shape == 0:
        for i in range(1, 5):
            pygame.draw.rect(surface, (255, 0, 0), (400 + i * gridsize, 244 + 2 * gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + i * gridsize , 244 + 2 * gridsize, gridsize, gridsize), 1)

    elif shape == 1:
        for i in range(2, 4):
            for j in range(2, 4):
                pygame.draw.rect(surface, (255, 0, 0), (400 + i * gridsize, 230 + j *gridsize, gridsize, gridsize), 0)
                pygame.draw.rect(surface, (0, 0, 0), (400 + i * gridsize , 230 + j * gridsize, gridsize, gridsize), 1)

    elif shape == 2:
        for i in range(1, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 244 + i * gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 244 + i * gridsize, gridsize, gridsize), 1)
        pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 244 + 3 * gridsize, gridsize, gridsize), 0)
        pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 244 + 3 * gridsize, gridsize, gridsize), 1)

    elif shape == 3:
        for i in range(1, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 244 + i * gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 244 + i * gridsize, gridsize, gridsize), 1)
        pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 244 + 3 * gridsize, gridsize, gridsize), 0)
        pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 244 + 3 * gridsize, gridsize, gridsize), 1)

    elif shape == 4:
        for i in range(1, 3):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 244 + i *gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 244 + i * gridsize, gridsize, gridsize), 1)
        for i in range(2, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 244 + i *gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 244 + i * gridsize, gridsize, gridsize), 1)

    elif shape == 5:
        for i in range(1, 3):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 244 + i *gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 244 + i * gridsize, gridsize, gridsize), 1)
        for i in range(2, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 244 + i *gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 244 + i * gridsize, gridsize, gridsize), 1)

    elif shape == 6:
        for i in range(1, 4):
            pygame.draw.rect(surface, (255, 0, 0), (400 + 2 * gridsize, 244 + i * gridsize, gridsize, gridsize), 0)
            pygame.draw.rect(surface, (0, 0, 0), (400 + 2 * gridsize , 244 + i * gridsize, gridsize, gridsize), 1) 
        pygame.draw.rect(surface, (255, 0, 0), (400 + 3 * gridsize, 244 + 2 * gridsize, gridsize, gridsize), 0)
        pygame.draw.rect(surface, (0, 0, 0), (400 + 3 * gridsize , 244 + 2 * gridsize, gridsize, gridsize), 1)

    else:
        raise Exception("Unexpected error")
    

def draw_labels(surface):
    # Next shape label
    font = pygame.font.Font(None, 25)
    text = font.render("Next shape", True, (255, 128, 0))
    text_rect = text.get_rect(center=(475, 75))
    surface.blit(text, text_rect)
    # Held shape label
    font = pygame.font.Font(None, 25)
    text = font.render("Held shape", True, (255, 128, 0))
    text_rect = text.get_rect(center=(475, 250))
    surface.blit(text, text_rect)
    # Controls
    font = pygame.font.Font(None, 25)
    text = font.render("H - hold", True, (255, 255, 255))
    text_rect = text.get_rect(center=(475, 460))
    surface.blit(text, text_rect)
    font = pygame.font.Font(None, 25)
    text = font.render("P - Pause", True, (255, 255, 255))
    text_rect = text.get_rect(center=(475, 485))
    surface.blit(text, text_rect)
    font = pygame.font.Font(None, 25)
    text = font.render("R - Reset", True, (255, 255, 255))
    text_rect = text.get_rect(center=(475, 510))
    surface.blit(text, text_rect)