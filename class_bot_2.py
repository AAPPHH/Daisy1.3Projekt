import numpy as np
import random
from class_player import *

class TreeBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def make_move(self, game, board):
            if board.board[board.m // 2][board.n // 2] == 0:
                print("Zentrum")
                return Player.place_piece(self, board.m // 2, board.n // 2, game, board)
            elif board.board[board.m // 2+1][board.n // 2+1] == 0:
                print("Oben von der Mitte")
                return Player.place_piece(self, board.m // 2+1, board.n // 2+1, game, board)
            elif board.board[board.m // 2-1][board.n // 2-1] == 0:
                print("Unten von der Mitte")
                return Player.place_piece(self, board.m // 2-1, board.n // 2-1, game, board)         
            elif board.board[board.m // 2+2][board.n // 2+2] == 0:
                print("Rechts von der Mitte")
                return Player.place_piece(self, board.m // 2+2, board.n // 2+2, game, board)
            elif board.board[board.m // 2-2][board.n // 2-2] == 0:
                print("Links von der Mitte")
                return Player.place_piece(self, board.m // 2-2, board.n // 2-2, game, board)   
            else:
                row = random.randint(0, 4)
                col = random.randint(0, 4)
                return Player.place_piece(self, row, col, game, board) #Parameter die die Rausgehen
            
    
    def get_chain(self, board, player_number):
        chain = []
        for row_index, row in enumerate(board.board):
            for col_index, value in enumerate(row):
                if value == player_number:
                    chain.append((row_index, col_index))
        return chain
    
def get_neighbors(array, row, col, radius=1):
    """Gibt einen Ausschnitt um die angegebene Position mit gegebenem Radius zurück."""
    start_row, end_row = max(0, row - radius), min(array.shape[0], row + radius + 1)
    start_col, end_col = max(0, col - radius), min(array.shape[1], col + radius + 1)
    return array[start_row:end_row, start_col:end_col]

# Beispiel-Array
board = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Erhalten der Nachbarn um Position (1, 1)
neighbors = get_neighbors(board, 1, 1)
print(neighbors)