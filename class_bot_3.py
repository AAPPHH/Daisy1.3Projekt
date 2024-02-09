import time
import numpy as np
from copy import deepcopy
from class_player import *
import pickle

class MinimaxBot(Player):
    """
    Alpha-Beta Pruning Bot with decision table and Minimax backup
    """
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.use_minimax = False
        self.depth = 6

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
        return Player.make_move(self, move[0], move[1], game, board)

    def get_empty_squares(self, board):
        """
        Returns a list of empty squares on the board
        """
        empty_squares = []
        for row_index, row in enumerate(board.array):
            for col_index, value in enumerate(row):
                if value == 0:  
                    empty_squares.append((row_index, col_index))

        empty_squares.sort(key=lambda pos: self.manhattan_distance_to_center(pos[0], pos[1], board))
        return empty_squares
        
    def manhattan_distance_to_center(self, row, col, board):
        center_row, center_col = len(board.array) // 2, len(board.array[0]) // 2
        return abs(row - center_row) + abs(col - center_col)
    
    def get_enemy(self):
        """
        Returns the player number of the enemy based on the player number of the bot
        """
        if self.player_number == 1:
            return 2
        else:
            return 1
        
    def switch_player(self, player_number):
        """
        Returns the player number of the enemy
        """
        if player_number == 1:
            return 2
        else:
            return 1
        
    def perform_move(self, board, move, player_number):
        """
        Returns a new board with the move performed
        """
        board_copy = deepcopy(board)
        row, col = move
        board_copy.array[row][col] = player_number
        return board_copy
    
    def evaluate(self, pos, dep):
        """
        Returns a score for the position
        """
        if pos.is_winner(self.player_number):
            return 10 * (dep+1)
        elif pos.is_winner(self.get_enemy()):
            return -10 * (dep+1)
        return 0
    
    def alphabeta(self, position, player_number, alpha, beta, depth):
        """
        Returns the best score for the current player and prunes the tree
        works completely recursive
        """
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
        """
        Returns the best move for the current player
        """
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
            if a == self.depth*10 or time.time() - start_time > time_limit:
                break
        return random.choice(choices) if choices else self.minimax(game, position, self.depth, self.player_number)