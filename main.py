import pygame
import random

from game_functions import *
from draw_functions import *

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

# Set key repeat to enable holding keys
pygame.key.set_repeat(100, 100)  # (delay, interval)

lines = 0

# Start of the game
showing_start = True
message_background = pygame.Rect(200, 200, 300, 200)
# Pause the game
pause = True
# Game over
over = False

current_shape = random.randrange(0,7)
next_shape = random.randrange(0,7)

new_shape(board, current_shape)


running = True
# Main game loop
while running:
    # Running clock
    fall_time += clock.get_rawtime()

    # User events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not pause and not over:
                move_shape(board, "left")
            elif event.key == pygame.K_RIGHT and not pause and not over:
                move_shape(board, "right")
                
            elif event.key == pygame.K_DOWN and not pause and not over:
                if move_shape(board, "down"):
                    # Check for game over
                    over = check_game_over(board)
                    if not over:
                        # New shape drop
                        current_shape = next_shape
                        next_shape = random.randrange(0,7)
                        new_shape(board, current_shape)
                # Check for full layers
                lines = check_lines(lines, board)

            elif event.key == pygame.K_UP and not pause and not over:
                print(board)
            # Start
            elif event.key == pygame.K_SPACE and not over:
                pause = False
                showing_start = False
            # Pause
            elif event.key == pygame.K_p and not showing_start and not over:
                if pause:
                    pause = False
                else:
                    pause = True
            # Reset
            elif event.key == pygame.K_r and not showing_start:
                # Reset run variables
                showing_start = True
                pause = True
                over = False
                lines = 0
                # Clear the field
                board = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
                # New shapes
                current_shape = random.randrange(0,7)
                next_shape = random.randrange(0,7)
                new_shape(board, current_shape)
            else: pass
        else: pass


    screen.fill(DARK_GREY)

    # Game field
    draw_frame(screen, game_window, BLACK, ORANGE, 5)
    draw_grid(screen, GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, (GAME_X_POSITION + 5, GAME_Y_POSITION + 5), board)
    
    # Automatic dropping
    if not pause and not over:
        if fall_time >= fall_speed:
            if move_shape(board, "down"):
                # Check for game over
                over = check_game_over(board)
                if not over:
                    # New shape drop
                    current_shape = next_shape
                    next_shape = random.randrange(0,7)
                    new_shape(board, current_shape)
            # Check for full layers
            lines = check_lines(lines, board)

            fall_time = 0


    draw_shape(screen, board, GRID_SIZE)

    # Show score
    draw_frame(screen, score_window, BLACK, ORANGE, 5)
    show_score(screen, lines)
    # Show next shape
    draw_frame(screen, next_window, BLACK, ORANGE, 5)
    draw_next_shape(screen, next_shape, GRID_SIZE)

    # At the start
    if showing_start:
        draw_frame(screen, message_background, BLACK, WHITE, 5)
        show_start(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # Paused
    elif pause:
        draw_frame(screen, message_background, BLACK, WHITE, 5)
        show_pause(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # Game over
    elif over:
        draw_frame(screen, message_background, BLACK, WHITE, 5)
        show_game_over(screen, (SCREEN_WIDTH, SCREEN_HEIGHT), lines)
    else: pass

    # Update the screen
    pygame.display.flip() 
    
    # Cap the frame rate to 60 FPS
    clock.tick(60)

pygame.quit()