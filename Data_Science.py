import pandas as pd
import pickle

class Data_Science:
    def __init__(self, filename="game_history.pkl"):
        self.filename = filename

    def save_game_history(self, game_history):
        # Speichert den DataFrame als Pickle-Datei
        game_history.to_pickle(self.filename)

    def load_game_history(self):
        try:
            # Lädt den DataFrame aus der Pickle-Datei
            return pd.read_pickle(self.filename)
        except FileNotFoundError:
            # Gibt einen leeren DataFrame zurück, wenn die Datei nicht existiert
            return pd.DataFrame()
        
