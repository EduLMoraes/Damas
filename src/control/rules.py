class Rules:
    points_b = 0
    points_w = 0
    name = "b"

    def __new__(cls, board):
        if not hasattr(cls, "instance"):
            cls.instance = super(Rules, cls).__new__(cls)
        return cls.instance

    def __init__(self, board):
        self.board = board

    def eat(self, position):
        x = position[0]
        y = position[1]

        if self.board[x][y] == "w":
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
            
                            if i > x and j > y and not (j + 1 > 7):
                                if self.board[i + 1][j + 1] == "none":
                                    return True
                                
                            elif i < x and j > y:
                                if self.board[i - 1][j + 1] == "none":
                                    return True
                                
                            elif i < x and j < y:
                                if self.board[i - 1][j - 1] == "none":
                                    return True
                                
                            elif i > x and j < y:
                                if self.board[i + 1][j - 1] == "none":
                                    return True
                
        return False
    
    def turn(self, name, position = [None, None]):
        if name.lower() == self.name.lower():
            return False
        
        print(">> rules: é combo?", self.is_combo(position))

        if not self.is_combo(position):
            self.name = name
        
        print(f">> rules: turno {self.name}")
        return True
    
    