import pandas as pd
import pickle

class Data_Science:
    def __init__(self, filename="game_history.pkl"):
        self.filename = filename

    def Player_Name_detection(self, player1, player2):
        if player1 == "GomokuBot" and player2 == "GomokuBot":
            spielerkennung = "Bot 1 vs. Bot 2"
        elif player1 == "GomokuBot" and player2 == "TreeBot":
            spielerkennung = "Bot 1 vs. Bot 2"
        elif player1 == "GomokuBot" and player2 == "MinimaxBot":
            spielerkennung = "Bot 1 vs. Bot 2"
        elif player1 == "TreeBot" and player2 == "GomokuBot":
            spielerkennung = "Bot 1 vs. Bot 2"
        elif player1 == "TreeBot" and player2 == "TreeBot":
            spielerkennung = "Bot 1 vs. Bot 2"
        elif player1 == "TreeBot" and player2 == "MinimaxBot":
            spielerkennung = "Bot 1 vs. Bot 2"
        elif player1 == "MinimaxBot" and player2 == "GomokuBot":
            spielerkennung = "Bot 1 vs. Bot 2"
        elif player1 == "MinimaxBot" and player2 == "TreeBot":
            spielerkennung = "Bot 1 vs. Bot 2"
        elif player1 == "MinimaxBot" and player2 == "MinimaxBot":
            spielerkennung = "Bot 1 vs. Bot 2"
        elif player1 == "" and player2 == "GomokuBot":
            spielerkennung = "Spieler vs. GomokuBot"
        elif player1 == "" and player2 == "TreeBot":
            spielerkennung = "Spieler vs. TreeBot"
        elif player1 == "" and player2 == "MinimaxBot":
            spielerkennung = "Spieler vs. MinimaxBot"
        elif player1 == "GomokuBot" and player2 == "":
            spielerkennung = "GomokuBot vs. Spieler"
        elif player1 == "TreeBot" and player2 == "":
            spielerkennung = "TreeBot vs. Spieler"
        elif player1 == "MinimaxBot" and player2 == "":
            spielerkennung = "MinimaxBot vs. Spieler"
        elif player1 == "" and player2 == "":
            spielerkennung = "Spieler vs. Spieler"
        return spielerkennung
    

    def save_game_state(self, game):
        game_history = self.load_game_history()
        for state in game.game_arrays:
            new_row = pd.DataFrame([{
                'player1': game.player1.name,
                'player2': game.player2.name,
                'board_state': state
            }])
            game_history = pd.concat([game_history, new_row], ignore_index=True)
        self.save_game_history(game_history)
    

    def save_game_history(self, game_history):
        game_history.to_pickle(self.filename)

    def load_game_history(self):
        try:
            return pd.read_pickle(self.filename)
        except FileNotFoundError:
            return pd.DataFrame()


