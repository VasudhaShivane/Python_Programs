import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
BALL_SPEED = [5, 3]  # Increase ball speed
PADDLE_SPEED = 4
FONT = "comicsansms"  # You can replace this with your preferred font

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Load background image
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Paddle attributes
paddle_width, paddle_height = 10, 100
paddle_color = (255, 255, 255)
left_paddle = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)

# Ball attributes
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_color = (255, 255, 255)

# Ball movement
ball_direction = [random.choice((1, -1)), random.choice((1, -1))]

# Player points
left_player_score = 0
right_player_score = 0

# Maximum number of moves
max_moves = 10
current_move = 0

# Game over font
game_over_font = pygame.font.Font(None, 72)

# Main menu
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw the background
        screen.blit(background_image, (0, 0))

        # Create menu text
        menu_text = game_over_font.render("Pong Game", True, WHITE)
        start_text = pygame.font.Font(None, 48).render("Press SPACE to Start", True, WHITE)

        # Position the text on the screen
        menu_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        # Blit the text to the screen
        screen.blit(menu_text, menu_rect)
        screen.blit(start_text, start_rect)

        pygame.display.flip()

        # Check for keypress to start the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_loop()

# Game loop
def game_loop():
    # Initialize game variables
    global left_player_score, right_player_score
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_direction[0] = random.choice((1, -1))
    ball_direction[1] = random.choice((1, -1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED

        # AI for the right paddle (simple tracking)
        if right_paddle.centery < ball.centery:
            right_paddle.y += PADDLE_SPEED
        if right_paddle.centery > ball.centery:
            right_paddle.y -= PADDLE_SPEED

        # Ball movement
        ball.x += BALL_SPEED[0] * ball_direction[0]
        ball.y += BALL_SPEED[1] * ball_direction[1]

        # Ball collisions
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_direction[1] *= -1
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_direction[0] *= -1

        # Ball out of bounds
        if ball.left <= 0:
            right_player_score += 1
            reset_ball()
        if ball.right >= WIDTH:
            left_player_score += 1
            reset_ball()

        # Draw the background
        screen.blit(background_image, (0, 0))

        # Render the paddles, ball, and game elements
        pygame.draw.rect(screen, paddle_color, left_paddle)
        pygame.draw.rect(screen, paddle_color, right_paddle)
        pygame.draw.ellipse(screen, ball_color, ball)

        # Display scores
        left_text = game_over_font.render(f"Left: {left_player_score}", True, WHITE)
        right_text = game_over_font.render(f"Right: {right_player_score}", True, WHITE)
        screen.blit(left_text, (50, 20))
        screen.blit(right_text, (WIDTH - 200, 20))

        # Update the display
        pygame.display.flip()

        # Check for game over
        if left_player_score >= max_moves or right_player_score >= max_moves:
            game_over(left_player_score, right_player_score)

        # Control the game speed
        pygame.time.delay(10)

# Reset ball to the center
def reset_ball():
    global current_move
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_direction[0] = random.choice((1, -1))
    ball_direction[1] = random.choice((1, -1))

    current_move += 1

# Game over screen
def game_over(left_score, right_score):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw the background
        screen.blit(background_image, (0, 0))

        # Create game over text
        game_over_text = game_over_font.render("Game Over", True, WHITE)
        result_text = game_over_font.render("Left Wins!" if left_score > right_score else "Right Wins!", True, WHITE)

        # Position the text on the screen
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        # Blit the text to the screen
        screen.blit(game_over_text, game_over_rect)
        screen.blit(result_text, result_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
