import pandas as pd


gamefile = pd.read_pickle(r"Data_Science/game_history.pkl")
gamefile.head()
gamefile.to_excel("New_Data.xlsx")
gamefile.to_pickle("New_Data.pkl")
