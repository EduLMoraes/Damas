import numpy as np
import pandas as pd
import os
from src.control.register import Recuperate

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

def test():
    if os.path.exists("./game.csv"):
        matriz = pd.read_csv('./game.csv').values
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

    for state in range(num_states):
        action = agent.choose_action(state)

        if state < num_states - 1:
            next_state = state + 1
        else:
            next_state = 0

        if os.path.exists("./game.csv"):
            for i in positions:
                if action == 0 and (i[0]+1 < 8 and i[1]+1 < 8):
                    x = i[0]+1
                    y = i[1]+1
                    if (matriz[x][y].lower() == 'none'):
                        reward = 0.5
                    else:
                        reward = 0

                elif action == 1 and (i[0]+1 < 8 and i[1]-1 > 0):
                    x = i[0]+1
                    y = i[1]-1
                    if (matriz[x][y].lower() == 'none'):
                        reward = 0.5
                    else:
                        reward = 0

                elif action == 2 and (i[0]-1 > 0 and i[1]-1 > 0):
                    x = i[0]-1
                    y = i[1]-1
                    if (matriz[x][y].lower() == 'none'):
                        reward = 0.5
                    else:
                        reward = 0

                elif action == 3 and (i[0]-1 > 0 and i[1]+1 < 8):
                    x = i[0]-1
                    y = i[1]+1
                    if (matriz[x][y].lower() == 'none'):
                        reward = 0.5
                    else:
                        reward = 0
        else:
            reward = 0.5

        agent.update_q_table(state, action, reward, next_state)
        print(agent.q_table)
    
test()