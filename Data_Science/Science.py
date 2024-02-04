import pandas as pd
import sketch

path = r"Data_Science/Monte_Mini.pkl"

df = pd.read_pickle(path)

pd.set_option('display.max_rows', None)  # Zeigt alle Zeilen an
pd.set_option('display.max_columns', None)  # Zeigt alle Spalten an
pd.set_option('display.width', None)  # Passt die Breite an, um Zeilenumbrüche zu verhindern
pd.set_option('display.max_colwidth', None)  # Zeigt den vollen Inhalt der Zellen an

# # Anzeigen des DataFrames
# print(df.head(5))
# board_state_first_row = df.loc[25, 'board_state']
# print(board_state_first_row)

winner = df['winner'].value_counts()
print(winner)

treebot_wins = df[df['winner'] == 'MonteCarloBot']
average_moves_treebot_wins = treebot_wins['N_turn'].mean()
print(average_moves_treebot_wins)

df.to_excel("Data_Science/check.xlsx")

df.sketch.ask("Which columns are integer type?")

df1 = pd.read_pickle(r"Data_Science/all_vs_all.pkl")
df2 = pd.read_pickle(r"Data_Science/Monte_Chain.pkl")
df3 = pd.read_pickle(r"Data_Science/Monte_Mini.pkl")


df4 = pd.concat([df1, df2, df3], axis=0).reset_index(drop=True)
df4.to_pickle("Data_Science/Bots_Games.pkl")
df4.to_excel("Data_Science/Bots_Games.xlsx")