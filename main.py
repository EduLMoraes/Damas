import arcade
import os
from src.view import window
from src.factory import board
from src.control.save import save
from src.control.register import Recuperate

class Game:
    def __init__(self):
        if not os.path.exists("./game.csv"):
            self.board = board.Board().matrix
            self.w_init_positions = [[0, 0], [2, 0], [4, 0], [6, 0], [1, 1],  [3, 1], [5, 1], [7, 1]]
            self.b_init_positions = [[0, 6], [2, 6], [4, 6], [6, 6], [1, 7],  [3, 7], [5, 7], [7, 7]]

            for i in self.w_init_positions:
                self.board[i[0]][i[1]] = "w"
            for i in self.b_init_positions:
                self.board[i[0]][i[1]] = "b"
        else:
            self.board = Recuperate().game()

        save(self.board)
        self.window = window.GameWindow(self.board)

    def update_board(self):
        print(">> main: update")


def game():
    Game()
    arcade.run()


if __name__ == "__main__":
    game()