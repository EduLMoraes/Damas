import numpy as np
import pandas as pd
import os
from src.control.register import QTable
from src.control.moves import Move
from src.control.save import save

class QLearningAgent:
    def __new__(cls, num_states, num_actions, learning_rate, discount_factor):
        if not hasattr(cls,'instance'):
            cls.instance = super(QLearningAgent, cls).__new__(cls)
            
        return cls.instance

    def __init__(self, num_states, num_actions, learning_rate, discount_factor):
            
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

        if QTable().read():
            self.q_table = QTable().qtable.values
        else:
            self.q_table = np.zeros((num_states, num_actions))

  
    def choose_action(self, state):
        q_values = self.q_table[state]
        action = np.argmax(q_values)
        return action

    def update_q_table(self, state, action, reward, next_state):
        current_q = self.q_table[state, action]
        max_next_q = np.max(self.q_table[next_state])
        td_target = reward + self.discount_factor * max_next_q
        td_error = td_target - current_q
        self.q_table[state, action] += self.learning_rate * td_error


def play(positions, new_positions, matriz):
    iv = Move(matriz)
    iv.select(positions, "b")
    iv.new_position(new_positions)
    board = iv.move()
    print("qlearning: Jogada feita")
    return board

def is_combo(board, position, name):
        if position == [None, None]:
            return False
        
        x = position[0]
        y = position[1]

        for i in range(max(1, x - 1), min(8, x + 2)):
            for j in range(max(1, y - 1), min(8, y + 2)):
                if (i + j) % 2 == 0:
                    if board[i][j] == name:
                        if not (i+1 > 7 or i-1 < 0 or j+1 > 7 or j-1 < 0):

                            if i > x and j > y:
                                if board[i + 1][j + 1] == "none":
                                    return True
                                
                            elif i > x and j < y:
                                if board[i + 1][j - 1] == "none":
                                    return True
                                
                            elif i < x and j > y:
                                if board[i - 1][j + 1] == "none":
                                    return True
                                
                            elif i < x and j < y:
                                if board[i - 1][j - 1] == "none":
                                    return True
                                
        return False

def test(board):
    if os.path.exists("./game.csv"):
        matriz = board
        positions = []
        for x in range(8):
            for y in range(8):
                if matriz[x][y].lower() == 'b':
                    positions.append((x, y))

        num_states = len(positions)+1
    else:
        num_states = 9

    num_actions = 4
    learning_rate = 0.1
    discount_factor = 0.9

    agent = QLearningAgent(num_states, num_actions, learning_rate, discount_factor)

    played = False
    reward = 0
    for state in range(num_states):
        action = agent.choose_action(state)

        if state < num_states - 1:
            next_state = state + 1
        else:
            next_state = 0

        if not played:
            for i in positions:
                if action == 0:
                    if(i[0]+1 < 8 and i[1]+1 < 8):
                        x = i[0]+1
                        y = i[1]+1
                        if (matriz[x][y].lower() == 'none' and matriz[i[0]][i[1]] == "B"):
                            matriz = play([i[0], i[1]], [x, y], matriz)
                            reward = 0.5
                            played = True

                            break
                        
                        elif (matriz[x][y].lower() == 'w' and ((i[0]+2 < 8 and i[1]+2 < 8) and (matriz[x+1][y+1] == "none"))):
                            matriz = play([i[0], i[1]], [x+1, y+1], matriz)
                            matriz[x][y] = 'none'
                            reward = 0.8
                            
                            if not is_combo:
                                played = True
                            
                            break
                        
                        else:
                            reward = 0
                    else:
                        action += 1

                if action == 1:
                    if(i[0]+1 < 8 and i[1]-1 > 0):
                        x = i[0]+1
                        y = i[1]-1
                        if (matriz[x][y].lower() == 'none'):
                            matriz = play([i[0], i[1]], [x, y], matriz)
                            reward = 0.5
                            played = True

                            break
                        elif (matriz[x][y].lower() == 'w' and ((i[0]+2 < 8 and i[1]-2 < 8) and (matriz[x+1][y-1] == "none"))):
                            matriz = play([i[0], i[1]], [x+1, y-1], matriz)
                            matriz[x][y] = 'none'
                            reward = 0.8
                            
                            if not is_combo:
                                played = True
                            
                            break
                        
                        else:
                            reward = 0
                    else:
                        action += 1

                if action == 2:
                    if(i[0]-1 > 0 and i[1]-1 > 0):
                        x = i[0]-1
                        y = i[1]-1
                        if (matriz[x][y].lower() == 'none'):
                            matriz = play([i[0], i[1]], [x, y], matriz)
                            reward = 0.5
                            played = True

                            break
                        elif (matriz[x][y].lower() == 'w' and ((i[0]-2 < 8 and i[1]-2 < 8) and (matriz[x-1][y-1] == "none"))):
                            matriz = play([i[0], i[1]], [x-1, y-1], matriz)
                            matriz[x][y] = 'none'
                            reward = 0.8
                            
                            if not is_combo:
                                played = True
                            
                            break
                        
                        else:
                            reward = 0
                    else:
                        action += 1

                if action == 3:
                    if(i[0]-1 > 0 and i[1]+1 < 8):
                        x = i[0]-1
                        y = i[1]+1
                        if (matriz[x][y].lower() == 'none' and matriz[i[0]][i[1]] == "B"):
                            matriz = play([i[0], i[1]], [x, y], matriz)
                            reward = 0.5
                            played = True

                            break
                        elif (matriz[x][y].lower() == 'w' and ((i[0]-2 < 8 and i[1]+2 < 8) and (matriz[x-1][y+1] == "none"))):
                            matriz = play([i[0], i[1]], [x-1, y+1], matriz)
                            matriz[x][y] = 'none'
                            reward = 0.8
                            
                            if not is_combo:
                                played = True
                            
                            break
                        
                        else:
                            reward = 0
                    else:
                        action = 0

        else:
            reward = 0
            break

        for i in positions:
            if i[1] == 0:
                matriz[i[0]][i[1]] = 'B'
        agent.update_q_table(state, action, reward, next_state)
        print(agent.q_table)
    QTable().write(agent.q_table)
    return matriz