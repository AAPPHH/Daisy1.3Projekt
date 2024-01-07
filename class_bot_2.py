import numpy as np
import random
from class_player import *

class Silly(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def be_smart(self, game, board):
        """
        Methode von Silly, die versucht, einen Stein nach folgendem System zu setzten:
        1. Ist das Zentrum leer? -> Dann setzt dort den Stein.
        2. Ist oben von der Mitte leer? ...
        3. ... unten von der Mitte...
        4. ... recht von der Mitte...
        5. ... links von der Mitte...
        6. Sind alle Felder belegt, wird aus eine Liste von rows und cols erstellt, wobei die Liste alle Fehlversuche exkludiert.
        7. Dann wird aus dieser Liste eine Zahl für row und col zufällig generiert.
        8. Das zufällig generierte Feld wird gleich der Spielerzahl gesetzt.
        """
        if self.board[self.m // 2][self.n // 2] == 0:  # Zentrum
            Player.place_piece(self, board.m // 2, board.n // 2, game, board)
        elif self.board[self.m // 2 + 1][self.n // 2] == 0:  # Oben von der Mitte
            Player.place_piece(self, board.m // 2 + 1, board.n // 2, game, board)
        elif self.board[self.m // 2 - 1][self.n // 2] == 0:  # Unten von der Mitte
            Player.place_piece(self, board.m // 2 - 1, board.n // 2, game, board)
        elif self.board[self.m // 2][self.n // 2 + 1] == 0:  # Rechts von der Mitte
            Player.place_piece(self, board.m // 2, board.n // 2 + 1, game, board)
        elif self.board[self.m // 2][self.n // 2 - 1] == 0:  # Links von der Mitte
            Player.place_piece(self, board.m // 2, board.n // 2 - 1, game, board)
        elif self.board[self.m // 2 + 2][self.n // 2] == 0:  # Zwei oben von der Mitte
            Player.place_piece(self, board.m // 2 + 2, board.n // 2, game, board)
        elif self.board[self.m // 2 - 2][self.n // 2] == 0:  # Zwei unten von der Mitte
            Player.place_piece(self, self.m // 2 - 2, self.n // 2, game, board)
        elif self.board[self.m // 2][self.n // 2 + 2] == 0:  # Zwei Rechts von der Mitte
            Player.place_piece(self, self.m // 2, self.n // 2 + 2, game, board)
        elif self.board[self.m // 2][self.n // 2 - 2] == 0:  # Zwei Links von der Mitte
            Player.place_piece(self, self.m // 2, self.n // 2 - 2, game, board)
        else:
            exceptional_list = [self.m // 2, self.m // 2 + 1, self.m // 2 - 1, self.m // 2 + 2, self.m // 2 - 2, self.n // 2, self.n // 2 + 1, self.n // 2 - 1, self.n // 2 + 2, self.n // 2 - 2]
            valid_rows = [i for i in range(self.m) if i not in exceptional_list]
            valid_columns = [i for i in range(self.n) if i not in exceptional_list]
            random_row = random.choice(valid_rows)
            random_column = random.choice(valid_columns)
            Player.place_piece(self, random_row, random_column, game, board)
