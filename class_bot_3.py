import time
import numpy as np
from copy import deepcopy
from class_player import *
import random
import pickle

class MinimaxBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.use_minimax = False
        self.depth = 5
        self.new_memo = {}
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
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 1), "KILLER_MOVE"), #3.1
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
        board_state = str(board.array)
        if board_state in self.memo:
            print("Memoization!")
            move = self.memo[board_state][0]
            best_score = self.memo[board_state][1]
            print(f"Beste Position: {move} mit Score {best_score}")
            return Player.make_move(self, move[0], move[1], game, board)
        if self.use_minimax:
            move = self.minimax(game, board, self.depth, self.player_number)
        else:
            move = self.alphabeta_bot(game, board, self.player_number)
        if move is not None:
            self.new_memo[board_state] = (move)
        return Player.make_move(self, move[0], move[1], game, board)

    def get_empty_squares(self, board):
        empty_squares = []
        for row_index, row in enumerate(board.array):
            for col_index, value in enumerate(row):
                if value == 0:  
                    empty_squares.append((row_index, col_index))
        return empty_squares
    
    def get_enemy(self):
        if self.player_number == 1:
            return 2
        else:
            return 1
        
    def switch_player(self, player_number):
        if player_number == 1:
            return 2
        else:
            return 1
        
    def perform_move(self, board, move, player_number):
        board_copy = deepcopy(board)
        row, col = move
        board_copy.array[row][col] = player_number
        return board_copy
    
    def evaluate(self, pos, dep):
        if pos.is_winner(self.player_number):
            return 10 * (dep+1)
        elif pos.is_winner(self.get_enemy()):
            return -10 * (dep+1)
        return 0
    
    def minimax(self, game, board, depth, player_number):
        moves = self.get_empty_squares(board)
        best_move = None
        best_score = float('-inf')
        for move in moves:
            clone = self.perform_move(board, move, player_number)
            score = self.min_play(game, clone, depth-1, move, player_number) 
            print(f"Move: {clone.array}, Score: {score}")
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

    def alphabeta(self, position, player_number, alpha, beta, depth):
        if position.is_winner(player_number) or position.is_full() or depth == 0:
            return self.evaluate(position, depth)
        for move in self.get_empty_squares(position):
            clone = self.perform_move(position, move, player_number)
            val = self.alphabeta(clone, self.switch_player(player_number), alpha, beta, depth-1)
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

    def alphabeta_bot(self, game, position, player_number, time_limit=180.0):
        start_time = time.time()
        choices = []
        a = 0
        for move in self.get_empty_squares(position):
            if time.time() - start_time > time_limit:
                print("Time limit exceeded")
                break
            clone = self.perform_move(position, move, player_number)
            val = self.alphabeta(clone, self.get_enemy(),-100 , 100, self.depth)
            if val > a:
                a = val
                choices = [move]
            elif val == a:
                print(a)
                choices.append(move)
            if a == 1 or time.time() - start_time > time_limit:
                print("Time limit exceeded")
                break
        return random.choice(choices) if choices else self.minimax(game, position, self.depth, self.player_number)
    
    def load_state(self):
        try:
            with open('bot_3_memo', 'rb') as f:
                self.memo = pickle.load(f)
        except FileNotFoundError:
            pass

    def save_state(self):
        self.memo.update(self.new_memo)
        with open('bot_3_memo.pkl', 'wb') as f:
            pickle.dump(self.memo, f)
        print("Zustand gespeichert.")