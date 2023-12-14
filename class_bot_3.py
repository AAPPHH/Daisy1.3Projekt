from class_player import Player
from class_board import Board

class MinimaxBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def make_move(self, board):
        best_score = float('-inf')
        best_move = None
        for move in self.get_possible_moves(board):
            score = self.minimax(board, move, 3, False)
            if score > best_score:
                best_score = score
                best_move = move

        if best_move:
            self.place_piece(best_move[0], best_move[1], board)
        else:
            print("No possible moves for MinimaxBot")

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
        for row in range(board.m):
            for col in range(board.n):
                if board.board[row][col] == 0:
                    possible_moves.append((row, col))
        return possible_moves

    def minimax(self, board, move, depth, is_maximizing):
        # Apply the move temporarily
        board.board[move[0]][move[1]] = self.player_number if is_maximizing else 3 - self.player_number

        if depth == 0 or board.is_game_over():
            score = self.evaluate_board(board)
            # Undo the move
            board.board[move[0]][move[1]] = 0
            return score

        if is_maximizing:
            max_eval = float('-inf')
            for next_move in self.get_possible_moves(board):
                eval = self.minimax(board, next_move, depth - 1, False)
                max_eval = max(max_eval, eval)
            # Undo the move
            board.board[move[0]][move[1]] = 0
            return max_eval
        
        else:
            min_eval = float('inf')
            for next_move in self.get_possible_moves(board):
                eval = self.minimax(board, next_move, depth - 1, True)
                min_eval = min(min_eval, eval)
            # Undo the move
            board.board[move[0]][move[1]] = 0
            return min_eval


