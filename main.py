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
screen.colormode(255)

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

# Looping over to keep track of ball actions and score
while True:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    # Checking if the ball hit a tile
    hit_tile, tile_hit = ball.hit_tile(tiles)
    if hit_tile:
        ball.tile_bounce()
        for row in tiles.tiles:
            if tile_hit in row:
                row.remove(tile_hit)
                tile_hit.goto(1000, 1000)  # Hide the tile
                break
        score += 10
        paddle.reduce_width(0.5)    # Reduce paddle width with increase in score
        paddle.clear()
        t1.clear()

    # Checking if the ball hit the walls
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()
    elif ball.ycor() > 265:
        ball.bounce_y()
    elif ball.ycor() < -265:
        ball.goto(0, 0)
        ball.setheading(135)
        lives -= 1
        t2.clear()
        time.sleep(1)
        ball.movespeed = 0.1

    ball.paddle_bounce(paddle, paddle.length*10)

    if lives == 0:  # Checks if game is over
        tur = Turtle()
        tur.goto(0, 0)
        tur.color('white')
        tur.hideturtle()
        tur.write("GAME OVER!", move=False, align="center", font=("Courier", 50))
        screen.exitonclick()

    if score == 480:    # Checks if player has won
        tur = Turtle()
        tur.goto(0, 0)
        tur.color('white')
        tur.hideturtle()
        tur.write("YOU WON!", move=False, align="center", font=("Courier", 50))
        screen.exitonclick()

    # Score
    t1.goto(x=-100, y=250)
    t1.color("white")
    t1.hideturtle()
    t1.write(f"Score: {score}", move=False, align='center', font=('arial', 30, 'normal'))

    # Lives
    t2.goto(x=100, y=250)
    t2.color("white")
    t2.hideturtle()
    t2.write(f"Lives: {lives}", move=False, align='center', font=('arial', 30, 'normal'))
