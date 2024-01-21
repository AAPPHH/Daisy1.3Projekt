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
        self.board = board #array objekt der klasse board
        self.player1 = Player("", 1)
        self.player2 = Player("", 2)
        self.current_player = self.player1
        self.game_arrays = []
        self.winner = None
        self.starter = None
    #echteres random
    #temp for temporary
    #random choice
    #pearl noise
    def start(self):
        start_choice = input("Let's play five in row! wollen sie oder soll der Computer spielen? (1/2):")
        if start_choice == "1":
            self.player1.name = input("Bitte geben sie ihre Namen ein:")
            choice = input(f"Hallo {self.player1.name}, möchtest du gegen einen anderen Spieler oder gegen den Computer spielen? (1/2):")
            if choice == "1":
                self.player2.name = input("Spieler 2: ")
                self.whos_first()
            elif choice == "2":
                choice = input(f"Hallo {self.player1.name}, möchtest du gegen einen RandomBot, TreeBot, MinimaxBot oder einen MonteCarloBot spielen? (1/2/3/4):")
                if choice == "1":
                    self.player2 = GomokuBot("GomokuBot", 2)
                    self.whos_first()
                elif choice == "2":
                    self.player2 = TreeBot("TreeBot", 2)
                    self.whos_first()
                elif choice == "3":
                    self.player2 = MinimaxBot("MinimaxBot", 2)
                    self.whos_first()
                elif choice == "4":
                    self.player2 = MonteCarloBot("MonteCarloBot", 2)
                    self.whos_first()
                else:
                    print("Bitte geben Sie eine gültige Zahl ein.")
            else:
                print("Bitte geben Sie eine gültige Zahl ein.")
        elif start_choice == "2":
            choice_bot_1 = input(f"Möchtest du das einen RandomBot, TreeBot, MinimaxBot oder einen MonteCarloBot Player One ist? (1/2/3/4):")
            if choice_bot_1 == "1":
                self.player1 = GomokuBot("GomokuBot", 1)
            elif choice_bot_1 == "2":
                self.player1 = TreeBot("ChainTreeBot", 1)
            elif choice_bot_1 == "3":
                self.player1 = MinimaxBot("MinimaxBot", 1)
            elif choice_bot_1 == "4":
                self.player1 = MonteCarloBot("MonteCarloBot", 1)
            else:
                print("Bitte geben Sie eine gültige Zahl ein.")
            self.current_player = self.player1
            choice_bot_2 = input(f"Möchtest du das einen RandomBot, TreeBot, MinimaxBot oder einen MonteCarloBot Player Two ist? (1/2/3/4):")
            if choice_bot_2 == "1":
                self.player2 = GomokuBot("GomokuBot_2", 2)
            elif choice_bot_2 == "2":
                self.player2 = TreeBot("ChainTreeBot_2", 2)
            elif choice_bot_2 == "3":
                self.player2 = MinimaxBot("MinimaxBot_2", 2)
            elif choice_bot_2 == "4":
                self.player2 = MonteCarloBot("MonteCarloBot_2", 2)
            num_games = input(f"Wie viele Runden möchtest du spielen? (1-10000):")
            try:
                for game_number in range(int(num_games)):
                        print(f"Spiel {game_number + 1} von {num_games}")
                        self.game_loop()
                        self.game_arrays = []
                        self.board.reset_board()
                        self.current_player = self.player1
                print("Alle Spiele wurden gespielt.")
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")
        else:
            print("Bitte geben Sie eine gültige Zahl ein.")
    
    def whos_first(self):
        order_choice = input(f"Möchtest du anfangen, {self.player1.name}? (j/n): ")
        if order_choice.lower() == 'n':
            self.current_player = self.player2 
            self.game_loop()
        elif order_choice.lower() == 'j':
            self.game_loop()
        else:
            print("Bitte geben Sie eine gültige Antwort ein.")

    def switch_player(self):
        self.current_player = (self.player2 if self.current_player == self.player1 else self.player1)

    def game_loop(self):
        game_over = False
        self.starter = self.current_player.name
        start_time = time.time()
        while not game_over:
            valid_move = True
            self.board.print_board()
            start_turn_time = time.time()
            if isinstance(self.current_player, GomokuBot):
                valid_move = GomokuBot.place_piece(self.current_player, self, self.board)

            elif isinstance(self.current_player, TreeBot):
                valid_move = TreeBot.make_move(self.current_player, self, self.board)  

            elif isinstance(self.current_player, MinimaxBot):
                valid_move = MinimaxBot.make_move(self.current_player, self, self.board)

            elif isinstance(self.current_player, MonteCarloBot):
                valid_move = MonteCarloBot.place_piece(self.current_player, self, self.board)
            
            elif isinstance(self.current_player, Player):
                try:
                    row = int(input(f"Spieler {self.current_player.name}, geben Sie die Zeilennummer ein (0-{self.m-1}): "))
                    col = int(input(f"Spieler {self.current_player.name}, geben Sie die Spaltennummer ein (0-{self.n-1}): "))
                except ValueError:
                    print("Bitte geben Sie gültige ganze Zahlen ein.")
                    continue
                valid_move = Player.place_piece(self.current_player, row, col, self, self.board)  
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
                # if isinstance(self.current_player, MinimaxBot):
                #     self.current_player.save_state() 
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
                    self.game_arrays.append(copy.deepcopy(self.board.board))
                    try:
                        print(f'Spielzugdauer: {end_turn_time - start_turn_time} Sekunden')
                    except:
                        pass
                    self.switch_player()
                    
Daisy = Data_Science("game_history.pkl")
Spielbrett = Board()
game = Game(Spielbrett)
game.start()