import random
from class_board import *
from class_player import *
from class_board import * 
import random
class GomokuBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def place_piece(self, row, col, board):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        board.place_piece(row, col)
