import numpy as np
import random
from class_player import *

class TreeBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def make_move(self, game, board):
        try:
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
                move = self.direction(board.board, self.player_number)
                print(move)
                print("Chain")
                return Player.place_piece(self, move[0], move[1], game, board)
        except:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            print("Random")
            return Player.place_piece(self, row, col, game, board)
              
    def direction(self, board, player_number):
        chain = self.get_chain(board, player_number)
        moves_list = []
        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                if value == player_number:
                    if (row_index, col_index+1) in chain:
                        moves_list.append((row_index, col_index+2))
                    elif (row_index, col_index-1) in chain:
                        moves_list.append((row_index, col_index-2))
                    elif (row_index+1, col_index) in chain:
                        moves_list.append((row_index+2, col_index))
                    elif (row_index-1, col_index) in chain:
                        moves_list.append((row_index-2, col_index))
                    elif (row_index+1, col_index+1) in chain:
                        moves_list.append((row_index+2, col_index+2))
                    elif (row_index-1, col_index-1) in chain:
                        moves_list.append((row_index-2, col_index-2))
                    elif (row_index+1, col_index-1) in chain:
                        moves_list.append((row_index+2, col_index-2))
                    elif (row_index-1, col_index+1) in chain:
                        moves_list.append((row_index-2, col_index+2))
                    else:
                        return
        for i, j in moves_list:
            if not 0 <= i < 5 and not 0 <= j < 5: 
                moves_list.remove((i, j))
        return random.choice(moves_list)

    def get_chain(self, board, player_number):
        chain = []
        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                if value == player_number:
                    chain.append((row_index, col_index))
        return chain
            