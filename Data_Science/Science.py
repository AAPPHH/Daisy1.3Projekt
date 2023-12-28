import pandas as pd
path = r"Data_Science/game_history.pkl"

df = pd.read_pickle(path)

print(df)