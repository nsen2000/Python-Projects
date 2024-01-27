from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
timmy.width(1)
timmy.speed("fastest")
t.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

increment = 10

for i in range(int(360/increment)):
    t.colormode(random_colour())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + increment)

screen = Screen()
screen.exitonclick()