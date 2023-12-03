from class_player import *
from class_board import *
class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number


    def place_piece(self, row, col, game, board):
        if board.is_valid_move(row, col):
            board.board[row][col] =  self.player_number #objekt der game class übergeben
            return True
        return False


