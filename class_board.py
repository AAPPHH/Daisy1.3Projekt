import numpy as np
from class_player import *

class Board:
    def __init__(self, m=5, n=5, k=4):
        self.m = m # rows
        self.n = n # columns
        self.k = k # number of pieces in a row to win
        self.array = np.zeros((m, n)) # 2D array of zeros we play on

    def reset_board(self):
        """
        Resets the board to an empty state of zeros
        """
        self.array = np.zeros((self.m, self.n))

    def print_board(self):
        """
        Prints the board to the console as strings
        """
        for row in self.array:
            print(' '.join(str(int(val)) for val in row))

    def is_valid_move(self, row, col):
        """
        Checks if a move is valid. i.e. if the cell is empty and within the board's boundaries.
        """
        m, n = self.array.shape
        if 0 <= row < m and 0 <= col < n and self.array[row][col] == 0:
            return True
        return False
    
    def is_winner(self, piece):
        """
        Checks if a player has won. i.e. if there is a string of k pieces of the same player.
        """
        win_sequence = str(piece) * self.k
        for row in self.array:
            if win_sequence in ''.join(str(int(e)) for e in row):
                return True
        for col in self.array.T:
            if win_sequence in ''.join(str(int(e)) for e in col):
                return True
        for diag in [np.diagonal(self.array, offset) for offset in range(-self.array.shape[0] + self.k, self.array.shape[1] - self.k + 1)]:
            if win_sequence in ''.join(str(int(e)) for e in diag):
                return True
        for diag in [np.diagonal(np.fliplr(self.array), offset) for offset in range(-self.array.shape[0] + self.k, self.array.shape[1] - self.k + 1)]:
            if win_sequence in ''.join(str(int(e)) for e in diag):
                return True
        return False

    def is_full(self):
        """
        Checks if the board is full
        """
        return np.all(self.array != 0)
    
