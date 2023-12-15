import numpy as np

from class_player import Player
from class_board import Board

class MinimaxBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def make_move(self, row, col, game, board):
        # Assuming 'board' is an instance of the Board class, we access the NumPy array with 'board.board'
        best_score = float('-inf')
        best_move = None
        for move in self.get_possible_moves(board.board):  # Access the NumPy array
            board_copy = np.copy(board.board)  # Create a copy of the NumPy array
            score = self.minimax(board_copy, move, 3, True)
            if score > best_score:
                best_score = score
                best_move = move

        # After finding the best move, we use 'board' as an instance of Board to call 'is_valid_move'
        if best_move and board.is_valid_move(best_move[0], best_move[1]):
            board.place_piece(best_move[0], best_move[1], self.player_number)
        else:
            print("Kein gültiger Zug gefunden für MinimaxBot")

    def evaluate_board(self, board):
        # Einfache Bewertung: Zähle die Steine des Spielers
        return np.sum(board == self.player_number) - np.sum((board != 0) & (board != self.player_number))

    def get_possible_moves(self, board):
        # Finde alle leeren Positionen für mögliche Züge
        return [(row, col) for row, col in np.ndindex(board.board.shape) if board.board[row, col] == 0]

    def minimax(self, board, move, depth, is_maximizing):
        # Here 'board' is a NumPy array
        board[move[0]][move[1]] = self.player_number if is_maximizing else 3 - self.player_number

        if depth == 0 or self.is_game_over(board):  # 'is_game_over' also needs to work with NumPy array
            score = self.evaluate_board(board)  # 'evaluate_board' should accept a NumPy array
            board[move[0]][move[1]] = 0  # Undo the move on the NumPy array
            return score

        if is_maximizing:
            max_eval = float('-inf')
            for next_move in self.get_possible_moves(board):
                board_copy = np.copy(board)
                eval = self.minimax(board_copy, next_move, depth - 1, False)
                max_eval = max(max_eval, eval)
            board[move[0]][move[1]] = 0  # Zug rückgängig machen
            return max_eval
        else:
            min_eval = float('inf')
            for next_move in self.get_possible_moves(board):
                board_copy = np.copy(board)
                eval = self.minimax(board_copy, next_move, depth - 1, True)
                min_eval = min(min_eval, eval)
            board[move[0]][move[1]] = 0  # Zug rückgängig machen
            return min_eval

    def is_game_over(self, board):
        # Diese Methode sollte implementiert werden, um zu prüfen, ob das Spiel vorbei ist
        pass  # Implementieren Sie die Logik basierend auf Ihrem Spiel


