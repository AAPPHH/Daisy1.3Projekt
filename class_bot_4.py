
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
        empty_squares = position.get_empty_squares()
        move = empty_squares[random.randrange(len(empty_squares))]
        depth = self.DEP
        while not position.is_gameover(move, position.get_enemy(self.player_number)) and depth != 0:
            empty_squares = position.get_empty_squares()
            move = empty_squares[random.randrange(len(empty_squares))]
            position.make_move(move, self.player_number)
            self.player_number = position.get_enemy(self.player_number)
            depth -= 1

    def mc_update_scores(self, scores, position):
        winner = position.winner
        if winner == 0:
            return
        coef = 1
        if self.player_number != winner:
            coef = -1
        for row in range(position.size):
            for col in range(position.size):
                if position.board[row][col] == self.player_number:
                    scores[row][col] += coef * self.SCORE_CURRENT
                elif position.board[row][col] != 0:
                    scores[row][col] -= coef * self.SCORE_OTHER

    def get_best_move(self, position, scores):
        best_square = position.get_empty_squares()[0]
        r, s = best_square // position.size, best_square % position.size
        best_score = scores[r][s]
        for square in position.get_empty_squares():
            r, s = square // position.size, square % position.size
            if scores[r][s] > best_score:
                best_square = square
                best_score = scores[r][s]
        out = []
        for square in position.get_empty_squares():
            r, s = square // position.size, square % position.size
            if scores[r][s] == best_score:
                out.append(square)
        return out[random.randrange(len(out))]

    def mc_move(self, position):
        scores = [[0] * position.size for _ in range(position.size)]
        num = 0
        while num < self.NTRIALS:
            clone = deepcopy(position)
            self.mc_trial(clone)
            self.mc_update_scores(scores, clone)
            num += 1
        print(scores)
        return self.get_best_move(position, scores)

    def place_piece(self, game, board):
        clone = deepcopy(board)
        move = self.mc_move(clone)
        Player.place_piece(self, move[0], move[1], game, board)
