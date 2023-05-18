import arcade
class PartDrawing:
    def __init__(self, window, positions):
        self.window = window
        self.size = 30
        self.parts = positions
        self.x = None
        self.y = None
        self.color = None

    def draw_part(self, piece):
        for i in self.parts:
            self.color = arcade.color.WHITE if piece == "w" else arcade.color.GRAY
            self.x = i[0] * 70 + 35
            self.y = i[1] * 70 + 35
            arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

    def select(self, piece):
        self.color = (0, 255, 0)
        self.x = piece.position_x * 70 + 35
        self.y = piece.position_y * 70 + 35
        arcade.draw_circle_outline(self.x, self.y, self.size, self.color)
