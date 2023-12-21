import pickle

class Data_Science:
    def __init__(self, filename="game_history.pkl"):
        self.filename = filename

    def save_game_history(self, game_history):
        with open(self.filename, "wb") as f:
            pickle.dump(game_history, f)

    def load_game_history(self):
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
        
