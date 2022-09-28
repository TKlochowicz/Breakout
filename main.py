from turtle import Turtle, Screen
from paddle import Paddle
from wall import Wall
from ball import Ball
from score import Score
import time

SPEED = 20

game_is_on = True

#Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Breakout")
screen.tracer(0)

#Create the Paddle
pad = Paddle()
screen.update()
screen.listen()
screen.onkey(pad.left, "Left")
screen.onkey(pad.right, "Right")

#Create and build the Wall
w = Wall()
w.build()
screen.update()


#Create the Ball
b = Ball()

#Create Scoreboard
scoreboard = Score()

#Start moving the Paddle 


while game_is_on:
    
    time.sleep(0.1)
    pad.move()
    b.move(SPEED)
    screen.update()
    
    #Detect loosing
    if b.ycor() < -305 + SPEED:
        game_is_on = False
        scoreboard.reset_score()
        scoreboard.game_over()

    #Detect paddle hit
    for segment in pad.segments:
        if b.distance(segment) < SPEED and pad.segments[0].heading() == 0: 
                b.setheading(- b.heading() - 20)
                b.move(SPEED)
        if b.distance(segment) < SPEED and pad.segments[0].heading() == 180: 
                b.setheading(- b.heading() + 20)
                b.move(SPEED)

    #detect side wall hit
    if b.xcor() > 300-SPEED:
        if b.heading() < 180:
            b.setheading(90 + b.heading())
            b.move(SPEED)
        else:
            b.setheading(270 + (270 - b.heading()))
            b.move(SPEED)

    if b.xcor() < -300+SPEED:
        if b.heading() < 180:
            b.setheading(b.heading()-90)
            b.move(SPEED)
        else:
            b.setheading(270 + (270 - b.heading()))
            b.move(SPEED)
    
    #detect back wall hit
    if b.ycor() > 300-SPEED:
        b.setheading(360 - b.heading())
        b.move(SPEED)
    
    #Detect brick hit
    
    for brick in w.bricks:
        for segment in brick:
            if b.distance(segment) < 10:
                b.setheading(-b.heading())
                b.move(SPEED)
                w.disapear(brick)
                scoreboard.brick_destroyed()

screen.exitonclick()