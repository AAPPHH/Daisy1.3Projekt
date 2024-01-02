import pandas as pd

path = r"Data_Science/game_history.pkl"

df = pd.read_pickle(path)

# pd.set_option('display.max_rows', None)  # Zeigt alle Zeilen an
# pd.set_option('display.max_columns', None)  # Zeigt alle Spalten an
# pd.set_option('display.width', None)  # Passt die Breite an, um Zeilenumbrüche zu verhindern
# pd.set_option('display.max_colwidth', None)  # Zeigt den vollen Inhalt der Zellen an

# # Anzeigen des DataFrames
# print(df)
board_state_first_row = df.loc[25, 'board_state']
print(board_state_first_row)