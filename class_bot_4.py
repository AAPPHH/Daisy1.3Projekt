import random
import ray
from copy import deepcopy
from functools import lru_cache
from class_player import Player


class MonteCarloBot(Player):
    NTRIALS = 100000
    SCORE_CURRENT = 1.0
    SCORE_OTHER = 10.0
    DEP = 50

    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        
    @lru_cache(maxsize=None)
    def mc_trial(self, position):
        current_player = self.player_number
        winner = position.is_winner(self.player_number)
        board_full = position.is_full()
        game_over = winner or board_full

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

    def get_best_move(self, position, scores):
        best_square = None
        best_score = float('-inf')
        for square in [(i, j) for i in range(position.m) for j in range(position.n)]:
            r, s = square
            if scores[r][s] > best_score and position.board[r][s] == 0:
                best_square = square
                best_score = scores[r][s]

        if best_square is not None:
            return best_square
        else:
            return random.choice([(i, j) for i in range(position.m) for j in range(position.n) if position.board[i][j] == 0])



    @ray.remote
    def mc_trial_remote(self, position):
        clone = deepcopy(position)
        self.mc_trial(clone)
        return clone

    def mc_move(self, position):
        scores = [[0] * position.n for _ in range(position.m)]
        num = 0

        ray.init()

        futures = [self.mc_trial_remote.remote(self, deepcopy(position)) for _ in range(self.NTRIALS)]
        results = ray.get(futures)

        for clone in results:
            self.mc_update_scores(scores, clone)
            num += 1

        print(f"Computer wählt aus {num} Möglichkeiten.")
        return self.get_best_move(position, scores)
    
    def place_piece(self, game, board):
        print("Computer denkt nach...")
        clone = deepcopy(board)
        move = self.mc_move(clone)
        ray.shutdown()
        self.mc_trial.cache_clear()
        Player.place_piece(self, move[0], move[1], game, board)