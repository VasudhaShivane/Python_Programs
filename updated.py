import turtle
import pygame  # You'll need to install pygame for sound effects

# Initialize pygame for sound effects
pygame.mixer.init()

# Load sound files
hit_sound = pygame.mixer.Sound("hit.wav")  # Replace with your sound file
score_sound = pygame.mixer.Sound("score.wav")  # Replace with your sound file

def play_hit_sound():
    hit_sound.play()

def play_score_sound():
    score_sound.play()

def update_score(l_score, r_score, player, score_board):
    if player == 'l':
        l_score += 1
    else:
        r_score += 1

    score_board.clear()
    score_board.write('Left Player: {} -- Right Player: {}'.format(
        l_score, r_score), align='center',
        font=('Arial', 24, 'normal'))
    return l_score, r_score, score_board

def setup_game():
    screen = turtle.Screen()
    screen.title('Pong Arcade Game')
    screen.bgcolor('cornsilk')
    screen.setup(width=1000, height=600)
    screen.bgpic("background.png")  # Set background image

    l_paddle = turtle.Turtle()
    l_paddle.speed(0)
    screen.addshape("paddle_left.gif")  # Replace with your paddle image file
    l_paddle.shape("paddle_left.gif")
    l_paddle.penup()
    l_paddle.goto(-400, 0)

    r_paddle = turtle.Turtle()
    r_paddle.speed(0)
    screen.addshape("paddle_right.gif")  # Replace with your paddle image file
    r_paddle.shape("paddle_right.gif")
    r_paddle.penup()
    r_paddle.goto(400, 0)

    ball = turtle.Turtle()
    ball.speed(40)
    screen.addshape("ball.gif")  # Replace with your ball image file
    ball.shape("ball.gif")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 5
    ball.dy = -5

    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.color('darkslategray')
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, 260)
    score_board.write('Left Player: 0 -- Right Player: 0',
                     align='center', font=('Arial', 24, 'normal'))

    return screen, ball, l_paddle, r_paddle, score_board

# Rest of the code remains the same as your original Pong game

if __name__ == '__main__':
    pong_game()
