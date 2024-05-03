from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, -100)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1
        self.direction = choice([1, -1])

    def move(self):
        """Moves the ball forward"""
        x = self.xcor() + self.xmove * self.direction
        y = self.ycor() + self.ymove
        self.goto(x=x, y=y)

    def bounce_x(self):
        """Bounce the ball on the x-axis"""
        self.xmove *= -1

    def bounce_y(self):
        """Bounce the ball on the y-axis"""
        self.ymove *= -1

    def paddle_bounce(self, paddle, length):
        """Paddle bounce the ball on the y-axis"""
        if self.distance(paddle) < length and self.ycor() < -220:
            self.ymove *= -1

    def hit_tile(self, tiles):
        """Check if the ball hits a tile"""
        for row in tiles.tiles:     # Iterates over the 2D list of tiles
            for tile in row:
                if self.distance(tile) < 35:
                    return True, tile
        return False, None

    def tile_bounce(self):
        self.ymove *= -1
        self.movespeed *= 0.9

