import random
import ray
import os
from copy import deepcopy
import pickle
from class_player import *

class MonteCarloBot(Player):
    """
    Monte Carlo Bot with decision table and memoization.
    """
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.NTRIALS = 250000
        self.SCORE_CURRENT = 1.0
        self.SCORE_OTHER = 1.0
        self.DEP = 25
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
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 3), "KILLER_MOVE"), #3.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 1), "KILLER_MOVE"), #3.2  
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 1), "KILLER_MOVE"), #4.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 3), "KILLER_MOVE"), #4.2
            #best move 5 Player_Number=1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"), #1.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #1.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #2.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #2.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #3.1
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"), #3.2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #4.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #4.2
            #best move 6 Player_Number=2
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 1. 1. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #1.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #1.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 1. 1. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE"), #2.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 1. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((3, 2), "KILLER_MOVE"), #2.2
            '[[0. 0. 0. 0. 0.]\n [0. 1. 0. 0. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #3.1
            '[[0. 0. 0. 0. 0.]\n [0. 2. 0. 0. 0.]\n [0. 1. 1. 0. 0.]\n [0. 2. 0. 1. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 3), "KILLER_MOVE"), #3.2
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 1. 0.]\n [0. 0. 1. 0. 0.]\n [0. 2. 1. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((1, 2), "KILLER_MOVE"), #4.1
            '[[0. 0. 0. 0. 0.]\n [0. 0. 0. 2. 0.]\n [0. 0. 1. 1. 0.]\n [0. 1. 0. 2. 0.]\n [0. 0. 0. 0. 0.]]': ((2, 1), "KILLER_MOVE")  #4.2
        }

    def mc_trial(self, position, depth):
        """
        Plays a game starting with the given position, alternating between players,
        by making random moves. Makes inplace changes to position.
        """
        current_player = self.player_number
        winner = position.is_winner(self.player_number)
        board_full = position.is_full()
        game_over = winner or board_full
        empty_squares = [(i, j) for i in range(position.m) for j in range(position.n) if position.array[i][j] == 0]
        if not empty_squares:
            return
        while not game_over and depth != 0:
            winner = position.is_winner(self.player_number)
            board_full = position.is_full()
            game_over = winner or board_full
            if game_over:
                break
            empty_squares = [(i, j) for i in range(position.m) for j in range(position.n) if position.array[i][j] == 0]
            if not empty_squares:
                break
            move = empty_squares[random.randrange(len(empty_squares))]
            position.array[move[0]][move[1]] = current_player
            current_player = 2 if current_player == 1 else 1
            depth -= 1

    def mc_update_scores(self, scores, position):
        """
        This function takes a grid of scores (a list of lists)
        """
        move =  [(i, j) for i in range(position.m) for j in range(position.n) if position.array[i][j] == 0]
        dep = len(move)
        winner = position.is_winner
        if winner == 0:
            return
        coef = 1
        if self.player_number != winner:
            coef = -1
        for row in range(position.m):
            for col in range(position.n):
                if position.array[row][col] == self.player_number:
                    scores[row][col] += coef * self.SCORE_CURRENT * dep#**2
                elif position.array[row][col] != 0:
                    scores[row][col] -= coef * self.SCORE_OTHER * dep#**2
        
    def get_best_move(self, position, scores):
        """
        Find all of the empty squares with the maximum score
        or randomly return one of them as a (row, column) tuple.
        """
        best_square = None
        best_score = float('-inf')
        board_state = str(position.array)
        for square in [(i, j) for i in range(position.m) for j in range(position.n)]:
            r, s = square
            if scores[r][s] > best_score and position.array[r][s] == 0:
                best_square = square
                best_score = scores[r][s]
                print(f"Beste Position: {best_square} mit Score {best_score}")
        if best_square is not None:
            self.new_memo[board_state] = (best_square, best_score)
            return best_square
        else:
            print("Keine beste Position gefunden.")
            return random.choice([(i, j) for i in range(position.m) for j in range(position.n) if position.array[i][j] == 0])

    @ray.remote
    def mc_trial_remote(self, position, depth):
        """
        Ray remote for mc_trial inplace changes.
        """
        clone = deepcopy(position)
        dep = deepcopy(depth)
        self.mc_trial(clone, dep)
        return clone
    
    def mc_move(self, position):
        """
        This method checks all if there is allready a best move for the current board state
        otherwise it will run the monte carlo simulation.
        """
        board_state = str(position.array)
        if board_state in self.memo:
            print("Memoization!")
            best_square = self.memo[board_state][0]
            best_score = self.memo[board_state][1]
            print(f"Beste Position: {best_square} mit Score {best_score}")
            return best_square
        if board_state in self.new_memo:
            print("Memoization!")
            best_square = self.new_memo[board_state][0]
            best_score = self.new_memo[board_state][1]
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
    
    def make_move(self, game, board):
        print("Computer denkt nach...")
        self.load_state()
        move = self.mc_move(board)
        ray.shutdown()
        return Player.make_move(self, move[0], move[1], game, board)
    
    def load_state(self):
        """
        Loads the memoization dictionary from a file.
        """
        try:
            with open('bot_4_memo', 'rb') as f:
                self.memo = pickle.load(f)
        except FileNotFoundError:
            print("Kein gespeicherter Zustand gefunden.")

    def save_state(self):
        """
        Saves the memoization dictionary to a file.
        """
        self.memo.update(self.new_memo)
        with open('Bot_4_memo.pkl', 'wb') as f:
            pickle.dump(self.memo, f)
        print("Zustand gespeichert.")