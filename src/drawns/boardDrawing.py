import arcade
class BoardDrawing:
    def __init__(self, window):
        self.window = window
        self.width = 8
        self.height = 8
        self.square_size = 70

    def draw_board(self):

        for i in range(self.width):
            for j in range(self.height):
                x = (i + 0.5) * self.square_size
                y = (j + 0.5) * self.square_size
                color = arcade.color.BLACK if (i + j) % 2 == 0 else arcade.color.WHITE
                arcade.draw_rectangle_filled(x, y, self.square_size, self.square_size, color)
