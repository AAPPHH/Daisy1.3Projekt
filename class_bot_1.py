from class_player import *
from class_board import * 
import random
class GomokuBot(Player):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def make_move(self):
        random_row = random.randint(0, 4)
        random_col = random.randint(0, 4)
        self.place_piece(random_row, random_col)