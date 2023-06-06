import pandas as pd
def save(board):
    print(">> Save: salvamento automatico...")
    pd.DataFrame(board).to_csv("./game.csv", index = False)
    print(">> Save: salvalvamento automatico completo.")