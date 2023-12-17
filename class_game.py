from class_board import *
from class_player import *
from class_bot_1 import *
from class_bot_2 import *
from class_bot_3 import *
from Data_Science import *

class Game:
    def __init__(self, board):
        self.m = board.m  # Zeilen
        self.n = board.n  # Spalten
        self.k = board.k  # Gewinnbedingung
        self.board = board
        self.player1 = Player("", 1)
        self.player2 = Player("", 2)
        self.current_player = self.player1

    def start(self):
        start_choice = input("Let's play five in row!/n wollen sie oder soll der Computer spielen? (1/2):")
        if start_choice == "1":
            self.player1.name = input("Bitte geben sie ihre Namen ein:")
            choice = input(f"Hallo {self.player1.name}, möchtest du gegen einen anderen Spieler oder gegen den Computer spielen? (1/2):")
            if choice == "1":
                self.player2.name = input("Spieler 2: ")
                order_choice = input(f"Möchtest du anfangen, {self.player1.name}? (j/n): ")
                if order_choice.lower() == 'n':
                    self.current_player = self.player2 
                    self.game_loop()
                else:
                    self.game_loop()
            elif choice == "2":
                choice = input(f"Hallo {self.player1.name}, möchtest du gegen einen RandomBot, TreeBot einen MinimaxBot spielen? (1/2/3):")
                if choice == "1":
                    self.player2 = GomokuBot("GomokuBot", 2)
                    self.whos_first()
                elif choice == "2":
                    self.player2 = TreeBot("TreeBot", 2)
                    self.whos_first()
                elif choice == "3":
                    self.player2 = MinimaxBot("MinimaxBot", 2)
                    self.whos_first()
                else:
                    print("Bitte geben Sie eine gültige Zahl ein.")
        elif start_choice == "2":
            choice_bot_1 = input(f"Möchtest du das einen RandomBot, TreeBot oder einen MinimaxBot Player One ist? (1/2/3):")
            choice_bot_2 = input(f"Möchtest du das einen RandomBot, TreeBot oder einen MinimaxBot Player Two ist? (1/2/3):")
            choice_rounds = input(f"Wie viele Runden möchtest du spielen? (1/2/3/4/5):")
            self.game_loop()
        else:
            print("Bitte geben Sie eine gültige Zahl ein.")

    def whos_first(self):
        order_choice = input(f"Möchtest du anfangen, {self.player1.name}? (j/n): ")
        if order_choice.lower() == 'n':
            self.current_player = self.player2 
            self.game_loop()
        else:
            self.game_loop()

    def switch_player(self):
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def game_loop(self):
        game_over = False
        while not game_over:
            valid_move = True
            self.board.print_board()
            if isinstance(self.current_player, GomokuBot):
                GomokuBot.place_piece(self.current_player, self, self.board)

            elif isinstance(self.current_player, MinimaxBot):
                MinimaxBot.make_move(self.current_player, row, col, self, self.board)
            
            # elif isinstance(self.current_player, GomokuBot_2):
            #     GomokuBot_2.place_piece(self.current_player, row, col, self, self.board)    

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
                print(f"Spieler {self.current_player.name} hat gewonnen!")
            elif self.board.is_full():
                game_over = True
                self.board.print_board()
                print("Das Spiel endet unentschieden!")
            else:
                if valid_move == True: 
                    self.switch_player()

Spielbrett = Board()
game = Game(Spielbrett)
game.start()

