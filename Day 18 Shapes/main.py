from turtle import Turtle, Screen

timmy = Turtle()
timmy.color("red")

sides = 3
angle = 360/sides

for i in ('blue', 'red', 'green', 'yellow', 'black', 'orange', 'beige', 'coral'):
    timmy.color(i)
    for x in range(sides):
        timmy.forward(100)
        timmy.right(angle)
    sides += 1
    angle = 360/sides


screen = Screen()
screen.exitonclick()