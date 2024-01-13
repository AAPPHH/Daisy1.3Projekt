import random
import secrets
import ray
import os
from copy import deepcopy
import pickle
from class_player import *


class MonteCarloBot(Player):
    NTRIALS = 250000
    SCORE_CURRENT = 1.0
    SCORE_OTHER = 10.0
    DEP = 4

    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.load_state() 
        self.memo = {
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2,2), "KILLER_MOVE"),

            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': (random.choice([(4,0)]), "KILLER_MOVE"),

            '[[2. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((4, 4), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 2.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((0, 0), "KILLER_MOVE"),
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [2. 0. 0. 0. 0.]]': ((0, 0), "KILLER_MOVE"),#
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 2.]]': ((0, 0), "KILLER_MOVE"),

            '[[2. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [2. 0. 0. 0. 0.]]': ((4, 4), "KILLER_MOVE"),
            '[[2. 0. 0. 0. 2.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((4, 4), "KILLER_MOVE")
        }
    def mc_trial(self, position, depth):
        current_player = self.player_number
        winner = position.is_winner(self.player_number)
        board_full = position.is_full()
        game_over = winner or board_full
        empty_squares = [(i, j) for i in range(position.m) for j in range(position.n) if position.board[i][j] == 0]
        if not empty_squares:
            return
        while not game_over and depth != 0:
            winner = position.is_winner(self.player_number)
            board_full = position.is_full()
            game_over = winner or board_full
            if game_over:
                break
            empty_squares = [(i, j) for i in range(position.m) for j in range(position.n) if position.board[i][j] == 0]
            if not empty_squares:
                break
            move = empty_squares[secrets.choice(range(len(empty_squares)))]
            position.board[move[0]][move[1]] = current_player
            current_player = 2 if current_player == 1 else 1
            depth -= 1

    def mc_update_scores(self, scores, position_tupel):
        position, depth = position_tupel
        move =  [(i, j) for i in range(position.m) for j in range(position.n) if position.board[i][j] == 0]
        dep = len(move)
        winner = position.is_winner
        if winner == 0:
            return
        coef = 1
        if self.player_number != winner:
            coef = -1
        for row in range(position.m):
            for col in range(position.n):
                if position.board[row][col] == self.player_number:
                    scores[row][col] += coef * self.SCORE_CURRENT * dep
                elif position.board[row][col] != 0:
                    scores[row][col] -= coef * self.SCORE_OTHER * dep
        
    def get_best_move(self, position, scores):
        best_square = None
        best_score = float('-inf')
        board_state = str(position.board)
        for square in [(i, j) for i in range(position.m) for j in range(position.n)]:
            r, s = square
            if scores[r][s] > best_score and position.board[r][s] == 0:
                best_square = square
                best_score = scores[r][s]
                print(f"Beste Position: {best_square} mit Score {best_score}")
        if best_square is not None:
            self.memo[board_state] = (best_square, best_score)
            return best_square
        else:
            print("Keine beste Position gefunden.")
            return random.choice([(i, j) for i in range(position.m) for j in range(position.n) if position.board[i][j] == 0])

    @ray.remote
    def mc_trial_remote(self, position, depth):
        clone = deepcopy(position)
        dep = deepcopy(depth)
        self.mc_trial(clone, dep)
        return clone, dep
    
    def mc_move(self, position):
        board_state = str(position.board)
        if board_state in self.memo:
            print("Memoization!")
            best_square = self.memo[board_state][0]
            best_score = self.memo[board_state][1]
            print(f"Beste Position: {best_square} mit Score {best_score}")
            return best_square
        scores = [[0] * position.n for _ in range(position.m)]
        ray.init(num_cpus=os.cpu_count())
        futures = [self.mc_trial_remote.remote(self, position, self.DEP) for _ in range(self.NTRIALS)]
        results = ray.get(futures)
        for clone in results:
            self.mc_update_scores(scores, clone)
        print(f"Computer wählt aus {len(results)} Möglichkeiten.")
        return self.get_best_move(position, scores)
    
    def load_state(self):
        try:
            with open('bot_state.pkl', 'rb') as f:
                self.memo = pickle.load(f)
        except FileNotFoundError:
            print("Kein gespeicherter Zustand gefunden.")

    def save_state(self):
        with open('bot_state.pkl', 'wb') as f:
            pickle.dump(self.memo, f)
    
    def place_piece(self, game, board):
        print("Computer denkt nach...")
        move = self.mc_move(board)
        ray.shutdown()
        self.save_state()
        return Player.place_piece(self, move[0], move[1], game, board)