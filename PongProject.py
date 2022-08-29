# Pong Project
# By James Bernau
# Pt. 1

import turtle   # Turtle is the main feature of the program, it draws the ball and paddles and allows them to move.

wn = turtle.Screen()    # Defining the name, colour, and shape of the game window
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)    # This defines the window size and allows me to position turtles in various places
wn.tracer(0)


# Score
score_a = 0    # These variables keep track of the points scored by player a and player b
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # Paddle a is a turtle - it can move and be whatever shape or colour is chosen
paddle_a.speed(0)   # The paddle does not move from it's fixed position
paddle_a.shape("square")
paddle_a.color("white")    # Colour and shape are that of the classic paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    # Stretching width and length makes the paddle into a rectangle, which is the intended shape
paddle_a.penup()    # When the paddle moves, it will not leave a trail
paddle_a.goto(-350, 0)  # This is where the paddle will be positioned on the window, at the far left of the screen.

# Paddle B - Same as paddle a, just positioned in the far right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")    # Shape and colour is the 'ball' shape from classic pong
ball.penup()    # Ball will not leave a trail
ball.goto(0, 0)    # Ball starts in the centre of the screen
ball.dx = 3   # ball.dx and ball.dy define the speed at which the ball moves
ball.dy = -3


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()    # Pen has no trail
pen.hideturtle()    # Pen cannot be seen
pen.goto(0, 260)    # Pen moves to these coordinates
pen.write("A SCORE - 0 - 0 - B SCORE", align="center", font=("Courier", 24, "normal"))    # This defines what is written by the pen, the font and size


# Function
def paddle_a_up():
    y = paddle_a.ycor()    # Checks for the y coordinate of the paddle and assigns it to the variable 'y'
    y += 30    # Adds 30 pixels to the y variable
    paddle_a.sety(y)    # Moves the paddle up 30 pixels

def paddle_a_down():
    y = paddle_a.ycor()    # Checks for the y coordinate of the paddle and assigns it to the variable 'y'
    y -= 30    # Subtracts 30 pixels to the y variable
    paddle_a.sety(y)    # Moves the paddle down 30 pixels

def paddle_b_up():
    y = paddle_b.ycor()    # Checks for the y coordinate of the paddle and assigns it to the variable 'y'
    y += 30    # Adds 30 pixels to the y variable
    paddle_b.sety(y)    # Moves the paddle up 30 pixels

def paddle_b_down():
    y = paddle_b.ycor()    # Checks for the y coordinate of the paddle and assigns it to the variable 'y'
    y -= 30    # Subtracts 30 pixels to the y variable
    paddle_b.sety(y)    # Moves the paddle down 30 pixels

# Keyboard Binding
wn.listen()    # The program can detect inputs
wn.onkeypress(paddle_a_up, "w")    # When 'w' key is pressed, paddle a moves up, according to the paddle_a_up function
wn.onkeypress(paddle_a_down, "s")    # When 's' key is pressed, paddle a moves down, according to the paddle_a_down function
wn.onkeypress(paddle_b_up, "Up")    # When up arrow key is pressed, paddle b moves up, according to the paddle_b_up function
wn.onkeypress(paddle_b_down, "Down")    # When down arrow key is pressed, paddle b moves down, according to the paddle_b_down function

# Main Game Loop - updates each loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)    # These add the ball's current coordinates to the ball.dx and ball.dy, moving it

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1    # If the ball collides with the top border, it will 'bounce' off

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    # If the ball collides with the bottom border, it will 'bounce' off

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1    # When the ball reaches the left border, the ball teleports to the centre and restarts, the score is increased to the player that scored
        pen.clear()
        pen.goto(0, 260)
        pen.write("A SCORE - {} - {} - B SCORE".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))    # The pen increases the new scores and updates the display

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1    # When the ball reaches the right border, the ball teleports to the centre and restarts, the score is increased to the player that scored
        pen.clear()
        pen.goto(0, 260)
        pen.write("A SCORE - {} - {} - B SCORE".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))    # The pen increases the new scores and updates the display

    # Paddle and ball collisions, Ball speed
    if (ball.xcor() > 340 and ball.xcor() < 355) and (ball.ycor() < paddle_b.ycor() + 50 and (ball.ycor() > paddle_b.ycor() - 50)):    # If the ball's x coordinate is within the paddles x coordinate, and in the same y coordinate as the paddle
        ball.setx(340)
        ball.dx *= -1.009
        ball.dy *= 1.009    # The ball collides with the paddle and rebounds at a slightly increased speed

    if (ball.xcor() < -340 and ball.xcor() > -355) and (ball.ycor() < paddle_a.ycor() + 50 and (ball.ycor() > paddle_a.ycor() - 50)):    # If the ball's x coordinate is within the paddles x coordinate, and in the same y coordinate as the paddle
        ball.setx(-340)
        ball.dx *= -1.009
        ball.dy *= 1.009   # The ball collides with the paddle and rebounds at a slightly increased speed

    if ball.dx > 4.99 and ball.dy > 4.99:
        ball.dx = 4.99
        ball.dy = 4.99    # This is a cap on the ball's max speed, so it is playable for the user and cannot move straight through the paddle.

    if ball.dx < -4.99 and ball.dy > 4.99:
        ball.dx = -4.99
        ball.dy = 4.99

    if paddle_a.ycor() < -250:
        paddle_a.goto(-350, -250)    # These 4 statements mean that the paddles cannot move outside of the viewing window, by being teleported back into the window when it moves out.

    if paddle_a.ycor() > 250:
        paddle_a.goto(-350, 250)

    if paddle_b.ycor() < -250:
        paddle_b.goto(350, -250)

    if paddle_b.ycor() > 250:
        paddle_b.goto(350, 250)




