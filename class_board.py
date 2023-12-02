import numpy as np
from class_player import *
class Board:
    def __init__(self, m=5, n=5, k=4):
        self.m = m
        self.n = n
        self.k = k
        self.board = np.zeros((m, n))

    def print_board(self):
        for row in self.board:
            print(' '.join(str(int(val)) for val in row))

    def is_valid_move(self, row, col):
        m, n = self.board.shape
        if 0 <= row < m and 0 <= col < n and self.board[row][col] == 0:
            return True
        return False

    def is_winner(self, piece): 
        # Zeilen überprüfen
        if np.any(np.all(self.board == piece, axis=1)):
            return True

        # Spalten überprüfen
        if np.any(np.all(self.board == piece, axis=0)):
            return True

        # Hauptdiagonale überprüfen, wenn das Brett quadratisch ist
        if self.board.shape[0] == self.board.shape[1]:
            if np.all(np.diag(self.board) == piece):
                return True

            # Nebendiagonale überprüfen
            if np.all(np.diag(np.fliplr(self.board)) == piece):
                return True

        return False
    
    def is_full(self):
        return np.all(self.board != 0)
    
