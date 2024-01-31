from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

"""Setting up blank screen"""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

"""Initialising food and snake objects from classes"""
snake = Snake()
food = Food()
score = Scoreboard()
score.display_score()

"""Listen to key inputs"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake. down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()
    """Detect if snake has reached food"""
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    """Detect if snake collides with wall"""
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -290:
        score.game_over()
        snake.reset()

    """Detect collision with tail"""
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score.game_over()
            snake.reset()

screen.exitonclick()
