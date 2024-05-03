from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.color("blue")
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(coordinates)

    def right(self, **kwargs):
        """Paddle goes right"""
        x = self.xcor() + 20
        self.goto(x, self.ycor())

    def left(self, **kwargs):
        """Paddle goes left"""
        x = self.xcor() - 20
        self.goto(x, self.ycor())
