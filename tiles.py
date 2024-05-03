from turtle import Turtle


class Tiles:
    def __init__(self):
        # Tile location
        self.x_cors = [i for i in range(-345, 340, 97)]
        self.y_cors = [i for i in range(200, -0, -37)]

        self.colors = ['#f54952', '#AE2D68', '#660F56', '#280659', '#341671', '#422680']
        self.tiles = []
        for row in range(len(self.y_cors)):
            tiles = [Turtle() for _ in range(len(self.x_cors))]
            for tile in tiles:
                tile.color(self.colors[row])
                tile.shape('square')
                tile.penup()
                tile.shapesize(stretch_len=4.5, stretch_wid=1.5)
                tile.goto(x=self.x_cors[tiles.index(tile)], y=self.y_cors[row])
            self.tiles.append(tiles)
