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
        
    def evaluate_board(self, board):
        # Implement the evaluation function to assess the current state of the board
        pass

    def evaluate_position(self, board):
        # Implement the evaluation function to assess the current position on the board
        pass


