import pygame

# Initialize pygame
pygame.init()

# Set the size of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Pong Game")

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set the paddle sizes and speeds
paddle_width = 20
paddle_height = 100
paddle_speed = 10

# Create the paddles
left_paddle = pygame.Rect(50, 250, paddle_width, paddle_height)
right_paddle = pygame.Rect(screen_width - 50 - paddle_width, 250, paddle_width, paddle_height)

# Create the ball
ball = pygame.Rect(screen_width//2 - 10, screen_height//2 - 10, 20, 20)
ball_speed_x = 5
ball_speed_y = 5

# Set the game loop
game_running = True
clock = pygame.time.Clock() # Create a clock object
while game_running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Move the paddles with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and left_paddle.top > 0:
        left_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN] and left_paddle.bottom < screen_height:
        left_paddle.move_ip(0, paddle_speed)
    if keys[pygame.K_w] and right_paddle.top > 0:
        right_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and right_paddle.bottom < screen_height:
        right_paddle.move_ip(0, paddle_speed)

    # Move the ball
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Check for collision with the paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Check for collision with the top or bottom of the screen
    if ball.top < 0 or ball.bottom > screen_height:
        ball_speed_y *= -1

    # Check for a point scored
    if ball.left < 0:
        print("Player 2 scores!")
        ball.center = (screen_width//2, screen_height//2)
        ball_speed_x *= -1
    if ball.right > screen_width:
        print("Player 1 scores!")
        ball.center = (screen_width//2, screen_height//2)
        ball_speed_x *= -1

    # Draw the screen
    screen.fill(black)
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (screen_width//2, 0), (screen_width//2, screen_height))

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
