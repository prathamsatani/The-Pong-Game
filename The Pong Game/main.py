from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup.
screen = Screen()
screen.setup(height=600, width=800)
screen.title("The Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# Initialize paddles.
paddle1 = Paddle(-380, 0)
paddle2 = Paddle(380, 0)

# Initialize the ball.
ball = Ball()

# Initialize the scoreboard
score1 = Scoreboard(-50, 220)
score2 = Scoreboard(50, 220)

# Set the movement of the paddles
screen.onkey(key="Up", fun=paddle2.move_up)
screen.onkeypress(key="Up", fun=paddle2.move_up)
screen.onkey(key="Down", fun=paddle2.move_down)
screen.onkeypress(key="Down", fun=paddle2.move_down)
screen.onkey(key="w", fun=paddle1.move_up)
screen.onkeypress(key="w", fun=paddle1.move_up)
screen.onkey(key="s", fun=paddle1.move_down)
screen.onkeypress(key="s", fun=paddle1.move_down)

# The driver code
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with upper wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce!!
        ball.bounce_y()

    # Detect collision with the paddle.
    if (ball.distance(paddle1) < 50 or ball.distance(paddle2) < 50) and (ball.xcor() > 350 or ball.xcor() < -350):
        # Bounce!!
        ball.bounce_x()

    # Detect for ball out of bounds
    if ball.xcor() > 390:
        score1.increment_score()
        ball.reset_position()
    if ball.xcor() < -390:
        score2.increment_score()
        ball.reset_position()

screen.exitonclick()
