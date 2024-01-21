import numpy as np
import random
from class_player import *

class TreeBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.memo = {
            #best starting move
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            #best second move when starting
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 3), (3, 1)]), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 1), (3, 3)]), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 1), (3, 3)]), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 3), (3, 1)]), "KILLER_MOVE"),
            #best third move when starting
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"),
            #best second move when not starting
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 1), (1, 3), (3, 1), (3, 3)]), "KILLER_MOVE"),
            #move that help to kill the TreeBot
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 3), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 1), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 1), "KILLER_MOVE")
        }

    def make_move(self, game, board):
            board_state = str(board.board)
            if board_state in self.memo:
                print("Memoization!")
                move = self.memo[board_state][0]
                best_score = self.memo[board_state][1]
                print(f"Beste Position: {move} mit Score {best_score}")
                return Player.place_piece(self, move[0], move[1], game, board)
            else:
                move = self.direction(board.board, self.player_number)
                return Player.place_piece(self, move[0], move[1], game, board)

    def get_pos(self, board, player_number):
        chain = []
        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                if value == player_number:
                    chain.append((row_index, col_index))
        return chain

    def direction(self, board, player_number):
        chain = self.get_pos(board, player_number)
        moves_list = []
        for row_index, col_index in chain:
            potential_moves = [
                (row_index, col_index + 2),
                (row_index, col_index - 2),
                (row_index + 2, col_index),
                (row_index - 2, col_index),
                (row_index + 2, col_index + 2),
                (row_index - 2, col_index - 2),
                (row_index + 2, col_index - 2),
                (row_index - 2, col_index + 2)
            ]
            for move in potential_moves:
                if (0 <= move[0] < len(board) and 0 <= move[1] < len(board[0]) and
                        board[move[0]][move[1]] == 0 and
                        ((move[0], move[1] - 1) in chain or
                         (move[0], move[1] + 1) in chain or
                         (move[0] - 1, move[1]) in chain or
                         (move[0] + 1, move[1]) in chain or
                         (move[0] - 1, move[1] - 1) in chain or
                         (move[0] + 1, move[1] + 1) in chain or
                         (move[0] - 1, move[1] + 1) in chain or
                         (move[0] + 1, move[1] - 1) in chain)):
                    moves_list.append(move)
        if moves_list:
            return random.choice(moves_list)
        else:
            return self.random_valid_move()

    def random_valid_move(self):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        return (row, col)

    # def make_move(self, game, board):
    #     try:
    #         if board.board[board.m // 2][board.n // 2] == 0:
    #             return Player.place_piece(self, board.m // 2, board.n // 2, game, board)
    #         elif board.board[board.m // 2+1][board.n // 2+1] == 0:
    #             return Player.place_piece(self, board.m // 2+1, board.n // 2+1, game, board)
    #         elif board.board[board.m // 2-1][board.n // 2-1] == 0:
    #             return Player.place_piece(self, board.m // 2-1, board.n // 2-1, game, board)         
    #         elif board.board[board.m // 2+2][board.n // 2+2] == 0:
    #             return Player.place_piece(self, board.m // 2+2, board.n // 2+2, game, board)
    #         elif board.board[board.m // 2-2][board.n // 2-2] == 0:
    #             return Player.place_piece(self, board.m // 2-2, board.n // 2-2, game, board)   
    #         else:
    #             move = self.direction(board.board, self.player_number)
    #             return Player.place_piece(self, move[0], move[1], game, board)
    #     except:
    #         row = random.randint(0, 4)
    #         col = random.randint(0, 4)
    #         return Player.place_piece(self, row, col, game, board)
              
    # def get_pos(self, board, player_number):
    #     chain = []
    #     for row_index, row in enumerate(board):
    #         for col_index, value in enumerate(row):
    #             if value == player_number:
    #                 chain.append((row_index, col_index))
    #     return chain
    
    # def direction(self, board, player_number):
    #     chain = self.get_pos(board, player_number)
    #     moves_list = []

    #     for row_index, col_index in chain:
    #         potential_moves = [
    #             (row_index, col_index + 2),
    #             (row_index, col_index - 2),
    #             (row_index + 2, col_index),
    #             (row_index - 2, col_index),
    #             (row_index + 2, col_index + 2),
    #             (row_index - 2, col_index - 2),
    #             (row_index + 2, col_index - 2),
    #             (row_index - 2, col_index + 2)
    #         ]

    #         for move in potential_moves:
    #             if (0 <= move[0] < len(board) and 0 <= move[1] < len(board[0]) and
    #                     board[move[0]][move[1]] == 0 and
    #                     (move[0], move[1] - 1) in chain or
    #                     (move[0], move[1] + 1) in chain or
    #                     (move[0] - 1, move[1]) in chain or
    #                     (move[0] + 1, move[1]) in chain or
    #                     (move[0] - 1, move[1] - 1) in chain or
    #                     (move[0] + 1, move[1] + 1) in chain or
    #                     (move[0] - 1, move[1] + 1) in chain or
    #                     (move[0] + 1, move[1] - 1) in chain):
    #                 moves_list.append(move)

    #     if moves_list:
    #         return random.choice(moves_list)   
    #     else:     
    #         row = random.randint(0, board.m)
    #         col = random.randint(0, board.n)
    #         return (row, col)
  # def direction(self, board, player_number):
    #     chain = self.get_pos(board, player_number)
    #     moves_list = []
    #     for row_index, row in enumerate(board):
    #         for col_index, value in enumerate(row):
    #             if value == player_number:
    #                 if (row_index, col_index+1) in chain:
    #                     moves_list.append((row_index, col_index+2))
    #                 elif (row_index, col_index-1) in chain:
    #                     moves_list.append((row_index, col_index-2))
    #                 elif (row_index+1, col_index) in chain:
    #                     moves_list.append((row_index+2, col_index))
    #                 elif (row_index-1, col_index) in chain:
    #                     moves_list.append((row_index-2, col_index))
    #                 elif (row_index+1, col_index+1) in chain:
    #                     moves_list.append((row_index+2, col_index+2))
    #                 elif (row_index-1, col_index-1) in chain:
    #                     moves_list.append((row_index-2, col_index-2))
    #                 elif (row_index+1, col_index-1) in chain:
    #                     moves_list.append((row_index+2, col_index-2))
    #                 elif (row_index-1, col_index+1) in chain:
    #                     moves_list.append((row_index-2, col_index+2))
    #                 else:
    #                     return
    #     for i, j in moves_list:
    #         if not (0 <= i < 5 and 0 <= j < 5):
    #             moves_list.remove((i, j))
    #     return random.choice(moves_list)