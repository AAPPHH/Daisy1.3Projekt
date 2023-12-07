<<<<<<< HEAD
import random
from class_board import *
from class_player import *

class GomokuBot(Player):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def make_move(self, board):
        random_row = random.randint(0, 4)
        random_col = random.randint(0, 4)
        self.place_piece(random_row, random_col)
        
        # while board[random_row][random_col] != 0:
        #     random_row = random.randint(0, 4)
        #     random_col = random.randint(0, 4)
        # board[random_row][random_col] = 2
=======
from class_player import *
from class_board import * 
import random
class GomokuBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def make_move(self):
        random_row = random.randint(0, 4)
        random_col = random.randint(0, 4)
        self.place_piece(random_row, random_col)
>>>>>>> fe24b2b9de5070fd8619261f2943e284cbce99e1
