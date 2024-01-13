import numpy as np
from copy import deepcopy
from class_player import *
import random

class MinimaxBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.use_minimax = True
        self.depth = 4

    def make_move(self, game, board):
        if self.use_minimax:
            move = self.minimax(game, board, self.depth, self.player_number)
        else:
            move =self.alphabeta_bot(game, board, self.player_number) 
        Player.place_piece(self, move[0], move[1], game, board)

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
        
    def perform_move(self, board, move, player):
        #print(board.board)
        board_copy = deepcopy(board)
        row, col = move
        board_copy.board[row][col] = player
        #print(board_copy.board)
        return board_copy
    
    def minimax(self, game, board, depth, player):
        moves = self.get_empty_squares(board)
        best_move = moves[0]
        best_score = float('-inf')
        for move in moves:
            clone = self.perform_move(board, move, player)
            score = self.min_play(game, clone, depth-1, move, player) 
            print(f"Move: {clone.board}, Score: {score}")
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def min_play(self, game, position, depth, move, player):
        if position.is_winner(player) or position.is_full() or depth == 0:
            return self.evaluate(position, player)
        moves = self.get_empty_squares(position)
        player = self.get_enemy()
        best_score = float('inf')
        for move in moves:
            clone = deepcopy(position)
            self.perform_move(clone, move, player)
            score = self.max_play(game, clone, depth-1, move, player)
            print(f"Move: {clone.board}, Score: {score}")
            if score < best_score:
                best_move = move
                best_score = score
        return best_score

    def max_play(self, game, position, depth, lastmove, player):
        if position.is_winner(player) or position.is_full() or depth == 0:
            return self.evaluate(position, depth)
        moves = self.get_empty_squares(position)
        player = self.get_enemy()
        best_score = float('-inf')
        for move in moves:
            clone = deepcopy(position)
            self.perform_move(clone, move, player)
            score = self.min_play(game, clone, depth-1, move, player)
            print(f"Move: {clone.board}, Score: {score}")
            if score > best_score:
                best_move = move
                best_score = score
        return best_score

    def evaluate(self, pos, dep):
        if pos.is_winner(self.player_number) == True:
            return 10 * (dep+1)
        elif pos.is_winner(self.player_number) == False:
            return -10 * (dep+1)
        return 0

    def alphabeta(self, position, lastmove, player, alpha, beta, depth):
        #print(f"{position.board}")
        if position.is_winner(player) or position.is_full() or depth == 0:
            return self.evaluate(position, depth)
        for move in self.get_empty_squares(position):
            clone = deepcopy(position)
            self.perform_move(clone, move, player)
            #print(f'Board state after move:{clone.board}')
            val = self.alphabeta(clone, move, self.get_enemy(), alpha, beta, depth-1)
            if player == self.player_number:
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == self.player_number:
            return alpha
        else:
            return beta

    def alphabeta_bot(self, game, position, player):
        a = -2
        choices = []
        if len(self.get_empty_squares(position)) == position.board.size ** 2:
            return position.board.size ** 2 // 2 + 1

        for depth in range(1, self.depth + 1):
            a = -2
            new_choices = []
            for move in self.get_empty_squares(position):
                clone = deepcopy(position)
                self.perform_move(clone, move, player)
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

