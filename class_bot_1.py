import random
from class_board import *
from class_player import *

class GomokuBot(Player):
    def __init__(self, name, row, col, **Kwargs):
        super().__init__()
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




