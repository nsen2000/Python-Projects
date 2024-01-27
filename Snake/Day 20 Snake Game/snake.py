from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for block in STARTING_POSITIONS:
            self.add_segment(block)

    def add_segment(self, block):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(block)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)