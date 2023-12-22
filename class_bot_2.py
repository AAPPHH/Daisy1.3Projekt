import numpy as np

import random
from class_player import *

class Bot_2:
    def __init__(self, m, n, board): 
        self.m = m
        self.n = n
        self.board = np.zeros((m, n), dtype=int)

<<<<<<< HEAD
    def make_intelligent_move(self):
=======
    def make_intelligent_move(self, game, board):
>>>>>>> 6ef0fa05dc132673feedb8b99b9e93c0512effb5
        if self.board[self.m // 2][self.n // 2] == 0:  # Zentrum
            self.board[self.m // 2][self.n // 2] = 2
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
            valid_rows = [i for i in range(self.m) if i not in exceptional_list]
            valid_columns = [i for i in range(self.n) if i not in exceptional_list]
            random_row = random.choice(valid_rows)
            random_column = random.choice(valid_columns)
<<<<<<< HEAD
            self.board[random_row][random_column] = 2
=======
            # self.board[random_row][random_column] = 2
            Player.place_piece(self, random_row, random_column, game, board)
>>>>>>> 6ef0fa05dc132673feedb8b99b9e93c0512effb5


