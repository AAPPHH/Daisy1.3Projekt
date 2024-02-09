from class_board import *
from class_player import * 
import secrets

class SecretsBot(Player):
    '''
    Places pieces at randome positions. Based on the secrets module.
    '''
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def make_move(self, game, board):
        row = secrets.randbelow(board.m)
        col = secrets.randbelow(board.n)
        return Player.make_move(self, row, col, game, board)
