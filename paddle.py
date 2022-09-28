from turtle import Turtle
class Paddle():
    def __init__(self):
            self.starting_positions = [(-20,-280), (-15,-280), (-10,-280),(-5,-280), (0,-280), (5,-280), (10,-280), (15,-280), (20,-280),]
            self.segments=[]
            self.create_paddle()
    
    def create_paddle(self):
        for position in self.starting_positions:
            t =  Turtle()
            t.shape("square")
            t.penup()
            t.shapesize(stretch_len=0.2, stretch_wid=0.5)
            t.color("white")
            t.setheading(0)
            t.goto(position)
            self.segments.append(t)
        


    def move(self):
        
        if self.segments[0].xcor() < 280 and self.segments[3].xcor() > -280:
            for segment in self.segments:
                segment.forward(20)
        elif self.segments[0].xcor() >= 280:
            self.left()
            for segment in self.segments:
                segment.forward(20)
        elif self.segments[3].xcor() <= -280:
            self.right()
            for segment in self.segments:
                segment.forward(20)
    
    def left(self):
        for segment in self.segments:
            segment.setheading(180)
    
    def right(self):
        for segment in self.segments:
            segment.setheading(0)