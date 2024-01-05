import numpy as np
import random
from class_player import *

class Silly(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def be_smart(self, game, board):
            if board.board[board.m // 2][board.n // 2] == 0:  # Zentrum
                Player.place_piece(self, board.m // 2, board.n // 2, game, board)
                print("Zentrum")
            elif board.board[board.m // 2 + 1][board.n // 2 + 1] == 0:  # Oben von der Mitte
                Player.place_piece(self, board.m // 2 + 1, board.n // 2 + 1, game, board)
                print("Oben von der Mitte")
            elif board.board[board.m // 2 - 1][board.n // 2 - 1] == 0:  # Unten von der Mitte
                Player.place_piece(self, board.m // 2 - 1, board.n // 2 - 1, game, board)
                print("Unten von der Mitte")
            elif board.board[board.m // 2 + 2][board.n // 2 + 2] == 0:  # Rechts von der Mitte
                Player.place_piece(self, board.m // 2 + 2, board.n // 2 + 2, game, board)
                print("Rechts von der Mitte")
            elif board.board[board.m // 2 - 2][board.n // 2 - 2] == 0:  # Links von der Mitte
                Player.place_piece(self, board.m // 2 - 2, board.n // 2 - 2, game, board)
                print("Links von der Mitte")
            else:
                exceptional_list = [self.m // 2, self.m // 2 + 1, self.m // 2 - 1, self.n // 2, self.n // 2 + 1, self.n // 2 - 1]
                valid_rows = [i for i in range(self.m) if i not in exceptional_list]
                valid_columns = [i for i in range(self.n) if i not in exceptional_list]
                random_row = random.choice(valid_rows)
                random_column = random.choice(valid_columns)
                Player.place_piece(self, random_row, random_column, game, board)
