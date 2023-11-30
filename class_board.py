import numpy as np

class Board:
    def __init__(self, m=5, n=5, k=4):
        self.m = m #rows 
        self.n = n #columns
        self.k = k #number of pieces in a row to win
        self.board = np.zeros((m, n))

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def place_piece(self, row, col, piece):
        if self.is_valid_move(row, col):
            self.board[row][col] = piece
            return True
        return False

    def is_valid_move(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' ':
            return True
        return False

    def is_winner(self, piece):
        # Check rows
        for row in self.board:
            if row.count(piece) == self.size:
                return True

        # Check columns
        for col in range(self.size):
            if [self.board[row][col] for row in range(self.size)].count(piece) == self.size:
                return True

        # Check diagonals
        if [self.board[i][i] for i in range(self.size)].count(piece) == self.size:
            return True
        if [self.board[i][self.size - 1 - i] for i in range(self.size)].count(piece) == self.size:
            return True

        return False
Spielbrett = Board()
print_board()