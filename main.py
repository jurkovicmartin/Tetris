import pygame
import random

from game_functions import *
from draw_functions import *
from rotating import rotate_shape


def main():
    pygame.init()
    pygame.mixer.init()

    # Define constants
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 600

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    DARK_GREY = (32, 32, 32)
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

    # Music and sounds
    pygame.mixer.music.load("audio/background.mp3")
    pygame.mixer.music.set_volume(0.2)
    full_line_sound = pygame.mixer.Sound("audio/line_sound.mp3")
    game_over_sound = pygame.mixer.Sound("audio/game_over.mp3")

    # Showing next shape
    next_window = pygame.Rect(400, 55, 6 * GRID_SIZE, 6 * GRID_SIZE)
    # Holding shape
    hold_window = pygame.Rect(400, 230, 6 * GRID_SIZE, 6 * GRID_SIZE)
    # Showing score
    score_window = pygame.Rect(400, 400, 150, 160)

    # Add a timer for automatic falling
    fall_time = 0
    fall_speed = 500 # Milliseconds per grid cell

    # Set key repeat to enable holding keys
    pygame.key.set_repeat(200, 100)  # (delay, interval)

    lines = 0

    # Start of the game
    message_background = pygame.Rect(175, 200, 350, 200)
    showing_start = True
    pause = True
    mute = False
    # Game over
    over = False


    current_shape = random.randrange(0,7)
    next_shape = random.randrange(0,7)
    held_shape = None
    rotation_state = 0

    new_shape(board, current_shape)


    running = True
    # Main game loop
    while running:
        # Running clock
        fall_time += clock.get_rawtime()

        track_lines = lines

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
                        # Game over
                        if over:
                            if not mute:
                                pygame.mixer.music.pause()
                                game_over_sound.play()
                        else:
                            # New shape drop
                            current_shape = next_shape
                            next_shape = random.randrange(0,7)
                            new_shape(board, current_shape)
                            rotation_state = 0
                    # Check for full layers
                    lines = check_lines(lines, board)
                elif event.key == pygame.K_UP and not pause and not over:
                    rotation_state = rotate_shape(board, current_shape, rotation_state)
                
                elif event.key == pygame.K_a and not pause and not over:
                    move_shape(board, "left")
                elif event.key == pygame.K_d and not pause and not over:
                    move_shape(board, "right")
                elif event.key == pygame.K_s and not pause and not over:
                    if move_shape(board, "down"):
                        # Check for game over
                        over = check_game_over(board)
                        # Game over
                        if over:
                            if not mute:
                                pygame.mixer.music.pause()
                                game_over_sound.play()
                        else:
                            # New shape drop
                            current_shape = next_shape
                            next_shape = random.randrange(0,7)
                            new_shape(board, current_shape)
                            rotation_state = 0
                    # Check for full layers
                    lines = check_lines(lines, board)
                elif event.key == pygame.K_w and not pause and not over:
                    rotation_state = rotate_shape(board, current_shape, rotation_state)
                
                # Start
                elif event.key == pygame.K_SPACE and not over:
                    pause = False
                    showing_start = False
                    # Start playing background music in loop
                    pygame.mixer.music.play(-1)
                # Pause
                elif event.key == pygame.K_p and not showing_start and not over:
                    if pause:
                        pause = False
                        # Pause background music
                        pygame.mixer.music.unpause()
                    else:
                        pause = True
                        # Unpause background music
                        pygame.mixer.music.pause()
                # Reset
                elif event.key == pygame.K_r and not showing_start:
                    # Reset run variables
                    showing_start = True
                    pause = True
                    over = False
                    lines = 0
                    fall_speed = 500
                    # Clear the field
                    board = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
                    # Pause background music
                    pygame.mixer.music.pause()
                    # New shapes
                    current_shape = random.randrange(0,7)
                    next_shape = random.randrange(0,7)
                    new_shape(board, current_shape)
                    rotation_state = 0
                    held_shape = None
                # Hold
                elif event.key == pygame.K_h and not pause and not over:
                    current_shape, next_shape, held_shape = hold_shape(board, current_shape, next_shape, held_shape)
                    new_shape(board, current_shape)
                    rotation_state = 0
                # Quit
                elif event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_m:
                    if mute:
                        mute = False
                        pygame.mixer.music.unpause()
                    else:
                        mute = True
                        pygame.mixer.music.pause()
                else: pass
            else: pass


        screen.fill(DARK_GREY)

        # Game field
        draw_frame(screen, game_window, BLACK, ORANGE, 5)
        draw_grid(screen, GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, (GAME_X_POSITION + 5, GAME_Y_POSITION + 5))
        
        # Automatic dropping
        if not pause and not over:
            if fall_time >= fall_speed:
                if move_shape(board, "down"):
                    # Check for game over
                    over = check_game_over(board)
                    # Game over
                    if over:
                        if not mute:
                            pygame.mixer.music.pause()
                            game_over_sound.play()
                    else:
                        # New shape drop
                        current_shape = next_shape
                        next_shape = random.randrange(0,7)
                        new_shape(board, current_shape)
                        rotation_state = 0
                # Check for full layers
                lines = check_lines(lines, board)
                fall_time = 0

        # Adding speed
        if track_lines != lines:
            if not mute:
                full_line_sound.play()
            # Speed limit
            if fall_speed != 20:
                fall_speed = fall_speed - 5


        draw_shape(screen, board, GRID_SIZE)

        # Show next shape
        draw_frame(screen, next_window, BLACK, ORANGE, 5)
        draw_next_shape(screen, next_shape, GRID_SIZE)
        # Show hold shape
        draw_frame(screen, hold_window, BLACK, ORANGE, 5)
        draw_hold_shape(screen, held_shape, GRID_SIZE)
        # Show score
        draw_frame(screen, score_window, BLACK, ORANGE, 5)
        show_score(screen, lines)
        # Show labels
        draw_labels(screen)

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



if __name__ == "__main__":
    main()