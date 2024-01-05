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

        # TreeBot.place_piece(self.current_player, self, self.board) Parameter die reinkommen
        # if self.board.board[self.m // 2][self.n // 2] == 0:  # Zentrum
        #     self.board.board[self.m // 2][self.n // 2] = 2
        # elif self.board[self.m // 2 + 1][self.n // 2] == 0:  # Oben von der Mitte
        #     self.board[self.m // 2 + 1][self.n // 2] = 2
        # elif self.board[self.m // 2 - 1][self.n // 2] == 0:  # Unten von der Mitte
        #     self.board[self.m // 2 - 1][self.n // 2] = 2
        # elif self.board[self.m // 2][self.n // 2 + 1] == 0:  # Rechts von der Mitte
        #     self.board[self.m // 2][self.n // 2 + 1] = 2
        # elif self.board[self.m // 2][self.n // 2 - 1] == 0:  # Links von der Mitte
        #     self.board[self.m // 2][self.n // 2 - 1] = 2
        # else:
            # exceptional_list = [self.m // 2, self.m // 2 + 1, self.m // 2 - 1, self.n // 2, self.n // 2 + 1, self.n // 2 - 1]
            # random_row = random.choice(valid_rows)
            # random_column = random.choice(valid_columns)
            # self.board[random_row][random_column] = 2