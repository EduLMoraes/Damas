import arcade
class PartDrawing:
    def __init__(self, window):
        self.window = window
        self.size = 30
        self.x = None
        self.y = None
        self.color = None

    def draw_part(self, pieces):

        for i in pieces:
            if i[2] == "w":
                self.color = arcade.color.WHITE
            elif i[2] == "b":
                self.color = arcade.color.GRAY
            elif i[2] == "W":
                self.color = arcade.color.LIGHT_GOLDENROD_YELLOW
            else:
                self.color = arcade.color.DARK_SLATE_GRAY

            self.x = i[0] * 70 + 35
            self.y = i[1] * 70 + 35
            arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

    def select(self, piece):
        self.color = (0, 255, 0)
        self.x = piece.position_x * 70 + 35
        self.y = piece.position_y * 70 + 35
        arcade.draw_circle_outline(self.x, self.y, self.size, self.color)
