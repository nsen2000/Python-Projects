import colorgram
from turtle import Turtle, Screen
import turtle as t
from random import choice

colours = colorgram.extract("painting.jpg", 20)
rgb_colours = []

for x in colours:
    r = x.rgb.r
    g = x.rgb.g
    b = x.rgb.b
    new_colour = (r, g, b)
    rgb_colours.append(new_colour)

rgb = [(236, 35, 108), (221, 231, 238), (145, 28, 66), (230, 237, 232), (239, 75, 36), (7, 148, 95), (222, 170, 45), (183, 158, 47), (44, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 92), (244, 219, 53), (178, 40, 98), (40, 168, 117), (208, 131, 165), (205, 56, 35)]

t.colormode(255)
timmy = t.Turtle()
timmy.speed("slowest")

for row in range(-200, 300, 100):
    for column in range(-200, 200, 100):
        timmy.hideturtle()
        timmy.teleport(column, row)
        timmy.dot(30, choice(rgb))

screen = Screen()
screen.exitonclick()