import random
import ray
import os
from copy import deepcopy
from functools import lru_cache
import pickle
from class_player import *

class MonteCarloBot(Player):
    NTRIALS = 250000
    SCORE_CURRENT = 1.0
    SCORE_OTHER = 10.0
    DEP = 50

    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.memo = {}
        self.load_state() 
        
    def mc_trial(self, position):
        current_player = self.player_number
        winner = position.is_winner(self.player_number)
        board_full = position.is_full()
        game_over = winner or board_full
        #print(f"Game Over: {game_over}")
        empty_squares = [(i, j) for i in range(position.m) for j in range(position.n) if position.board[i][j] == 0]
        if not empty_squares:
            return

        move = empty_squares[random.randrange(len(empty_squares))]
        depth = self.DEP
        while not game_over and depth != 0:
            winner = position.is_winner(self.player_number)
            board_full = position.is_full()
            game_over = winner or board_full

            if game_over:
                break

            empty_squares = [(i, j) for i in range(position.m) for j in range(position.n) if position.board[i][j] == 0]
            if not empty_squares:
                break

            move = empty_squares[random.randrange(len(empty_squares))]
            position.board[move[0]][move[1]] = current_player
            current_player = 2 if current_player == 1 else 1
            depth -= 1

    def mc_update_scores(self, scores, position):
        # print(position.board)
        winner = position.is_winner
        if winner == 0:
            return
        coef = 1
        if self.player_number != winner:
            coef = -1
        for row in range(position.m):
            for col in range(position.n):
                if position.board[row][col] == self.player_number:
                    scores[row][col] += coef * self.SCORE_CURRENT
                elif position.board[row][col] != 0:
                    scores[row][col] -= coef * self.SCORE_OTHER

    # def chain(self, piece):
    #     longeste_chain = str(piece) * (2/self.k)

    #     for row in self.board:
    #         if longeste_chain in ''.join(str(int(e)) for e in row):
    #             return True

    #     for col in self.board.T:
    #         if longeste_chain in ''.join(str(int(e)) for e in col):
    #             return True

    #     for diag in [np.diagonal(self.board, offset) for offset in range(-self.board.shape[0] + self.k, self.board.shape[1] - self.k + 1)]:
    #         if longeste_chain in ''.join(str(int(e)) for e in diag):
    #             return True

    #     for diag in [np.diagonal(np.fliplr(self.board), offset) for offset in range(-self.board.shape[0] + self.k, self.board.shape[1] - self.k + 1)]:
    #         if longeste_chain in ''.join(str(int(e)) for e in diag):
    #             return True

    #     return False

    # def mc_update_scores(self, scores, position):
    #     longest_chain = position.chain(self.player_number)
    #     coef = 1
    #     if longest_chain:
    #         coef = -1
    #     for row in range(position.m):
    #         for col in range(position.n):
    #             if position.board[row][col] == self.player_number:
    #                 scores[row][col] += coef * self.SCORE_CURRENT
    #             elif position.board[row][col] != 0:
    #                 scores[row][col] -= coef * self.SCORE_OTHER
            
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
    def mc_trial_remote(self, position):
        clone = deepcopy(position)
        self.mc_trial(clone)
        return clone
    
    @lru_cache(maxsize=None)
    def mc_move(self, position):
        board_state = str(position.board)

        if board_state in self.memo:
            print("Memoization!")
            return self.get_best_move(self.memo[board_state][0], self.memo[board_state][1])
        scores = [[0] * position.n for _ in range(position.m)]
        num = 0
        # while num < self.NTRIALS:
        #     clone = deepcopy(position)
        #     self.mc_trial(clone)
        #     self.mc_update_scores(scores, clone)
        #     num += 1

        # print(f"Computer wählt aus {num} Möglichkeiten.")
        # return self.get_best_move(position, scores)
        ray.init(num_cpus=os.cpu_count())

        futures = [self.mc_trial_remote.remote(self, deepcopy(position)) for _ in range(self.NTRIALS)]
        results = ray.get(futures)
        # print(results)
        for clone in results:
            self.mc_update_scores(scores, clone)
            num += 1

        print(f"Computer wählt aus {num} Möglichkeiten.")
        return self.get_best_move(position, scores)
    
    def load_state(self):
        try:
            with open('bot_state.pkl', 'rb') as f:
                self.memo = pickle.load(f)
        except FileNotFoundError:
            self.memo = {}

    def save_state(self):
        with open('bot_state.pkl', 'wb') as f:
            pickle.dump(self.memo, f)
    
    def place_piece(self, game, board):
        print("Computer denkt nach...")
        move = self.mc_move(board)
        ray.shutdown()
        self.save_state()
        self.mc_move.cache_clear()
        return Player.place_piece(self, move[0], move[1], game, board)