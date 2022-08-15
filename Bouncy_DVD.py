# Pong Project
# By James Bernau
# Pt. 1

import turtle

wn = turtle.Screen()
wn.title("Bouncy")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red") 
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = 0


# Function
def ball_up():
    ball.dx = 0
    ball.dy = 6



def ball_down():
    ball.dx = 0
    ball.dy = -6


def ball_left():
    ball.dx = -6
    ball.dy = 0


def ball_right():
    ball.dx = 6
    ball.dy = 0


def clear_pen():
    ball.clear()


def stop():
    ball.dx = 0
    ball.dy = 0


def pen_stop():
    ball.penup()


def pen_go():
    ball.pendown()


# Keyboard Binding
wn.listen()
wn.onkeypress(ball_up, "w")
wn.onkeypress(ball_down, "s")
wn.onkeypress(ball_left, "a")
wn.onkeypress(ball_right, "d")
wn.onkeypress(clear_pen, "c")
wn.onkeypress(stop, "e")
wn.onkeypress(pen_stop, "q")
wn.onkeypress(pen_go, "r")

# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1




