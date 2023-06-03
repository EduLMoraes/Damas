import csv
import os
import pandas as pd

class Recuperate:
    def __init__(self):
        if os.path.exists("./src/IA/memory/history.csv") and os.path.exists("./game.csv"):
            self.history = pd.read_csv('./src/IA/memory/history.csv')
            self.has_history = True
        else:
            self.has_history = False
    
    def matrix(self):

        list_matrix = []
        list_clean = []
        print(self.history['matrix'])
        for i in self.history['matrix']:
            list_matrix.append(i)

        for i in list_matrix:
            if len(list_clean) == 0:
                list_clean.append(i)
            else:
                for j in range(len(list_clean)):
                    if list_matrix[j] != list_clean[j]:
                        list_clean.append(i)


        print("tamanho lista:", len(list_clean))
        print("tamanho history:", len(self.history['matrix']))

        return self.history['matrix']

    def game(self):
        if os.path.exists("./game.csv"):
            print(">> register: Jogo recuperado.")

            board = pd.read_csv("./game.csv")
            
            return board.values
        return False

    def turn(self):
        if self.has_history:
            turn = self.history['team']
            last = len(turn) - 1
            print(">> register: Turno recuperado.")

            turn = turn[last]

            return str(turn)
        else:
            return "b"
    
    def scoreboard(self):
        if self.has_history:
            score = self.history['scoreboard']
            last = len(score) - 1

            print(">> register: Pontuação recuperada.")

            score = score[last]

            return score
        return ([0, 0])

def first_round():
    with open('./src/IA/memory/round.txt', 'w') as file:
        file.write(str(1))

def round():
    if not os.path.exists('./src/IA/memory/round.txt'):
        first_round()

    with open("./src/IA/memory/round.txt", 'r') as file:
        rounds = file.read()
        return int(rounds)
    
def new_round(rounds = round()):
    with open("./src/IA/memory/round.txt", 'w') as file:
        file.write(str(rounds+1))

    if os.path.exists("./game.csv"):
        os.remove("./game.csv")

class Register:
    def __init__(self, *info):
        self.playeds = [
            {
                'rounds': f'{round()}',
                'team': info[0],
                'choose': info[1],
                'move': info[2],
                'scoreboard': info[3],
                'combo': info[4],
                'matrix': info[5]
            }
        ]
        self.name = "history.csv"
        self.dir = "./src/IA/memory/"

        if os.path.exists(self.dir+self.name):
            self.read_table()
            self.write_table()
        else:
            self.history = []
            self.write_table()

    def write_table(self):
        with open((self.dir + self.name), 'w', newline="") as file_csv:
            slots = ['rounds', 'team', 'choose', 'move', 'scoreboard', 'combo', 'matrix']
            writer = csv.DictWriter(file_csv, fieldnames=slots)

            writer.writeheader()

            if not self.exists():
                for row in self.playeds:
                    self.history.append(row)

            for played in self.history:
                writer.writerow(played)

    def read_table(self):

        self.history = []
        
        with open((self.dir + self.name), 'r') as file_csv:
            reader = csv.DictReader(file_csv)
            
            for row in reader:
                self.history.append(row)

    def exists(self):

        for row in self.history:
            if row['matrix'] == self.playeds[0]['matrix']:
                return True

        return False

