# Pong

import turtle
import os
import math
import random

a = 1
# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Pong")
wn.setup(600, 400)

# Field
top = wn.window_height() / 2 - 100
bottom = - wn.window_height() / 2 + 100
left = - wn.window_width() / 2 + 50
right = wn.window_width() / 2 - 50

# Draw border
border_pen = turtle.Turtle()
border_pen.color("black")
border_pen.hideturtle()
border_pen.penup()
border_pen.setposition(right, top)
border_pen.pendown()
border_pen.setposition(left, top)
border_pen.setposition(left, bottom)
border_pen.setposition(right, bottom)
border_pen.setposition(right, top)
border_pen.hideturtle()

# Padle_A
padleA = turtle.Turtle()
padleA.color("black")
padleA.shape("square")
padleA.shapesize(2, 0.3)
padleA.penup()
padleA.speed(0)
padleA.setposition(left + 10, 0)

# Padle_B
padleB = turtle.Turtle()
padleB.color("black")
padleB.shape("square")
padleB.shapesize(2, 0.3)
padleB.penup()
padleB.speed(0)
padleB.setposition(right - 10, 0)

padlespeed = 20
ballspeed1 = 3
ballspeed2 = 3

# Ball
ball = turtle.Turtle()
ball.penup()
ball.color("black")
ball.shape("circle")
ball.shapesize(0.5, 0.5)
ball.speed(0)

# Score
score = turtle.Turtle()
score.penup()
score.hideturtle()

score_1 = 0
score_2 = 0


def write_scores():
    score.clear()
    score.setposition(-100, top + 5)
    score.write(score_1, align="center", font=("Arial", 32, "bold"))
    score.setposition(100, top + 5)
    score.write(score_2, align="center", font=("Arial", 32, "bold"))


creator = turtle.Turtle()
creator.penup()
creator.hideturtle()


def write_creator():
    creator.clear()
    creator.setposition(0, bottom - 80)
    creator.write("GAME CREATED BY ADAM HACIA", align="center", font=("Arial", 10, "bold"))
    creator.setposition(0, bottom - 90)
    creator.write("SPECIAL THANKS TO ZOFIA HACIA", align="center", font=("Arial", 10, "bold"))


write_scores()
write_creator()
# Move the player


def move_up_A():
    y = padleA.ycor()
    y += padlespeed
    if y > top - 20:
        y = top - 20
    padleA.sety(y)


def move_down_A():
    y = padleA.ycor()
    y -= padlespeed
    if y < bottom + 20:
        y = bottom + 20
    padleA.sety(y)


def move_up_B():
    y = padleB.ycor()
    y += padlespeed
    if y > top - 20:
        y = top - 20
    padleB.sety(y)


def move_down_B():
    y = padleB.ycor()
    y -= padlespeed
    if y < bottom + 20:
        y = bottom + 20
    padleB.sety(y)


# Create keyboard binding
wn.listen()
wn.onkey(move_up_B, "Up")
wn.onkey(move_down_B, "Down")
wn.onkey(move_up_A, "w")
wn.onkey(move_down_A, "s")

# Main game loop
wygrana = 3
while score_1 != wygrana and score_2 != wygrana:
    # Move the ball
    x = ball.xcor()
    y = ball.ycor()
    x += ballspeed1
    y += ballspeed2
    ball.setposition(x, y)

    # Borders control
    if ball.xcor() > right - 5:
        ball.setposition(0, 0)
        # ballspeed1 = random.randint(1, 2)
        # ballspeed2 = random.randint(1, 2)
        ballspeed1 *= -1
        score_1 += 1
        write_scores()
        a = 0

    if ball.xcor() < left + 5:
        ball.setposition(0, 0)
        # ballspeed1 = random.randint(1, 2)
        # ballspeed2 = random.randint(1, 2)
        ballspeed1 *= -1
        score_2 += 1
        write_scores()
        a = 1

    if ball.ycor() > top - 5:
        ballspeed2 *= -1
        os.system("afplay bounce.mp3&")

    if ball.ycor() < bottom + 5:
        ballspeed2 *= -1
        os.system("afplay bounce.mp3&")

    # Padle
    if a == 0:
        if (ball.ycor() < padleA.ycor() + 20) and (ball.ycor() > padleA.ycor() - 20) and (ball.xcor() == padleA.xcor()):
            ballspeed1 *= -1
            a = 1
            # ballspeed1 += 0.1
            # ballspeed2 += 0.1
            # os.system("afplay a.mp3&")

    if a == 1:
        if (ball.ycor() < padleB.ycor() + 20) and (ball.ycor() > padleB.ycor() - 20) and (ball.xcor() == padleB.xcor()):
            ballspeed1 *= -1
            a = 0
            # ballspeed1 += 0.1
            # ballspeed2 += 0.1
            # os.system("afplay a.mp3&")

ball.hideturtle()
if score_2 == wygrana:
    score.setposition(100, top + 50)
else:
    score.setposition(-100, top + 50)
score.write("WINNER", align="center", font=("Arial", 32, "bold"))
score.setposition(0, bottom - 50)
score.write("THANK YOU FOR PLAYING", align="center", font=("Arial", 32, "bold"))
wn.mainloop()
