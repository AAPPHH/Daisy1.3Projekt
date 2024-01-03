import numpy as np
import ray
from copy import deepcopy
from class_player import *
import random

class MinimaxBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.use_minimax = True  # Setzen Sie dies auf False, um Alpha-Beta-Pruning zu verwenden

    # Hauptfunktion, um einen Zug zu machen
    def make_move(self, game, board):
        if self.use_minimax:
            move = self.minimax(game, board, 5, self.player_number)
        else:
            move = self.alphabeta_bot(board, self.player_number)
        Player.place_piece(self, move[0], move[1], game, board)

    def get_empty_squares(self, board):
        empty_squares = []
        for row_index, row in enumerate(board.board):  # Zugriff auf das NumPy-Array innerhalb des Board-Objekts
            for col_index, value in enumerate(row):
                if value == 0:  # Annahme: 0 repräsentiert ein leeres Feld
                    empty_squares.append((row_index, col_index))
        return empty_squares
    
    def get_enemy(self):
        if self.player_number == 1:
            return 2
        else:
            return 1
        
    def perform_move(self, board, move, player):
        # Erstellt eine Kopie des Bretts und führt darauf einen hypothetischen Zug aus
        board_copy = deepcopy(board)
        row, col = move
        board_copy.board[row][col] = player  # Setzt den Spielerwert an der gewählten Position auf dem internen Array
        return board_copy
    
    def minimax(self, game, board, depth, player):
        moves = self.get_empty_squares(board)
        best_move = moves[0]
        best_score = float('-inf')

        for move in moves:
            clone = self.perform_move(board, move, player)
            score = self.min_play(game, clone, depth-1, move, player)  # Pass the game object here
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def min_play(self, game, position, depth, move, player):
        if position.is_winner(player) or position.is_full() or depth == 0:  # Call is_winner on the game object
            return self.evaluate(position, player)
        moves = self.get_empty_squares(position)
        player = self.get_enemy()
        best_score = float('inf')
        print(best_score)
        for move in moves:
            clone = deepcopy(position)
            self.perform_move(clone, move, player)
            score = self.max_play(game, clone, depth-1, move, player)
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
            if score > best_score:
                best_move = move
                best_score = score
        return best_score

    def evaluate(self, pos, dep):
        cur_player = self.player_number
        if pos.is_winner == cur_player:
            return 10 * (dep+1)
        elif pos.is_winner == cur_player * (-1):
            return -10 * (dep+1)
        return 0

    # Alpha-Beta-Pruning
    def alphabeta(self, position, lastmove, player, alpha, beta, depth):
        if position.is_gameover(lastmove, position.get_enemy(player)) or depth == 0:
            cur_player = self.player_number
            if cur_player == -1:
                return position.winner * (-1)
            elif cur_player == 1:
                return position.winner
            return 0
        for move in position.get_empty_squares():
            clone = deepcopy(position)
            clone.make_move(move, player)
            val = self.alphabeta(clone, move, position.get_enemy(player), alpha, beta, depth-1)
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

    def alphabeta_bot(self, position, player):
        a = -2
        choices = []
        if len(position.get_empty_squares()) == position.size ** 2: # bester erster Zug
            return position.size ** 2 // 2 + 1
        for move in position.get_empty_squares():
            clone = deepcopy(position)
            clone.make_move(move, player)
            val = self.alphabeta(clone, move, position.get_enemy(player), -2, 2, 4)
            if val > a:
                a = val
                choices = [move]
            elif val == a:
                choices.append(move)
        return random.choice(choices)
