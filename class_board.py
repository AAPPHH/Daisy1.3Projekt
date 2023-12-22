import numpy as np
from class_player import *

class Board:
    def __init__(self, m=5, n=5, k=4):
        self.m = m
        self.n = n
        self.k = k
        self.board = np.zeros((m, n))

    def reset_board(self):
        self.board = np.zeros((self.m, self.n))

    def print_board(self):
        for row in self.board:
            print(' '.join(str(int(val)) for val in row))

    def is_valid_move(self, row, col):
        m, n = self.board.shape
        if 0 <= row < m and 0 <= col < n and self.board[row][col] == 0:
            return True
        return False
    
    def is_winner(self, piece):
        win_sequence = str(piece) * self.k

        for row in self.board:
            if win_sequence in ''.join(str(int(e)) for e in row):
                return True

        for col in self.board.T:
            if win_sequence in ''.join(str(int(e)) for e in col):
                return True

        for diag in [np.diagonal(self.board, offset) for offset in range(-self.board.shape[0] + self.k, self.board.shape[1] - self.k + 1)]:
            if win_sequence in ''.join(str(int(e)) for e in diag):
                return True

        for diag in [np.diagonal(np.fliplr(self.board), offset) for offset in range(-self.board.shape[0] + self.k, self.board.shape[1] - self.k + 1)]:
            if win_sequence in ''.join(str(int(e)) for e in diag):
                return True

        return False

    def is_full(self):
        return np.all(self.board != 0)
    
