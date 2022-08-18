# Pong Remastered Project
# By James Bernau
# Pt. 2

import os  # This allows my code to communicate with a folder
import turtle  # Turtle is the main feature of the program, it draws the ball and paddles and allows them to move.
import time

wn = turtle.Screen()    # Defining the name, colour, and shape of the game window
wn.title("Bouncy Funtime")
wn.bgcolor("black")
wn.setup(width=800, height=600)    # This defines the window size and allows me to position turtles in various places
wn.tracer(0)

# Points
points_a = 0    # These variables keep track of each time a player wins 7 games, for a total of one point
points_b = 0

# Score
score_a = 0    # These variables keep track of each game one by a player, to earn one score
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # Paddle a is a turtle - it can move and be whatever shape or colour is chosen
paddle_a.speed(0)   # The paddle does not move from it's fixed position
paddle_a.shape("square")    # Shape is that of the classic paddle
paddle_a.color("#9F9F9F")   # Colour is a light grey, a more modern feel than the classic white
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    # Stretching width and length makes the paddle into a rectangle, which is the intended shape
paddle_a.penup()    # When the paddle moves, it will not leave a trail
paddle_a.goto(-350, 0)  # This is where the paddle will be positioned on the window, at the far left of the screen.

# Paddle B - Same as paddle a, just positioned in the far right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#9F9F9F")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")    # Ball shape has been updated to a circle - a modern improvement
ball.color("#9F9F9F")   # Ball colour is a light grey, a more modern feel than the classic white
ball.penup()    # Ball will not leave a trail
ball.goto(0, 0)    # Ball starts in the centre of the screen
ball.dx = 3    # ball.dx and ball.dy define the speed at which the ball moves
ball.dy = -3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("#9F9F9F")
pen.penup()    # Pen has no trail
pen.hideturtle()    # Pen cannot be seen
pen.goto(0, 260)    # Pen moves to these coordinates
pen.write("A POINTS - 0 - 0 - B POINTS", align="center", font=("Courier", 24, "normal"))
pen.goto(0, 220)
pen.write("A SCORE - 0 - 0 - B SCORE", align="center", font=("Courier", 24, "normal"))  # This defines what is written by the pen, the font and size


# Centre line
centre_line1 = turtle.Turtle()
centre_line1.speed(0)
centre_line1.shape("square")
centre_line1.color("#9F9F9F")   # The centre line is a turtle that adds to the aesthetic of the game
centre_line1.shapesize(stretch_wid=3, stretch_len=0.2)  # Stretched into a rectangle
centre_line1.penup()    # The centre line does not leave a trail
centre_line1.goto(0, -250)  # Moves the centre line to its desired location

centre_line2 = turtle.Turtle()  # Repeated centre lines to create a dotted line
centre_line2.speed(0)
centre_line2.shape("square")
centre_line2.color("#9F9F9F")
centre_line2.shapesize(stretch_wid=3, stretch_len=0.2)
centre_line2.penup()
centre_line2.goto(0, -150)

centre_line3 = turtle.Turtle()
centre_line3.speed(0)
centre_line3.shape("square")
centre_line3.color("#9F9F9F")
centre_line3.shapesize(stretch_wid=3, stretch_len=0.2)
centre_line3.penup()
centre_line3.goto(0, -50)

centre_line4 = turtle.Turtle()
centre_line4.speed(0)
centre_line4.shape("square")
centre_line4.color("#9F9F9F")
centre_line4.shapesize(stretch_wid=3, stretch_len=0.2)
centre_line4.penup()
centre_line4.goto(0, 50)

centre_line5 = turtle.Turtle()
centre_line5.speed(0)
centre_line5.shape("square")
centre_line5.color("#9F9F9F")
centre_line5.shapesize(stretch_wid=2.5, stretch_len=0.2)
centre_line5.penup()
centre_line5.goto(0, 150)

welcome_message = turtle.Turtle()   # This message will display when the program begins, and disappear after 5 seconds.
welcome_message.speed(0)
welcome_message.color("#9F9F9F")    # Colour is the same as the colours used throughout the project
welcome_message.penup()
welcome_message.hideturtle()
welcome_message.goto(0, 0)  # The turtle moves to the centre of the screen, and the text welcomes the players and tells them the controls.
welcome_message.write("Welcome to modern Pong! \n Player 1 uses w and s keys \n Player 2 uses up and down arrow keys.", align="center", font=("Courier", 20, "normal"))
welcome_message.goto(0, -200)   # This message helps protect from legal implications
welcome_message.write("This game is in no way affiliated with Atari Interactive Inc.", align="center", font=("Impact", 10, "normal"))
time.sleep(5)   # This delays the code, allowing the message to be displayed for five seconds.
welcome_message.clear()    # This clears the message and allows the game to run as usual.



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
        os.system("afplay pong.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    # If the ball collides with the bottom border, it will 'bounce' off
        os.system("afplay pong.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)    # The ball resets to kick off position when a point is scored
        if ball.dx >= 3:
            ball.dx = -3
        if ball.dy >= 3:
            ball.dy = -3
        if ball.dy <= -3:
            ball.dy = 3    # These if statements will send the ball in the opposite direction off kickoff
        score_a += 1    # gives one score to the player who scored
        pen.clear()
        pen.goto(0, 260)    # This updates the points and score for each player
        pen.write("A POINTS - {} - {} - B POINTS".format(points_a, points_b), align="center", font=("Courier", 30, "normal"))
        pen.goto(0, 220)
        pen.write("A SCORE - {} - {} - B SCORE".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)    # The ball resets to kick off position when a point is scored
        if ball.dx <= -3:
            ball.dx = 3
        if ball.dy >= 3:
            ball.dy = -3
        if ball.dy <= -3:
            ball.dy = 3    # These if statements will send the ball in the opposite direction off kickoff
        score_b += 1    # gives one score to the player who scored
        pen.clear()
        pen.goto(0, 260)    # This updates the points and score for each player
        pen.write("A POINTS - {} - {} - B POINTS".format(points_a, points_b), align="center", font=("Courier", 30, "normal"))
        pen.goto(0, 220)
        pen.write("A SCORE - {} - {} - B SCORE".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions, Ball speed, Collisions sfx
    if (ball.xcor() > 340 and ball.xcor() < 355) and (ball.ycor() < paddle_b.ycor() + 50 and (ball.ycor() > paddle_b.ycor() - 50)):
        # This checks for ball position and paddle position, determining if they are in the same position, and therefore colliding
        ball.setx(340)    # Sets the balls position in front of the paddle that it collided with
        ball.dx *= -1.009    # Rebounds the ball back off the paddle, and increasing horizontal speed
        ball.dy *= 1.009    # Increases vertical speed
        os.system("afplay pong.wav&")    # This plays the bounce noise in my python folder. The '&' allows the game to continue running while the sound plays.

    if (ball.xcor() < -340 and ball.xcor() > -355) and (ball.ycor() < paddle_a.ycor() + 50 and (ball.ycor() > paddle_a.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1.009
        ball.dy *= 1.009
        os.system("afplay pong.wav&")

    # If the ball is travelling faster than 5 pixels per movement, it can travel through the paddles. This keeps the ball speed just below this

    if ball.dx > 4.99 and ball.dy > 4.99:
        ball.dx = 4.99
        ball.dy = 4.99

    if ball.dx < -4.99 and ball.dy > 4.99:
        ball.dx = -4.99
        ball.dy = 4.99  # This monitors ball speed in the opposite direction

    # Prevents paddles form existing the viewing window by establishing barriers

    if paddle_a.ycor() < -250:
        paddle_a.goto(-350, -250)

    if paddle_a.ycor() > 250:
        paddle_a.goto(-350, 250)

    if paddle_b.ycor() < -250:
        paddle_b.goto(350, -250)

    if paddle_b.ycor() > 250:
        paddle_b.goto(350, 250)

    # Colour changes and sounds according to score

    if score_a == 0:
        paddle_a.color("#9F9F9F")   # The colours were chosen according to aesthetic preferences and the progression of the rainbow
    if score_a == 1:
        paddle_a.color("#FF0000")
    if score_a == 2:
        paddle_a.color("#FF5100")
    if score_a == 3:
        paddle_a.color("#FFFF00")
    if score_a == 4:
        paddle_a.color("#2AFF00")
    if score_a == 5:
        paddle_a.color("#00ECFF")
    if score_a == 6:
        paddle_a.color("#8B00FF")
    if score_a == 7:
        paddle_a.color("#9F9F9F")
        os.system("afplay win.wav&")    # Fanfare plays when a players wins a point (seven score)
        score_a = 0
        score_b = 0
        points_a += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write("A POINTS - {} - {} - B POINTS".format(points_a, points_b), align="center", font=("Courier", 30, "normal"))
        pen.goto(0, 220)
        pen.write("A SCORE - {} - {} - B SCORE".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # When a player wins a point, the scores are reset to zero and score display is updated.

    if score_b == 0:
        paddle_b.color("#9F9F9F")
    if score_b == 1:
        paddle_b.color("#FF0000")
    if score_b == 2:
        paddle_b.color("#FF5100")
    if score_b == 3:
        paddle_b.color("#FFFF00")
    if score_b == 4:
        paddle_b.color("#2AFF00")
    if score_b == 5:
        paddle_b.color("#00ECFF")
    if score_b == 6:
        paddle_b.color("#8B00FF")
    if score_b == 7:
        paddle_b.color("#9F9F9F")
        os.system("afplay win.wav&")
        score_b = 0
        score_a = 0
        points_b += 1
        pen.clear()
        pen.goto(0, 260)
        pen.write("A POINTS - {} - {} - B POINTS".format(points_a, points_b), align="center", font=("Courier", 30, "normal"))
        pen.goto(0, 220)
        pen.write("A SCORE - {} - {} - B SCORE".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Above is the same for the other player
