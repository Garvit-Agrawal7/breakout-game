from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from tiles import Tiles
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

# Initializing the paddle and tiles
paddle = Paddle((0, -250))
tiles = Tiles()

# Initializing the ball
ball = Ball()
t1 = Turtle()
t2 = Turtle()

# Listening to keypress for paddle movement
screen.listen()
screen.onkeypress(paddle.left, "Left")
screen.onkeypress(paddle.right, "Right")

# Keeping track of the score
score = 0
lives = 3

while True:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    hit_tile, tile_hit = ball.hit_tile(tiles)
    if hit_tile:
        ball.tile_bounce()
        tile_hit.goto(1000, 1000)
        score += 10
        t1.clear()

    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()
    elif ball.ycor() > 270:
        ball.bounce_y()

    ball.paddle_bounce(paddle)

    if ball.ycor() < -265:
        ball.goto(0, 0)
        ball.setheading(135)
        lives -= 1
        t2.clear()
        ball.movespeed = 0.1

    t1.goto(x=-100, y=250)
    t1.color("white")
    t1.hideturtle()
    t1.write(f"Score: {score}", move=False, align='center', font=('arial', 30, 'normal'))

    t2.goto(x=100, y=250)
    t2.color("white")
    t2.hideturtle()
    t2.write(f"Lives: {lives}", move=False, align='center', font=('arial', 30, 'normal'))
