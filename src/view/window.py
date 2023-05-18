import arcade
from src.drawns import boardDrawing, pieceDrawing
from src.control import isValid

class Game(arcade.Window):
    def __init__(self, board):
        self.board = board
        self.click = True

        super().__init__(560, 560, "Eduardo Moraes - Damas")
        arcade.set_background_color((255, 255, 255))

    def on_draw(self):
        w_position = []
        b_position = []

        for x in range(8):
            for y in range(8):
                if self.board[x][y] == "w":
                    w_position.append([x, y])
                elif self.board[x][y] == "b":
                    b_position.append([x, y])

        self.clear()
        arcade.start_render()

        plane = boardDrawing.BoardDrawing(self)
        plane.draw_board()

        piece = pieceDrawing.PartDrawing(self, w_position)
        piece.draw_part("w")

        piece = pieceDrawing.PartDrawing(self, b_position)
        piece.draw_part("b")

    def on_mouse_press(self, x, y, button, modifiers):
        x = int(x / 70)
        y = int(y / 70)
        
        if not (x+y) % 2 == 0:
            return False

        if self.board[x][y] != "none" and self.click == True:
            self.isValid = isValid.IsValid(self.board)
            self.isValid.position([x, y], self.board[x][y])

            self.click = False

        elif self.click == False and self.board[x][y] == "none":
            self.board = self.isValid.new_position([x, y])
            self.click = True
        
        elif self.click == False and self.board[x][y] != "none":
            self.board = self.isValid.is_jump([x, y], self.board[x][y])
            self.click = True

