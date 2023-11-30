from class_board import *
from class_player import *
class Game:
    def __init__(self, m, n, k, board, player1, player2):
        self.m = m # Zeilen
        self.n = n # Spalten
        self.k = k # Gewinnbedingung
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = 'X'

    def start(self):
       Spielbrett = Board()

    def game_loop(self):
        game_over = False
        while not game_over:
            self.print_board()
            try:
                row = int(input(f"Spieler {self.current_player}, geben Sie die Zeilennummer ein (0-4): "))
                col = int(input(f"Spieler {self.current_player}, geben Sie die Spaltennummer ein (0-4): ")) #hast to be array based
            except ValueError:
                print("Bitte geben Sie gültige ganze Zahlen ein.")
                continue

            if self.make_move(row, col):
                if self.check_winner():
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
                continue

# Usage example:
game = Game()
game.print_board()
game.make_move(7, 7)
game.print_board()


Human = Player.Player("John", 1)
print(Human.player_number)
