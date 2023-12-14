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
        score = 0

        for row in range(board.m):
            for col in range(board.n):
                if board.board[row][col] == self.player_number:
                    score += 1  
                elif board.board[row][col] != 0:
                    score -= 1 
        return score

    def get_possible_moves(self, board):
        possible_moves = []
        # Durchlaufe das Spielbrett, um alle möglichen Züge zu finden
        for row in range(board.height):
            for col in range(board.width):
                if board.is_piece_of_player(row, col, self.player_number):
                    # Finde alle möglichen Züge für das Spielstück an dieser Position
                    piece_moves = board.get_moves_for_piece(row, col)
                    possible_moves.extend(piece_moves)
        return possible_moves

    def minimax(self, board, depth, is_maximizing):
        if depth == 0 or board.is_game_over():
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

