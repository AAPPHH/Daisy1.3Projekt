import pandas as pd
import pickle

class Data_Science: 
    def __init__(self, filename="game_history.pkl"):
        self.filename = filename

    def save_game_state(self, game):
        """
        Saves the game state to a pickle file.
        """
        game_history = self.load_game_history()
        new_row = pd.DataFrame([{
                'winner': game.winner,
                'starter': game.starter,
                'N_turn': len(game.game_arrays),
                'player1': game.player1.name,
                'player2': game.player2.name,
                'board_state': game.game_arrays     
            }])
        game_history = pd.concat([game_history, new_row], ignore_index=True)
        self.save_game_history(game_history)
    
    def save_game_history(self, game_history):
        """
        Saves the game history to a pickle file.
        """
        game_history.to_pickle(self.filename)

    def load_game_history(self):
        """
        Loads the game history from a pickle file.
        """
        try:
            return pd.read_pickle(self.filename)
        except FileNotFoundError:
            return pd.DataFrame()


