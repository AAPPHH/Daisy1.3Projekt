from class_board import *

from class_player import *

from class_board import * 

import random

class GomokuBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def make_move(self, board):
        random_row = random.randint(0, m)
        random_col = random.randint(0, n)
        self.place_piece(random_row, random_col)
        self.place_piece(random_row, random_col)
        
        # while board[random_row][random_col] != 0:
        #     random_row = random.randint(0, 4)
        #     random_col = random.randint(0, 4)
        # board[random_row][random_col] = 2

#%%

from class_board import *
from class_player import *
import random

class GomokuBot(Player):
    def __init__(self, name, player_number, m=5, n=5):
        super().__init__(name, player_number)
        self.m = m
        self.n = n
    
    def make_move(self, board):
        random_row = random.randint(0, self.m - 1)
        random_col = random.randint(0, self.n - 1)
        self.place_piece(random_row, random_col, board)

