import pandas as pd
import os, numpy

class Recuperate:
    def __init__(self):
        if os.path.exists("./src/IA/memory/history.csv"):
            self.history = pd.read_csv('./src/IA/memory/history.csv')
        
    def game(self):
        matrix = self.history['matrix']
        last_row = len(matrix) - 1

        print(">> register: Jogo recuperado.")

        board = eval(matrix[last_row])
        print(board)

    def turn(self):
        turn = self.history['team']
        last = len(turn) - 1

        print(">> register: Jogo recuperado.")

        turn = turn[last]

        print(turn)

    def scoreboard(self):
        score = self.history['scoreboard']
        last = len(score) - 1

        print(">> register: Jogo recuperado.")

        score = score[last]

        print(score)



Recuperate().scoreboard()