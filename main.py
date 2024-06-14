import pygame
import random

from functions import *

pygame.init()

# Define constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (32, 32, 32)
LIGTH_GREY = (64, 64, 64)
ORANGE = (255, 128, 0)

# Set up the clock for a decent frame rate
clock = pygame.time.Clock()
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")


# Define the frame's position and size
GAME_X_POSITION = 50
GAME_Y_POSITION = 50
GAME_WIDTH = 250
GAME_HEIGTH = 500
# Left, Right, Down
GAME_LIMITS = (GAME_X_POSITION + 5, GAME_X_POSITION + GAME_WIDTH + 5, GAME_Y_POSITION + GAME_HEIGTH + 5)
game_window = pygame.Rect(GAME_X_POSITION, GAME_Y_POSITION, GAME_WIDTH + 10, GAME_HEIGTH + 10)

GRID_SIZE = 25
GRID_WIDTH = GAME_WIDTH // GRID_SIZE
GRID_HEIGHT = GAME_HEIGTH // GRID_SIZE
# Define the game board matrix
board = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Showing next shape
next_window = pygame.Rect(400, 55, 6 * GRID_SIZE, 6 * GRID_SIZE)

# Showing score
score_window = pygame.Rect(400, 250, 150, 75)

# Add a timer for automatic falling
fall_time = 0
fall_speed = 100 # Milliseconds per grid cell

lines = 0

current_shape = random.randrange(0,7)
# next_shape = random.randrange(0,7)
next_shape = 0

new_shape(board, current_shape)

# Main game loop
running = True
while running:
    # Running clock
    fall_time += clock.get_rawtime()

    # User events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_shape(board, "left")
            elif event.key == pygame.K_RIGHT:
                move_shape(board, "right")
            elif event.key == pygame.K_DOWN:
                if move_shape(board, "down"):
                    # New shape drop
                    current_shape = next_shape
                    next_shape = random.randrange(0,7)
                    new_shape(board, current_shape)
            elif event.key == pygame.K_UP:
                print(board)


    screen.fill(DARK_GREY)

    # Game field
    draw_frame(screen, game_window, BLACK, ORANGE, 5)
    draw_grid(screen, GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, (GAME_X_POSITION + 5, GAME_Y_POSITION + 5), board)
    
    if fall_time >= fall_speed:
        if move_shape(board, "down"):
            # New shape drop
                    current_shape = next_shape
                    next_shape = random.randrange(0,7)
                    new_shape(board, current_shape)
        fall_time = 0

    draw_shape(screen, board, GRID_SIZE)

    lines = check_lines(lines, board)

    # Show score
    draw_frame(screen, score_window, BLACK, ORANGE, 5)
    show_score(screen, lines)
    # Show next shape
    draw_frame(screen, next_window, BLACK, ORANGE, 5)
    draw_next_shape(screen, next_shape, GRID_SIZE)

    # Update the screen
    pygame.display.flip() 
    
    # Cap the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()