from src.control.register import Recuperate
from qlearning import test
class Rules:
    rec = Recuperate()
    points_w = int(rec.scoreboard()[1]) if rec.scoreboard()[0] else 0
    points_b = int(rec.scoreboard()[4]) if rec.scoreboard()[0] else 0
    name = rec.turn() if rec.turn() else 'b'
    round = 1

    def __new__(cls, board):
        if not hasattr(cls, "instance"):
            cls.instance = super(Rules, cls).__new__(cls)
        return cls.instance

    def __init__(self, board):
        self.board = board

    def scoreboard(self):
        return [self.points_w, self.points_b]

    def eat(self, position):
        x = position[0]
        y = position[1]

        if self.board[x][y].lower() == "w":
            self.points_b += 1
            self.name = "w"
        else:
            self.points_w += 1
            self.name = "b"

        print(f">> rules: Placar: P{self.points_b} | {self.points_w}B")

        if self.points_w == 8:
            print(">> rules: Vitória das peças brancas.")
            
        elif self.points_b == 8:
            print(">> rules: Vitória das peças pretas.")

        self.board[x][y] = "none"
        return self.board
    
    def is_combo(self, position):
        if position == [None, None]:
            return False
        
        x = position[0]
        y = position[1]

        for i in range(max(1, x - 1), min(8, x + 2)):
            for j in range(max(1, y - 1), min(8, y + 2)):
                if (i + j) % 2 == 0:
                    if self.board[i][j] == self.name:
                        if not (i+1 > 7 or i-1 < 0 or j+1 > 7 or j-1 < 0):

                            if i > x and j > y:
                                if self.board[i + 1][j + 1] == "none":
                                    return True
                                
                            elif i > x and j < y:
                                if self.board[i + 1][j - 1] == "none":
                                    return True
                                
                            elif i < x and j > y:
                                if self.board[i - 1][j + 1] == "none":
                                    return True
                                
                            elif i < x and j < y:
                                if self.board[i - 1][j - 1] == "none":
                                    return True
                                
        return False
    
    def turn(self, name, position = [None, None]):
        if name.lower() != 'w':
            return False

        if not self.is_combo(position):
            print(">> rules: Não há combo!")
            self.name = name
            if self.name.lower() == "b":
                print(">> rule: teste: ", test(self.board))
                self.name = "b"
        else:
            print(">> rule: Há combo!")


        print(f">> rules: turno {self.name}")
        return True
    
    
    