import time
from class_board import *
from class_player import *
from class_bot_1 import *

class Game:
    def __init__(self, board):
        self.m = board.m # Zeilen
        self.n = board.n # Spalten
        self.n = board.n # Spalten
        self.k = board.k # Gewinnbedingung
        self.board = board
        self.player1 = Player("", 1)
        self.player2 = Player("", 2)
        self.current_player = self.player1

    def start(self):
        print("Let's play five in row!/n Bitte geben sie ihre Namen ein")
        time.sleep(1)
        self.player1.name = input("Spieler 1: ")
        time.sleep(1)
        choice = input(f"Hallo {self.player1.name}, möchtest du gegen einen anderen Spieler oder gegen den Computer spielen? (1/2):")
        time.sleep(1)
        if choice == "1":
              self.player2.name = input("Spieler 2: ")
              self.game_loop()
        elif choice == "2":
              self.player2 = GomokuBot("GomokuBot", 2)
              self.game_loop()
        elif choice == "3":
             pass
        else:
              player2 = "Computer"
              game.game_loop()

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def game_loop(self):
        game_over = False
        while not game_over:
            self.board.print_board()
            if isinstance(self.current_player, GomokuBot):
                self.current_player.make_move()
            else:
                try:
                    row = int(input(f"Spieler {self.current_player.name}, geben Sie die Zeilennummer ein (0-{self.m-1}): "))
                    col = int(input(f"Spieler {self.current_player.name}, geben Sie die Spaltennummer ein (0-{self.n-1}): "))
                except ValueError:
                    print("Bitte geben Sie gültige ganze Zahlen ein.")
                continue

            if Player.place_piece(self.current_player, row, col, self, self.board):
                if self.board.is_winner(self.current_player.player_number):
                    game_over = True
                    self.board.print_board()
                    print(f"Spieler {self.current_player.name} hat gewonnen!")
                elif self.board.is_full():
                    game_over = True
                    self.board.print_board()
                    print("Das Spiel endet unentschieden!")
                else:
                    self.switch_player()
            else:
                print("Ungültiger Zug, bitte versuchen Sie es erneut.")
   
Spielbrett = Board()
game = Game(Spielbrett)
game.start()

# def game_loop(self):
#     game_over = False
#     while not game_over:
#         self.board.print_board()
#         if isinstance(self.current_player, GomokuBot):
#             self.current_player.make_move()
#         else:
#             try:
#                 row = int(input(f"Spieler {self.current_player.name}, geben Sie die Zeilennummer ein (0-{self.m-1}): "))
#                 col = int(input(f"Spieler {self.current_player.name}, geben Sie die Spaltennummer ein (0-{self.n-1}): "))
#             except ValueError:
#                 print("Bitte geben Sie gültige ganze Zahlen ein.")
#                 continue
#             if Player.place_piece(self.current_player, row, col, self, self.board):
#                 if self.board.is_winner(self.current_player.player_number):
#                     game_over = True
#                     self.board.print_board()
