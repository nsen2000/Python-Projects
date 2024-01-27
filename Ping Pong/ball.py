from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.X_DISTANCE = 5
        self.Y_DISTANCE = 5

    def move(self):
        # self.seth(35)
        # for spot in range(0,20,1):
        #     self.forward(spot/100)

        new_x = self.xcor() + self.X_DISTANCE
        new_y = self.ycor() + self.Y_DISTANCE
        self.goto(new_x, new_y)

    def bounce(self):
        if self.ycor() > 280:
            self.Y_DISTANCE = -abs(self.Y_DISTANCE)
        if self.ycor() < -275:
            self.Y_DISTANCE = abs(self.Y_DISTANCE)

    def reset_position(self):
        self.goto(0, 0)
        self.X_DISTANCE *= -1




