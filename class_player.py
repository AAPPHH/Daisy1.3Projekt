from class_board import *

class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number
        #memo einfügen


    def place_piece(self, row, col, game, board):
        print("old place_piece")
        if board.is_valid_move(row, col): 
            board.array[row][col] =  self.player_number 
            return True  
        return False 
    
    def make_move(self, row, col, game, board):
        """
        Places a piece on the board.
        """
        if board.is_valid_move(row, col): 
            board.array[row][col] =  self.player_number 
            return True  
        return False 
    
    def set_player_number(self, new_player_number):
        """
        Sets the player number.
        """
        self.player_number = new_player_number