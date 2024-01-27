from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.width(8)


direction = ["l", "r", "f", "b"]
angles = [0, 90, 180, 270]
numbers = [0, 1, 2, 3]
run = True
i = 0
timmy.speed("fastest")

while (i < 100):
    for r in ('blue', 'red', 'green', 'yellow', 'black', 'orange', 'beige', 'coral'):
        x = random.choice(numbers)
        timmy.color(r)
        if direction[x] == "f":
            timmy.forward(20)
        elif direction[x] == "r":
            timmy.right(90)
        elif direction[x] == "l":
            timmy.left(90)
    i += 1

screen = Screen()
screen.exitonclick()

