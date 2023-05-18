class Rules:
    points_b = None
    points_w = None
    def __init__(self, board):
        self.board = board

    def eat(self, position):
        x = position[0]
        y = position[1]

        if self.board[x][y] == "w":
            self.points_b += 1
            
        else:
            self.points_w += 1

        if self.points_w == 8:
            print(">> rules: Vitória das peças brancas.")

        elif self.points_b == 8:
            print(">> rules: Vitória das peças pretas.")

        self.board[x][y] = "none"
        return self.board