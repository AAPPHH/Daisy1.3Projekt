from class_player import *
from class_board import *
class MinimaxBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
    
    def make_move(self):
        best_score = float('-inf')
        best_move = None
        for move in self.get_possible_moves(self.board):
            score = self.minimax(move, 3, False)
            if score > best_score:
                best_score = score
                best_move = move
        self.place_piece(best_move[0], best_move[1])
    
    def evaluate_board(self, board):
        pass

    def get_possible_moves(self, board):
        pass

    def minimax(self, board, depth, is_maximizing):
        if depth == 0 or game_over:
            return self.evaluate_board(board)

        if is_maximizing:
            max_eval = float('-inf')
            for move in self.get_possible_moves(board):
                eval = self.minimax(move, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_possible_moves(board):
                eval = self.minimax(move, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

