import pygame
import random

# Initialize pygame
pygame.init()

# Set the size of the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set the font
font = pygame.font.SysFont('Arial', 30)

# Set the snake block size and speed
block_size = 10
snake_speed = 15

# Create the snake
def create_snake():
    snake_length = 1
    snake_list = []
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    for i in range(snake_length):
        snake_list.append((snake_x, snake_y))
    return snake_list

# Draw the snake
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, block_size, block_size])

# Move the snake
def move_snake(snake_list, direction):
    head_x, head_y = snake_list[-1]
    new_head = (head_x, head_y)  # Define a default value for new_head
    if direction == "up":
        new_head = (head_x, head_y - block_size)
    elif direction == "down":
        new_head = (head_x, head_y + block_size)
    elif direction == "left":
        new_head = (head_x - block_size, head_y)
    elif direction == "right":
        new_head = (head_x + block_size, head_y)

    # Check for collision with body
    if new_head in snake_list[:-1]:
        # Collision with body, end the game
        game_running = False
        return snake_list

    snake_list.append(new_head)
    del snake_list[0]
    return snake_list

# Check for collision with food
def check_food_collision(snake_list, food_x, food_y):
    head_x, head_y = snake_list[-1]
    if head_x == food_x and head_y == food_y:
        return True
    else:
        return False

# Create the food
def create_food():
    food_x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
    return food_x, food_y

# Draw the food
def draw_food(food_x, food_y):
    pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

# Set the game loop
def game_loop():
    snake_list = create_snake()
    direction = "right"
    food_x, food_y = create_food()
    score = 0

    game_running = True
    clock = pygame.time.Clock()
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "down":
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
                elif event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"

        snake_list = move_snake(snake_list, direction)

        if check_food_collision(snake_list, food_x, food_y):
            # Update score and display it
            score += 10
            score_text = font.render("Score: " + str(score), True, white)
            screen.blit(score_text, (10, 10))

            # Generate new food location
            food_x, food_y = create_food()

            # Increase the length of the snake
            snake_list.append(snake_list[-1])

        # Fill the screen with black color
        screen.fill(black)

        # Draw the snake and food
        draw_snake(snake_list)
        draw_food(food_x, food_y)

        # Update the display
        pygame.display.update()

        # Slow down the game
        clock.tick(snake_speed)

    # Add a delay before quitting the game
    pygame.time.delay(1000)

    # Quit pygame
    print("Game loop finished")
    pygame.quit()

game_loop()