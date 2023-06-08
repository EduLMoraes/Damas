class Move:
    def __init__(self, board):
        self.board = board

    def select(self, piece, name):
        self.piece_change = name
        self.x = piece[0]
        self.y = piece[1]
        return True

    def new_position(self, position):
        self.new_x = position[0]
        self.new_y = position[1]
        return True

    def move(self):
        self.old_board = self.board
        self.board[self.x][self.y] = "none"
        self.board[self.new_x][self.new_y] = self.piece_change
        return self.board
    

