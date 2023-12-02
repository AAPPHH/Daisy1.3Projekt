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
    
    # def make_move(self, row, col):
    #     if self.board[row][col] == ' ':
    #         self.board[row][col] = self.current_player
    #         self.current_player = 'O' if self.current_player == 'X' else 'X'
    #     else:
    #         print('Invalid move. Please try again.')


# Path: class_game
