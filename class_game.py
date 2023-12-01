import time
from class_board import *
from class_player import *
from class_bot_1 import *
class Game:
    def __init__(self, m, n, k, board, player1, player2):
        self.m = m # Zeilen
        self.n = n # Spalten
        self.k = k # Gewinnbedingung
        self.player1 = player1
        self.player2 = player2
        self.current_player = 'X'

    def start(self):
        print("Let's play five in row!/n Bitte geben sie ihre Namen ein:")
        game = Game()
        time.sleep(1)
        player1 = input("Spieler 1: ")
        time.sleep(1)
        choice = input(f"Hallo {player1}, möchtest du gegen einen anderen Spieler oder gegen den Computer spielen? (1/2):")
        time.sleep(1)
        if choice == 1:
              player2 = input("Spieler 2: ")
              game.game_loop()
        else:
              player2 = "Computer"
              game.game_loop()

    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1

    def game_loop(self):
        game_over = False
        while not game_over:
            self.print_board()
            try:
                row = int(input(f"Spieler {self.current_player}, geben Sie die Zeilennummer ein (0-{self.m-1}): "))
                col = int(input(f"Spieler {self.current_player}, geben Sie die Spaltennummer ein (0-{self.n-1}): "))
            except ValueError:
                print("Bitte geben Sie gültige ganze Zahlen ein.")
                continue

            if self.place_piece(row, col):
                if self.is_winner():
                    game_over = True
                    self.print_board()
                    print(f"Spieler {self.current_player} hat gewonnen!")
                elif self.is_full():
                    game_over = True
                    self.print_board()
                    print("Das Spiel endet unentschieden!")
                else:
                    self.switch_player()
            else:
                print("Ungültiger Zug, bitte versuchen Sie es erneut.")

