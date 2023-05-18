import arcade

from src.view import window
from src.factory import board

class Game:
    def __init__(self):
        self.board = board.Board().matrix
        self.w_init_positions = [[0, 0], [2, 0], [4, 0], [6, 0], [1, 1],  [3, 1], [5, 1], [7, 1]]
        self.b_init_positions = [[0, 6], [2, 6], [4, 6], [6, 6], [1, 7],  [3, 7], [5, 7], [7, 7]]

        for i in self.w_init_positions:
            self.board[i[0]][i[1]] = "w"
        for i in self.b_init_positions:
            self.board[i[0]][i[1]] = "b"

        self.window = window
        self.window.Game(self.board)


def game():
    Game()
    arcade.run()

if __name__ == "__main__":
    game()
