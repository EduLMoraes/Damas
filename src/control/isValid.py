from src.control import rules, moves

class IsValid:
    def __init__(self, board):
        self.board = board
        self.rule = rules.Rules(board)
    
    def position(self, position, name):
        self.x = position[0]
        self.y = position[1]
        self.name = name
        
        self.move = moves.Move(self.board)
        self.move.select([self.x, self.y], self.board[self.x][self.y])
            
        print(">> isValid: Peça selecionada:", name, position)
    
    def new_position(self, new_position):
        self.new_x = new_position[0]
        self.new_y = new_position[1]

        if self.name == "w":
            if self.new_x == self.x + 1 and self.new_y == self.y + 1:
                self.move.new_position([self.new_x, self.new_y])
                
                print(">> isValid: Movimento válido.")
    
                return self.move.move()
            elif self.new_x == self.x - 1 and self.new_y == self.y + 1:
                self.move.new_position([self.new_x, self.new_y])

                print(">> isValid: Movimento válido.")
                return self.move.move()
            else:
                print(">> isValid: Movimento inválido.")
                return self.board
            
        else:
            if self.new_x == self.x + 1 and self.new_y == self.y - 1:
                self.move.new_position([self.new_x, self.new_y])

                print(">> isValid: Movimento válido.")
                return self.move.move()
            elif self.new_x == self.x - 1 and self.new_y == self.y - 1:
                self.move.new_position([self.new_x, self.new_y])

                print(">> isValid: Movimento válido.")
                return self.move.move()
            else:
                print(">> isValid: Movimento inválido.")
                return self.board
            
    def is_jump(self, new_position, piece):
        if (self.name == piece or new_position[0]+1 > 7 or new_position[0]-1 < 0
            or new_position[1]+1 > 7 or new_position[1]-1 < 0):

            print(">> isValid: Movimento inválido.")
            return self.board
        
        if new_position[0] > self.x and new_position[1] > self.y:
            self.new_x = new_position[0]+1
            self.new_y = new_position[1]+1
        
        elif new_position[0] < self.x and new_position[1] > self.y:
            self.new_x = new_position[0]-1
            self.new_y = new_position[1]+1
        
        elif new_position[0] < self.x and new_position[1] < self.y:
            self.new_x = new_position[0]-1
            self.new_y = new_position[1]-1

        else:
            self.new_x = new_position[0]+1
            self.new_y = new_position[1]-1

        if self.board[self.new_x][self.new_y] == "none":
            self.board = self.rule.eat(new_position)
            self.move.new_position([self.new_x, self.new_y])

            print(">> isValid: Peça comida.")
            return self.move.move()
        
        else:
            print(">> isValid: Peça não pode ser comida.")
            return self.board
        
        