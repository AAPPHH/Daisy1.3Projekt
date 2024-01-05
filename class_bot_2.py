import numpy as np
import random
from class_player import *

class TreeBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def make_move(self, game, board):
            if board.board[board.m // 2][board.n // 2] == 0:
                Player.place_piece(self, board.m // 2, board.n // 2, game, board)
                print("Zentrum")
            elif board.board[board.m // 2+1][board.n // 2+1] == 0:
                Player.place_piece(self, board.m // 2+1, board.n // 2+1, game, board)
                print("Oben von der Mitte")
            elif board.board[board.m // 2-1][board.n // 2-1] == 0:
                Player.place_piece(self, board.m // 2-1, board.n // 2-1, game, board)
                print("Unten von der Mitte")
            elif board.board[board.m // 2+2][board.n // 2+2] == 0:
                Player.place_piece(self, board.m // 2+2, board.n // 2+2, game, board)
                print("Rechts von der Mitte")
            elif board.board[board.m // 2-2][board.n // 2-2] == 0:
                Player.place_piece(self, board.m // 2-2, board.n // 2-2, game, board)
                print("Links von der Mitte")
            else:
                row = random.randint(0, 4)
                col = random.randint(0, 4)
                Player.place_piece(self, row, col, game, board) #Parameter die die Rausgehen