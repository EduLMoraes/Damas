import arcade
from src.drawns import boardDrawing, pieceDrawing
from src.control import isValid

class GameWindow(arcade.Window):
    def __init__(self, board):
        self.board = board
        self.click = True

        super().__init__(560, 560, "Eduardo Moraes - Damas")
        arcade.set_background_color((255, 255, 255))

    def on_draw(self):

        self.clear()
        arcade.start_render()
        
        plane = boardDrawing.BoardDrawing(self)
        plane.draw_board()

        whites = []
        grays = []

        for x in range(8):
            for y in range(8):
                if self.board[x][y] != "none":
                    if self.board[x][y].lower() == "b":
                        grays.append(self.board[x][y])
                    else:
                        whites.append(self.board[x][y])
        
        if len(whites) < 1:
            arcade.draw_text("Vitória das pretas", 150, 250, arcade.color.RED_DEVIL, 30)
        elif len(grays) < 1:
            arcade.draw_text("Vitória das brancas", 150, 250, arcade.color.RED_DEVIL, 30)

 

        piece = pieceDrawing.PartDrawing(self)

        for x in range(8):
            for y in range(8):
                if self.board[x][y] == "w":
                    piece.draw_part([[x, y, "w"]])
                elif self.board[x][y] == "b":
                    piece.draw_part([[x, y, "b"]])
                elif self.board[x][y] == "W":
                    piece.draw_part([[x, y, "W"]])
                elif self.board[x][y] == "B":
                    piece.draw_part([[x, y, "B"]])

    def on_mouse_press(self, x, y, button, modifiers):
        x = int(x / 70)
        y = int(y / 70)
        
        if not (x+y) % 2 == 0:
            return False

        if self.board[x][y] != "none" and self.click == True:
            self.isValid = isValid.IsValid(self.board)
            position = self.isValid.position([x, y], self.board[x][y])

            if position:
                self.click = False
            else:
                self.click = True

        elif self.click == False and self.board[x][y] == "none":
            self.board = self.isValid.new_position([x, y])
            self.click = True
        
        elif self.click == False and self.board[x][y] != "none":
            self.board = self.isValid.is_jump([x, y], self.board[x][y])
            self.click = True

    def update_board(self):
        return self.board

