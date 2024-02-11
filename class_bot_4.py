import ray
import os
from copy import deepcopy
import pickle
from class_player import *
from Decision_table import *

class MonteCarloBot(Player):
    """
    Monte Carlo Bot with decision table and memoization.
    if the board state is in the decision table use killer move
    else use Monte Carlo simulation
    """
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.NTRIALS = 250000
        self.SCORE_CURRENT = 1.0
        self.SCORE_OTHER = 2.0
        self.DEP = 10
        self.memo = decision_table
        self.new_memo = {}

    def mc_trial(self, temp_board, depth):
        """
        Plays a game starting with the given position, alternating between players,
        by making random moves. Makes inplace changes to board_temp.
        """
        current_player = self.player_number
        winner = temp_board.is_winner(self.player_number)
        board_full = temp_board.is_full()
        game_over = winner or board_full
        empty_squares = [(i, j) for i in range(temp_board.m) for j in range(temp_board.n) if temp_board.array[i][j] == 0]
        if not empty_squares:
            return
        while not game_over and depth != 0:
            winner = temp_board.is_winner(self.player_number)
            board_full = temp_board.is_full()
            game_over = winner or board_full
            if game_over:
                break
            empty_squares = [(i, j) for i in range(temp_board.m) for j in range(temp_board.n) if temp_board.array[i][j] == 0]
            if not empty_squares:
                break
            move = empty_squares[random.randrange(len(empty_squares))]
            temp_board.array[move[0]][move[1]] = current_player
            current_player = 2 if current_player == 1 else 1
            depth -= 1

    def mc_update_scores(self, scores, temp_board):
        """
        This function takes a grid of scores (a list of lists)
        """
        move = [(i, j) for i in range(temp_board.m) for j in range(temp_board.n) if temp_board.array[i][j] == 0]
        dep = len(move)
        winner = temp_board.is_winner(self.player_number)
        if winner == 0:
            return
        coef = 1 if self.player_number == winner else -1
        for row in range(temp_board.m):
            for col in range(temp_board.n):
                if temp_board.array[row][col] == self.player_number:
                    scores[row][col] += coef * self.SCORE_CURRENT * dep**2
                elif temp_board.array[row][col] != 0:
                    scores[row][col] -= coef * self.SCORE_OTHER * dep**2
        
    def get_best_move(self, temp_board, scores):
        """
        picks the square with the highest score.
        """
        best_square = None
        best_score = float('-inf')
        board_state = str(temp_board.array)
        for square in [(i, j) for i in range(temp_board.m) for j in range(temp_board.n)]:
            r, s = square
            if scores[r][s] > best_score and temp_board.array[r][s] == 0:
                best_square = square
                best_score = scores[r][s]
                print(f"Beste Position: {best_square} mit Score {best_score}")
        if best_square is not None:
            self.new_memo[board_state] = (best_square, best_score)
            return best_square
        else:
            print("Keine beste Position gefunden.")
            return random.choice([(i, j) for i in range(temp_board.m) for j in range(temp_board.n) if temp_board.array[i][j] == 0])

    @ray.remote
    def mc_trial_remote(self, board, depth):
        """
        Ray remote for mc_trial inplace changes.
        """
        board_temp = deepcopy(board)
        dep = deepcopy(depth)
        self.mc_trial(board_temp, dep)
        return board_temp
    
    def make_move(self, game, board):
        """
        This method checks all if there is allready a best move for the current board state
        otherwise it will run the MontecCarlo simulation.
        """
        board_state = str(board.array)
        if board_state in self.memo:
            print("Memoization!")
            best_square = self.memo[board_state][0]
            best_score = self.memo[board_state][1]
            print(f"Beste Position: {best_square} mit Score {best_score}")
            return  Player.make_move(self, best_square[0], best_square[1], game, board)
        if board_state in self.new_memo:
            print("Memoization!")
            best_square = self.new_memo[board_state][0]
            best_score = self.new_memo[board_state][1]
            print(f"Beste Position: {best_square} mit Score {best_score}")
            return Player.make_move(self, best_square[0], best_square[1], game, board)
        scores = [[0] * board.n for _ in range(board.m)]
        ray.init(num_cpus=os.cpu_count())
        futures = [self.mc_trial_remote.remote(self, board, self.DEP) for _ in range(self.NTRIALS)]
        results = ray.get(futures)
        ray.shutdown()
        for clone in results:
            self.mc_update_scores(scores, clone)
        best_square = self.get_best_move(board, scores)
        print(f"Computer wählt aus {len(results)} Möglichkeiten.")
        return Player.make_move(self, best_square[0], best_square[1], game, board)
    
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

    

    # def mc_move(self, board):
    #     """
    #     This method checks all if there is already a best move for the current board state
    #     otherwise it will run the monte carlo simulation. !!!Without Ray!!!
    #     """
    #     board_state = str(board.array)
    #     # Überprüfen auf Memoisierung
    #     if board_state in self.memo:
    #         print("Memoization!")
    #         return self.memo[board_state][0]
    #     if board_state in self.new_memo:
    #         print("Memoization!")
    #         return self.new_memo[board_state][0]

    #     scores = [[0] * board.n for _ in range(board.m)]
    #     for _ in range(self.NTRIALS):
    #         #print(scores)
    #         board_temp = deepcopy(board)
    #         self.mc_trial(board_temp, self.DEP)
    #         #print(board_temp.array)
    #         self.mc_update_scores(scores, board_temp)
    #         #print(scores)
    #     print(scores)
    #     print(f"Computer wählt aus {self.NTRIALS} Möglichkeiten.")
    #     return self.get_best_move(board_temp, scores)