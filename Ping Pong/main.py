from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
sleep = 0.05

"""Setting up the screen"""
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

"""Creating paddles"""
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_score = Scoreboard()
r_score = Scoreboard()
# l_score.display_score()
# r_score.display_score()

"""Controlling paddles"""
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep)

    """Making ball move"""
    ball.move()

    """Detect if ball collides with wall"""
    ball.bounce()

    """Detect if ball collides with paddle"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.X_DISTANCE = -abs(ball.X_DISTANCE)
        # sleep -= 0.002
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.X_DISTANCE = abs(ball.X_DISTANCE)
        # sleep -= 0.002

    """Detect if right paddle misses ball"""
    if ball.xcor() > 400:
        l_score.leftscore_update()
        ball.reset_position()
        ball.write(" Game over! Left paddle wins!", True, align="center", font=('Arial', 24, 'normal'))
        game_is_on = False
        k = input("press anything to exit")

    """Detect if left paddle misses ball"""
    if ball.xcor() < -440:
        r_score.rightscore_update()
        ball.reset_position()
        ball.write(" Game over! Right paddle wins!", True, align="center", font=('Arial', 24, 'normal'))
        game_is_on = False
        k = input("press anything to exit")


screen.exitonclick()