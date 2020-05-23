# Might have to install using this: python3 -m pip install -U pygame==2.0.0.dev6 --user

import pygame
from random import randint

def get_fruit_spawn_location():
    locations = (
        (50,50),
        (430,50),
        (430,430),
        (50,430))
    random_number = randint(0,3)
    return locations[random_number]

def main():

    # Game constants
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    BLACK_COLOUR = (0,0,0)
    WHITE_COLOUR = (255,255,255)
    FRUIT_COLOUR = (255,0,0)
    SNAKE_COLOUR = (0,0,255)
    SNAKE_WIDTH = 20
    SNAKE_HEIGHT = 20
    # Game variables
    is_game_over = False
    score = 0
    speed = 1
    snake_x = 239
    snake_y = 239
    x_change = 0
    y_change = 0
    should_generate_new_fruit = False
    fruit_location = get_fruit_spawn_location()

    # Basic set up
    pygame.init()
    pygame.display.set_caption("Simple Snake")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Set up score text
    font = pygame.font.Font("assets/Arial.ttf", 24)
    score_text_position = (10,10)

    # Main game loop
    while True:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if not is_game_over:
                    if event.key == pygame.K_LEFT:
                        x_change = -speed
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = speed
                        y_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = speed
                        x_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -speed
                        x_change = 0
                else:
                    if event.key == pygame.K_SPACE:
                        score = 0
                        speed = 1
                        is_game_over = False
                        x_change = 0
                        y_change = 0
                        snake_x = 239
                        snake_y = 239
                

        # Update states
        if not is_game_over:
            snake_x += x_change
            snake_y += y_change
        if should_generate_new_fruit:
            fruit_location = get_fruit_spawn_location()
            should_generate_new_fruit = False

        # Check for collisions
        if snake_x < 0 or snake_y < 0 or snake_x > (SCREEN_WIDTH - SNAKE_WIDTH) or snake_y > (SCREEN_HEIGHT - SNAKE_HEIGHT):
            is_game_over = True
        elif (snake_x + SNAKE_WIDTH) > fruit_location[0] and snake_x < (fruit_location[0] + SNAKE_WIDTH) and (snake_y + SNAKE_HEIGHT) > fruit_location[1] and snake_y < (fruit_location[1] + SNAKE_HEIGHT):
            score += 1
            should_generate_new_fruit = True

        # Render graphics   
        screen.fill(BLACK_COLOUR)
        # Draw snake
        pygame.draw.rect(screen, SNAKE_COLOUR, (snake_x,snake_y,SNAKE_WIDTH,SNAKE_HEIGHT), 0)
        # Draw fruit
        pygame.draw.rect(screen, FRUIT_COLOUR, (fruit_location[0], fruit_location[1], SNAKE_WIDTH, SNAKE_HEIGHT))
        # Draw texts
        if is_game_over:
            end_game_text = font.render("Game over! Final score: {}".format(score), 0, WHITE_COLOUR)
            play_again_text = font.render("Press SPACE to play again", 0, WHITE_COLOUR)
            end_game_text_rect = end_game_text.get_rect()
            end_game_text_rect.center = (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 25)
            play_again_text_rect = play_again_text.get_rect()
            play_again_text_rect.center = (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 25)
            screen.blit(end_game_text, end_game_text_rect)
            screen.blit(play_again_text, play_again_text_rect)
        else:
            score_text = font.render("Score: {}".format(score), 1, WHITE_COLOUR)
            screen.blit(score_text, score_text_position)
        
        pygame.display.update()
        


# Starts the program if run from main thread
if __name__ == "__main__":
    main()