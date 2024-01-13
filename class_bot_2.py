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
                # weitere Abfrage sinnlos, da nach return nicht mehr weiter gelesen wird
            # elif board.board[board.m // 2+1][board.n // 2+1] == 0:
            #     print("Oben von der Mitte")
            #     return Player.place_piece(self, board.m // 2+1, board.n // 2+1, game, board)
            # elif board.board[board.m // 2-1][board.n // 2-1] == 0:
            #     print("Unten von der Mitte")
            #     return Player.place_piece(self, board.m // 2-1, board.n // 2-1, game, board)         
            # elif board.board[board.m // 2+2][board.n // 2+2] == 0:
            #     print("Rechts von der Mitte")
            #     return Player.place_piece(self, board.m // 2+2, board.n // 2+2, game, board)
            # elif board.board[board.m // 2-2][board.n // 2-2] == 0:
            #     print("Links von der Mitte")
            #     return Player.place_piece(self, board.m // 2-2, board.n // 2-2, game, board)   
            else:
                row = random.randint(0, 4)
                col = random.randint(0, 4)
                return Player.place_piece(self, row, col, game, board) #Parameter die die Rausgehen
            
    # def chain(self, piece):
    #     longeste_chain = str(piece) * (2/self.k)

    #     for row in self.board:
    #         if longeste_chain in ''.join(str(int(e)) for e in row):
    #             return True

    #     for col in self.board.T:
    #         if longeste_chain in ''.join(str(int(e)) for e in col):
    #             return True

    #     for diag in [np.diagonal(self.board, offset) for offset in range(-self.board.shape[0] + self.k, self.board.shape[1] - self.k + 1)]:
    #         if longeste_chain in ''.join(str(int(e)) for e in diag):
    #             return True

    #     for diag in [np.diagonal(np.fliplr(self.board), offset) for offset in range(-self.board.shape[0] + self.k, self.board.shape[1] - self.k + 1)]:
    #         if longeste_chain in ''.join(str(int(e)) for e in diag):
    #             return True

    #     return False
