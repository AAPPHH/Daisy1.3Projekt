import random
from class_board import *

class GomokuBot(Player):
    def super__init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col

    def make_move(self, board):
        random_row = random.randint(0, 4)
        random_col = random.randint(0, 4)
        while board[random_row][random_col] != 0:
            random_row = random.randint(0, 4)
            random_col = random.randint(0, 4)
        board[random_row][random_col] = 2




