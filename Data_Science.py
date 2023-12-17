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
        
    def play_multiple_games(self, bot1, bot2, num_games):
        """
        Spielt mehrere Spiele zwischen zwei Bots.

        :param bot1: Eine Instanz von Bot, der als Spieler 1 fungiert.
        :param bot2: Eine Instanz von Bot, der als Spieler 2 fungiert.
        :param num_games: Anzahl der Spiele, die gespielt werden sollen.
        """
        for game_number in range(num_games):
            print(f"Spiel {game_number + 1} von {num_games}")
            self.reset_board()
            self.play_bot_vs_bot(bot1, bot2)
            # Hier können Sie weitere Statistiken oder Logik nach jedem Spiel hinzufügen.
