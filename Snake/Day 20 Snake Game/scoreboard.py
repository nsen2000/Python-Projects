from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def display_score(self):
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

