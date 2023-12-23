
import random
from copy import deepcopy
from class_player import Player

class MonteCarloBot(Player):
    NTRIALS = 3000
    SCORE_CURRENT = 1.0
    SCORE_OTHER = 2.0
    DEP = 4

    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def mc_trial(self, position):
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
            position.board[move[0]][move[1]] = self.player_number
            self.player_number = 2 if self.player_number == 1 else 1
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

    def mc_move(self, position):
        scores = [[0] * position.n for _ in range(position.m)]
        num = 0
        while num < self.NTRIALS:
            clone = deepcopy(position)
            self.mc_trial(clone)
            self.mc_update_scores(scores, clone)
            num += 1

        return self.get_best_move(position, scores)

    def place_piece(self, game, board):
        clone = deepcopy(board)
        move = self.mc_move(clone)
        Player.place_piece(self, move[0], move[1], game, board)