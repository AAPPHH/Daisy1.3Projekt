import numpy as np
from copy import deepcopy
from class_player import *
import random

class MinimaxBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.use_minimax = True
        self.depth = 4
        self.memo = {
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,2), "KILLER_MOVE"),

            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(4,0)]), "KILLER_MOVE"),

            '[[2. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((4, 4), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 2.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((0, 0), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [2. 0. 0. 0. 0.]]': ((0, 0), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 2.]]': ((0, 0), "KILLER_MOVE"),

            '[[2. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [2. 0. 0. 0. 0.]]': ((4, 4), "KILLER_MOVE"),
            '[[2. 0. 0. 0. 2.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((4, 4), "KILLER_MOVE")
        }

    def make_move(self, game, board):
        board_state = str(board.board)
        if board_state in self.memo:
            print("Memoization!")
            move = self.memo[board_state][0]
            best_score = self.memo[board_state][1]
            print(f"Beste Position: {move} mit Score {best_score}")
            return Player.place_piece(self, move[0], move[1], game, board)
        if self.use_minimax:
            move = self.minimax(game, board, self.depth, self.player_number)
        else:
            move = self.alphabeta_bot(game, board, self.player_number) 
        return Player.place_piece(self, move[0], move[1], game, board)

    def get_empty_squares(self, board):
        empty_squares = []
        for row_index, row in enumerate(board.board):
            for col_index, value in enumerate(row):
                if value == 0:  
                    empty_squares.append((row_index, col_index))
        return empty_squares
    
    def get_enemy(self):
        if self.player_number == 1:
            return 2
        else:
            return 1
        
    def perform_move(self, board, move, player_number):
        board_copy = deepcopy(board)
        row, col = move
        board_copy.board[row][col] = player_number
        return board_copy
    
    def minimax(self, game, board, depth, player_number):
        moves = self.get_empty_squares(board)
        best_move = None
        best_score = float('-inf')
        for move in moves:
            clone = self.perform_move(board, move, player_number)
            score = self.min_play(game, clone, depth-1, move, player_number) 
            print(f"Move: {clone.board}, Score: {score}")
            if score > best_score:
                best_score = score
                best_move = move
        return best_move 

    def min_play(self, game, position, depth, move, player_number):
        if position.is_winner(player_number) or position.is_full() or depth == 0:
            return self.evaluate(position, depth)
        moves = self.get_empty_squares(position)
        player_number_enemy = self.get_enemy()
        best_score = float('inf')
        for move in moves:
            clone = self.perform_move(position, move, player_number_enemy)
            score = self.max_play(game, clone, depth-1, move, player_number)
            #print(f"Move: {clone.board}, Score: {score}")
            if score < best_score:
                best_move = move
                best_score = score
        return best_score

    def max_play(self, game, position, depth, lastmove, player_number):
        if position.is_winner(player_number) or position.is_full() or depth == 0:
            return self.evaluate(position, depth)
        moves = self.get_empty_squares(position)
        best_score = float('-inf')
        for move in moves:
            clone = self.perform_move(position, move, player_number)
            score = self.min_play(game, clone, depth-1, move, player_number)
            #print(f"Move: {clone.board}, Score: {score}")
            if score > best_score:
                best_move = move
                best_score = score
        return best_score

    def evaluate(self, pos, dep):
        if pos.is_winner(self.player_number):
            return 10 * (dep+1)
        elif pos.is_winner(self.get_enemy()):
            return -10 * (dep+1)
        return 0

    def alphabeta(self, position, lastmove, player_number, alpha, beta, depth):
        if position.is_winner(player_number) or position.is_full() or depth == 0:
            return self.evaluate(position, depth)
        for move in self.get_empty_squares(position):
            clone = deepcopy(position)
            self.perform_move(clone, move, player_number)
            val = self.alphabeta(clone, move, self.get_enemy(), alpha, beta, depth-1)
            if player_number == self.player_number:
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player_number == self.player_number:
            return alpha
        else:
            return beta

    def alphabeta_bot(self, game, position, player_number):
        choices = []
        if len(self.get_empty_squares(position)) == position.board.size ** 2:
            return position.board.size ** 2 // 2 + 1
        for depth in range(1, self.depth + 1):
            a = -2
            new_choices = []
            for move in self.get_empty_squares(position):
                clone = deepcopy(position)
                self.perform_move(clone, move, player_number)
                val = self.alphabeta(clone, move, self.get_enemy(), -2, 2, depth)
                if val > a:
                    a = val
                    new_choices = [move]
                elif val == a:
                    new_choices.append(move)
            choices = new_choices
            if a == 1:
                break
        return random.choice(choices)

