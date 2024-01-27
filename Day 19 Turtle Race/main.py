from turtle import Turtle, Screen
import random

"""Setting up the screen and screen size"""
screen = Screen()
screen.setup(500, 400)

"""Asking user to pick a turtle colour and creating variables"""
user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle will win the race? Enter a colour: (blue, red, orange, green, pink or orange)")
colours = ["red", "green", "blue", "orange", "yellow", "pink"]
y = 100
is_race_on = True
all_turtles = []

"""Creating turtle objects"""
for i in colours:
    timmy = Turtle(shape="turtle")
    timmy.color(i)
    timmy.penup()
    timmy.goto(-230, y)
    y -= 40
    all_turtles.append(timmy)

"""Moving each turtle a random amount and checking which turtle has won"""
while is_race_on == True:
    for each_turtle in all_turtles:

        if each_turtle.xcor() >= 200:
            is_race_on = False
            winning_colour = each_turtle.pencolor()
            if user_bet == each_turtle.pencolor():
                print(f"The {winning_colour} turtle won! You won the bet!")
                # k = input("press anything to exit")
            else:
                print(f"The {winning_colour} turtle won! You lost the bet!")
                # k = input("press anything to exit")

        jump = random.randint(0, 10)
        each_turtle.forward(jump)

screen.exitonclick()