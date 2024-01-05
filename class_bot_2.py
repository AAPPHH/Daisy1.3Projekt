import numpy as np
import random
from class_player import *

class TreeBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    # TreeBot.place_piece(self.current_player, self, self.board) Parameter die reinkommen
    def make_move(self, game, board): 
        if self.board.board[self.m // 2][self.n // 2] == 0:  # Zentrum
            self.board.board[self.m // 2][self.n // 2] = 2
        elif self.board[self.m // 2 + 1][self.n // 2] == 0:  # Oben von der Mitte
            self.board[self.m // 2 + 1][self.n // 2] = 2
        elif self.board[self.m // 2 - 1][self.n // 2] == 0:  # Unten von der Mitte
            self.board[self.m // 2 - 1][self.n // 2] = 2
        elif self.board[self.m // 2][self.n // 2 + 1] == 0:  # Rechts von der Mitte
            self.board[self.m // 2][self.n // 2 + 1] = 2
        elif self.board[self.m // 2][self.n // 2 - 1] == 0:  # Links von der Mitte
            self.board[self.m // 2][self.n // 2 - 1] = 2
        else:
            exceptional_list = [self.m // 2, self.m // 2 + 1, self.m // 2 - 1, self.n // 2, self.n // 2 + 1, self.n // 2 - 1]
            random_row = random.choice(valid_rows)
            random_column = random.choice(valid_columns)
            self.board[random_row][random_column] = 2
            Player.place_piece(self, random_row, random_column, game, board) #Parameter die die Rausgehen


