import pandas as pd
from src.control import rules, moves, register
from qlearning import test

class IsValid:
    def __init__(self, board):
        self.board = board
        self.rule = rules.Rules(board)
        
    def position(self, position, name):
        self.x = position[0]
        self.y = position[1]
        self.name = name
        
        if not self.rule.turn(name):
            print(">> isValid: Não é seu turno ainda.")
            return False

        self.move = moves.Move(self.board)
        self.move.select([self.x, self.y], self.board[self.x][self.y])
        
        print(">>>>>>>>>>>>>>>>>>>>>> New Play >>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(">> isValid: Peça selecionada:", name, position)
        return True
    
    def new_position(self, new_position):
        self.new_x = new_position[0]
        self.new_y = new_position[1]

        if self.name == "w":
            for i in [-1, 1]:
                if self.new_x == self.x + i and self.new_y == self.y + 1:
                    print(">> isValid: Movimento válido.")

                    for i in range(0, 8):
                        if self.new_x == i and self.new_y == 7:
                            self.board[self.x][self.y] = "W"
                            self.move = moves.Move(self.board)
                            self.move.select([self.x, self.y], self.board[self.x][self.y])
                            print(">> isValid: w se tornou Dama")

                    self.move.new_position([self.new_x, self.new_y])
                    self.board = self.move.move()
                    self.compare()
                    test()
                    
                    
                    return self.board
            
        elif self.name == "b":
            for i in [-1, 1]:
                if self.new_x == self.x + i and self.new_y == self.y - 1:
                    print(">> isValid: Movimento válido.")

                    for i in range(0, 8):
                        if self.new_x == i and self.new_y == 0:
                            self.board[self.x][self.y] = "B"
                            self.move = moves.Move(self.board)
                            self.move.select([self.x, self.y], self.board[self.x][self.y])
                            print(">> isValid: b se tornou Dama")

                    self.move.new_position([self.new_x, self.new_y])
                    self.board = self.move.move()
                    self.compare()
                    test()
                    
                    
                    return self.board
                
        elif self.name == "W":
            for i in range(0, 8):
                for j in range(0, 8):
                    if (self.new_x == i and self.new_y == j and
                         (i != self.x and j != self.y) and (abs(self.x - i) == abs(self.y - j))):
                        
                        print(">> isValid: Movimento válido.")
                        self.move.new_position([self.new_x, self.new_y])
                        self.board = self.move.move()
                        self.compare()
                        test()
                        

                        return self.board
                
        elif self.name == "B":
            for i in range(0, 8):
                for j in range(0, 8):
                    print(">> isValid: Testando posição:", [i, j])
                    if (self.new_x == i and self.new_y == j and
                         (i != self.x and j != self.y) and (abs(self.x - i) == abs(self.y - j))):
                        
                        print(">> isValid: Movimento válido.")
                        self.move.new_position([self.new_x, self.new_y])
                        self.board = self.move.move()
                        self.compare()
                        test()
                        

                        return self.board


        if self.name.lower() == "w":
            self.rule.turn("b") 
        else:
            self.rule.turn("w")    

        print(">> isValid: Movimento inválido, tente novamente.")
        return self.board
            
    def is_jump(self, new_position, piece):
        if (self.name.upper() == piece.upper() or new_position[0]+1 > 7 or new_position[0]-1 < 0
            or new_position[1]+1 > 7 or new_position[1]-1 < 0):

            if self.name.lower() == "w":
                self.rule.turn("b") 
            else:
                self.rule.turn("w")

            print(">> isValid: Movimento inválido, tente novamente.")
            return self.board
        
        if new_position[0] > self.x and new_position[1] > self.y:
            self.new_x = new_position[0]+1
            self.new_y = new_position[1]+1
            duble_x = new_position[0]-1
            duble_y = new_position[1]-1
        
        elif new_position[0] < self.x and new_position[1] > self.y:
            self.new_x = new_position[0]-1
            self.new_y = new_position[1]+1
            duble_x = new_position[0]+1
            duble_y = new_position[1]-1
        
        elif new_position[0] < self.x and new_position[1] < self.y:
            self.new_x = new_position[0]-1
            self.new_y = new_position[1]-1
            duble_x = new_position[0]+1
            duble_y = new_position[1]+1

        else:
            self.new_x = new_position[0]+1
            self.new_y = new_position[1]-1
            duble_x = new_position[0]-1
            duble_y = new_position[1]+1

        if self.name == "b" or self.name == "w":
            for i in [1, -1]:
                for j in [1, -1]:
                    if self.board[self.new_x][self.new_y] == "none" and new_position[0] == self.x + i and new_position[1] == self.y + j:
                            self.board = self.rule.eat(new_position)
                            self.rule.turn(self.name, [self.new_x, self.new_y])

                            for k in range(0, 7):
                                if self.name == "w" and not self.rule.is_combo([self.new_x, self.new_y]):
                                    if self.new_x == k and self.new_y == 7:
                                        self.board[self.x][self.y] = self.board[self.x][self.y].upper()
                                        self.move = moves.Move(self.board)
                                        self.move.select([self.x, self.y], self.board[self.x][self.y])
                                
                                elif self.name == "b" and not self.rule.is_combo([self.new_x, self.new_y]):
                                    if self.new_x == k and self.new_y == 0:
                                        self.board[self.x][self.y] = self.board[self.x][self.y].upper()
                                        self.move = moves.Move(self.board)
                                        self.move.select([self.x, self.y], self.board[self.x][self.y])

                            self.move.new_position([self.new_x, self.new_y])
                            self.board = self.move.move()
                            self.compare()
                            test()
                            

                            print(">> isValid: Peça comida.")
                            return self.board
            else:
                if self.name.lower() == "w":
                    self.rule.turn("b") 
                else:
                    self.rule.turn("w")    

                print(">> isValid: Peça não pode ser comida, tente novamente.")
                return self.board

        elif self.name == "B" or self.name == "W":
            if self.board[self.new_x][self.new_y] == "none" and self.board[duble_x][duble_y].lower() != piece.lower():
                self.board = self.rule.eat(new_position)
                self.rule.turn(self.name, [self.new_x, self.new_y])
                self.move.new_position([self.new_x, self.new_y])
                self.board = self.move.move()
                self.compare()
                test()
                

                print(">> isValid: Peça comida.")
                return self.board
            
            else:
                if self.name.lower() == "w":
                    self.rule.turn("b") 
                else:
                    self.rule.turn("w")    

                print(">> isValid: Peça não pode ser comida, tente novamente.")
                return self.board
    
    def compare(self):
        table = pd.read_csv("game.csv")
        old_board = table.values

        for x in range(8):
            for y in range(8):
                if old_board[x][y] != self.board[x][y] and self.board[x][y] != "none":
                    print(">> isValid: Alteração detectada.")

                    scoreboard = self.rule.scoreboard()
                    combo = self.rule.is_combo([self.new_x, self.new_y])
                    
                    register.Register(f'{self.board[self.new_x][self.new_y]}', f'{(self.x, self.y)}', f'{(self.new_x, self.new_y)}', f'{(scoreboard)}', f'{combo}', f'{self.board}')

        print(">> isValid: comparado")
    
        