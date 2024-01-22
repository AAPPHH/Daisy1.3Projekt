import numpy as np
import random
from class_player import *

class TreeBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.memo = {
            #best move 1 Player_Number=1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,  2), "KILLER_MOVE"),
            #best move 2 Player_Number=2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 1), (1, 3), (3, 1), (3, 3)]), "KILLER_MOVE"),
            #best move 3 Player_Number=1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 3), (3, 1)]), "KILLER_MOVE"), #1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 1), (3, 3)]), "KILLER_MOVE"), #2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 1), (3, 3)]), "KILLER_MOVE"), #3
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(1, 3), (3, 1)]), "KILLER_MOVE"), #4
            #best move 4 Player_Number=2
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 1), "KILLER_MOVE"), #1.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 3), "KILLER_MOVE"), #1.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 3), "KILLER_MOVE"), #2.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 1), "KILLER_MOVE"), #2.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 3), "KILLER_MOVE"), #3.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 3), "KILLER_MOVE"), #3.2 
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 1), "KILLER_MOVE"), #4.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 3), "KILLER_MOVE"), #4.2
            #best move 5 Player_Number=1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"), #1.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #1.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #2.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #2.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #3.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #3.2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #4.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #4.2
            #best move 6 Player_Number=2
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 1. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #1.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #1.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 1. 1. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"), #2.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #2.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #3.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 1. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"), #3.2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #4.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 1. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE")  #4.2
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