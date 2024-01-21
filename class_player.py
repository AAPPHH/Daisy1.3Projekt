from class_board import *

class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number


    def place_piece(self, row, col, game, board):
        if board.is_valid_move(row, col): 
            board.board[row][col] =  self.player_number 
            return True  
        return False 
    
    def set_player_number(self, new_player_number):
        self.player_number = new_player_number