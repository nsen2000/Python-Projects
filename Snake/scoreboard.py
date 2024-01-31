from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()


    def display_score(self):
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.display_score()

    def get_highscore(self):
        with open("data.txt") as file:
            contents = file.read()
        return int(contents)



