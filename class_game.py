import time
import copy
from class_board import *
from class_player import *
from class_bot_1 import *
from class_bot_2 import *
from class_bot_3 import *
from class_bot_4 import *
from Data import *

class Game:
    def __init__(self, board):
        self.m = board.m  # Zeilen
        self.n = board.n  # Spalten
        self.k = board.k  # Gewinnbedingung
        self.board = board # objekt der klasse board
        self.player1 = Player("", 1)
        self.player2 = Player("", 2)
        self.current_player = self.player1
        self.game_arrays = []
        self.winner = None
        self.starter = None

    def start(self):
        """
        Starts the game and asks the player for the game mode.
        """
        while True:
            self.reset_game()
            start_choice = input("Let's play five in a row! Wollen Sie oder soll der Computer spielen? (1/2): ")
            if start_choice == "1":
                self.player1.name = input("Bitte geben Sie Ihren Namen ein: ")
                while True:
                    choice = input(f"Hallo {self.player1.name}, möchten Sie gegen einen anderen Spieler oder gegen den Computer spielen? (1/2): ")
                    if choice == "1":
                        self.player2.name = input("Spieler 2: Bitte geben Sie Ihren Namen ein: ")
                        self.whos_first()
                    elif choice == "2":
                        while True:
                            choice = input(f"Hallo {self.player1.name}, möchten Sie gegen einen SecretsBot, ChainTreeBot, MinimaxBot oder einen MonteCarloBot spielen? (1/2/3/4): ")
                            if choice == "1":
                                self.player2 = SecretsBot("SecretsBot", 2)
                            elif choice == "2":
                                self.player2 = ChainTreeBot("ChainTreeBot", 2)
                            elif choice == "3":
                                self.player2 = MinimaxBot("MinimaxBot", 2)
                            elif choice == "4":
                                self.player2 = MonteCarloBot("MonteCarloBot", 2)
                            else:
                                print("Bitte geben Sie eine gültige Zahl ein.")
                            self.whos_first()
                            break
                        break
                    else:
                        print("Bitte geben Sie eine gültige Zahl ein.")
                break
            elif start_choice == "2":
                while True:
                    choice_bot_1 = input(f"Möchtest du das einen RandomBot, TreeBot, MinimaxBot oder einen MonteCarloBot Player One ist? (1/2/3/4):")
                    if choice_bot_1 == "1":
                        self.player1 = SecretsBot("SecretsBot", 1)
                        break
                    elif choice_bot_1 == "2":
                        self.player1 = ChainTreeBot("ChainTreeBot", 1) 
                        break   
                    elif choice_bot_1 == "3":
                        self.player1 = MinimaxBot("MinimaxBot", 1)
                        break
                    elif choice_bot_1 == "4":
                        self.player1 = MonteCarloBot("MonteCarloBot", 1) 
                        break
                    else:
                        print("Bitte geben Sie eine gültige Zahl ein.")
                    self.current_player = self.player1
                while True:
                    choice_bot_2 = input(f"Möchtest du das einen RandomBot, TreeBot, MinimaxBot oder einen MonteCarloBot Player Two ist? (1/2/3/4):")
                    if choice_bot_2 == "1":
                        self.player2 = SecretsBot("SecretsBot_2", 2)
                        break
                    elif choice_bot_2 == "2":
                        self.player2 = ChainTreeBot("ChainTreeBot_2", 2)
                        break
                    elif choice_bot_2 == "3":
                        self.player2 = MinimaxBot("MinimaxBot_2", 2)
                        break
                    elif choice_bot_2 == "4":
                        self.player2 = MonteCarloBot("MonteCarloBot_2", 2)
                        break
                    else:
                        print("Bitte geben Sie eine gültige Zahl ein.")
                num_games = None
                while num_games is None:
                    num_games_input = input("Wie viele Runden möchtest du spielen? (1-10000): ")
                    try:
                        num_games_converted = int(num_games_input)
                        if 1 <= num_games_converted <= 10000:
                            num_games = num_games_converted
                        else:
                            print("Bitte geben Sie eine gültige Zahl zwischen 1 und 10000 ein.")
                    except ValueError:
                        print("Bitte geben Sie eine gültige Zahl ein.")
                    for game_number in range(int(num_games)):
                        print(f"Spiel {game_number + 1} von {num_games}")
                        self.current_player = self.player1
                        self.game_loop()
                        self.reset_game()
                    print("Alle Spiele wurden gespielt.")
                    break
            elif start_choice == "3":
                num_games = None
                while num_games is None:
                    num_games_input = input("Wie viele Runden möchtest du spielen? (1-10000): ")
                    try:
                        num_games_converted = int(num_games_input)
                        if 1 <= num_games_converted <= 10000:
                            num_games = num_games_converted
                        else:
                            print("Bitte geben Sie eine gültige Zahl zwischen 1 und 10000 ein.")
                    except ValueError:
                        print("Bitte geben Sie eine gültige Zahl ein.")
                    self.all_bot_vs_bot(int(num_games))
                    print("Alle Spiele wurden gespielt.")
                    break
            else:
                print("Bitte geben Sie eine gültige Zahl ein.")
    
    def all_bot_vs_bot(self, num_games):
        """
        Plays all bots against each other for a certain number of games.
        """
        bots = [SecretsBot, ChainTreeBot, MinimaxBot]
        for i, Bot1 in enumerate(bots):
            for Bot2 in bots[i:]:
                for game_number in range(num_games):
                    self.player1 = Bot1(f"{Bot1.__name__}", 1)
                    self.player2 = Bot2(f"{Bot2.__name__}_2", 2)
                    self.reset_game()
                    print(f"Spiel {game_number + 1} von {num_games}")
                    self.game_loop()
                    self.player1 = Bot2(f"{Bot2.__name__}", 1)
                    self.player2 = Bot1(f"{Bot1.__name__}_2", 2)
                    self.reset_game()
                    print(f"Spiel {game_number + 1} von {num_games}")
                    self.game_loop()
                        
    def reset_game(self):
        """
        Resets the game stats and the board.
        """
        self.game_arrays = []
        self.board.reset_board()
        self.winner = None
        self.current_player = self.player1
        
    def whos_first(self):
        """
        Asks the player if he wants to start first and starts the game loop.
        """
        while True:
            order_choice = input(f"Möchtest du anfangen, {self.player1.name}? (j/n): ")
            if order_choice.lower() == 'n':
                self.current_player.set_player_number(2)
                self.current_player = self.player2 
                self.player2.set_player_number(1)
                self.game_loop()
                break
            elif order_choice.lower() == 'j':
                self.game_loop()
                break
            else:
                print("Bitte geben Sie eine gültige Antwort ein.")

    def switch_player(self):
        """
        Switches the current player.
        """
        self.current_player = (self.player2 if self.current_player == self.player1 else self.player1)

    def game_loop(self):
        """
        Main game loop till game is over.
        """
        game_over = False
        self.starter = self.current_player.name
        start_time = time.time()
        while not game_over:
            valid_move = True
            self.board.print_board()
            start_turn_time = time.time()
            if isinstance(self.current_player, SecretsBot):
                valid_move = SecretsBot.make_move(self.current_player, self, self.board)

            elif isinstance(self.current_player, ChainTreeBot):
                valid_move = ChainTreeBot.make_move(self.current_player, self, self.board)  

            elif isinstance(self.current_player, MinimaxBot):
                valid_move = MinimaxBot.make_move(self.current_player, self, self.board)

            elif isinstance(self.current_player, MonteCarloBot):
                valid_move = MonteCarloBot.make_move(self.current_player, self, self.board)
            
            elif isinstance(self.current_player, Player):
                try:
                    row = int(input(f"Spieler {self.current_player.name}, geben Sie die Zeilennummer ein (0-{self.m-1}): "))
                    col = int(input(f"Spieler {self.current_player.name}, geben Sie die Spaltennummer ein (0-{self.n-1}): "))
                except ValueError:
                    print("Bitte geben Sie gültige ganze Zahlen ein.")
                    continue
                valid_move = Player.make_move(self.current_player, row, col, self, self.board)  
                if not valid_move:
                    print("Bitte geben Sie eine gültige Zahl ein.")
                    continue

            if self.board.is_winner(self.current_player.player_number):
                game_over = True
                self.board.print_board()
                end_turn_time = time.time()
                print(f'Spielzugdauer: {end_turn_time - start_turn_time} Sekunden')
                end_time = time.time()
                print(f'Gesamtspieldauer: {end_time - start_time} Sekunden')
                self.winner = self.current_player.name
                Daisy.save_game_state(game)
                print(f"Spieler {self.current_player.name} hat gewonnen!")
                
                if isinstance(self.current_player, MonteCarloBot):
                    self.current_player.save_state()

            elif self.board.is_full():
                game_over = True
                self.board.print_board()
                end_turn_time = time.time()
                print(f'Spielzugdauer: {end_turn_time - start_turn_time} Sekunden')
                end_time = time.time()
                print(f'Gesamtspieldauer: {end_time - start_time} Sekunden')
                Daisy.save_game_state(game)
                print("Das Spiel endet unentschieden!")

            else:
                if valid_move == True:
                    end_turn_time = time.time()
                    self.game_arrays.append(copy.deepcopy(self.board.array))
                    try:
                        print(f'Spielzugdauer: {end_turn_time - start_turn_time} Sekunden')
                    except:
                        pass
                    self.switch_player()
                    
Daisy = Data_Science("game_history.pkl") # Erstellt ein neues Objekt der Klasse Data_Science
Spielbrett = Board() # Erstellt ein neues Spielbrett
game = Game(Spielbrett) # Erstellt ein neues Spiel
game.start() # Startet das Spiel