from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        # self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Score: {self.right_score}", True, align=ALIGNMENT, font=FONT)
        self.goto(200, 260)
        self.write(f"Score: {self.left_score}", True, align=ALIGNMENT, font=FONT)

    def leftscore_update(self):
        # self.clear()
        self.left_score += 1
        # self.display_score()

    def rightscore_update(self):
        # self.clear()
        self.right_score += 1
        # self.display_score()
