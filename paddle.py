from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.color("#ff6d00")
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.length = 25
        self.shapesize(stretch_len=self.length, stretch_wid=1)
        self.goto(coordinates)

    def right(self, **kwargs):
        """Paddle goes right"""
        x = self.xcor() + 20
        if self.xcor() > 380:   # Restricts paddle from going outside the right wall
            self.goto(x-40, self.ycor())
        else:
            self.goto(x, self.ycor())

    def left(self, **kwargs):
        """Paddle goes left"""
        x = self.xcor() - 20
        if self.xcor() < -380:  # Restricts paddle from going outside the left wall
            self.goto(x+40, self.ycor())
        else:
            self.goto(x, self.ycor())

    def reduce_width(self, reduction):
        self.length -= reduction
        self.shapesize(stretch_len=self.length, stretch_wid=1)
        return self.length
