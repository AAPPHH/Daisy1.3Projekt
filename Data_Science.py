import pandas as pd
import pickle

class Data_Science:
    def __init__(self, filename="game_history.pkl"):
        self.filename = filename

    def save_game_history(self, game_history):
        # Saves the DataFrame as a pickle file
        game_history.to_pickle(self.filename)

    def load_game_history(self):
        try:
            # Loads the DataFrame from the pickle file
            return pd.read_pickle(self.filename)
        except FileNotFoundError:
            # Returns an empty DataFrame if the file does not exist
            return pd.DataFrame()

def save_game_state(self, game):
    # Convert game states to DataFrame
    game_history = self.load_game_history()
    for state in game.game_arrays:
        new_row = pd.DataFrame([{
            'player1': game.player1.name,
            'player2': game.player2.name,
            'board_state': state
        }])
        game_history = game_history.append(new_row, ignore_index=True)
    
    # Save updated game history
    self.save_game_history(game_history)
