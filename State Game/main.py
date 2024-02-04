import turtle
import pandas
from turtle import Turtle

"""Setting up screen and lists to hold states"""
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
correct_guesses = []
remaining_states = []
score = 0

"""While loop to loop state game until all states are guessed"""
while(score < 50):
    answer_state = screen.textinput(title=f"{score}/50 Guessed", prompt="What's another state?")
    answer_state = answer_state.title()

    for each_state in range(len(data)):
        if answer_state == data["state"][each_state]:
            state = Turtle()
            state.penup()
            state.hideturtle()
            state.goto(data["x"][each_state], data["y"][each_state])
            state.write(f"{data["state"][each_state]}", True, align="center")
            correct_guesses.append(answer_state)
            score += 1
        elif answer_state == "Exit":
            for every_state in correct_guesses:
                if data["state"][each_state] not in correct_guesses and data["state"][each_state] not in remaining_states:
                    remaining_states.append(data["state"][each_state])
            score = 51

new_data = pandas.DataFrame(remaining_states)
new_data.to_csv("states_to_learn.csv")

def get_mouse_click_coor(x, y):
    print(x, y)
    #
    # turtle.onscreenclick(get_mouse_click_coor)
    # turtle.mainloop()
