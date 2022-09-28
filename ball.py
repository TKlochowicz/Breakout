from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.goto((0,0))
        self.setheading(270)

    def move(self, SPEED):
        self.forward(SPEED)