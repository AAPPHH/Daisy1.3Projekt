import numpy as np
from class_player import *

class Board:
    def __init__(self, m=5, n=5, k=4):  # Default-Werte gemäß des Softcodings
        self.m = m  # Zeilenanzahl
        self.n = n  # Spaltenanzahl
        self.k = k  # Länge der Gewinnsequenz
        self.board = np.zeros((m, n))  # Board als Numpy-Array mit allen Feldern auf 0

    def print_board(self):  # Definition der Funktion, die das Baord printed
        for row in self.board:  # "Für jede Zeile im Numpy-Array"
            print(' '.join(str(int(val)) for val in row))  # "Konvertiere jeden Wert in einen Int und dann in einen Str. Anschließend verbinde alle Str und setzt Leerzeichen

    def is_valid_move(self, row, col):  # Definition der Funktion, die die Gültigkeit eines Spielzuges eruiert
        m, n = self.board.shape  # Erstellung eines Numpy-Arrays mit zwei Dimensionen, Zuweisung der Dimensionen
        if 0 <= row < m and 0 <= col < n and self.board[row][col] == 0:  # "Liegt row zwischen 0 und m und liegt col zwischen 0 und n und ist der Wert des Feldes 0?"
            return True  # "... dann wahr -> valider Zug"
        return False  # "andernfalls falsch"
    
    def is_winner(self, piece):  # Definition der Funktion, die einen Gewinner feststellt
        win_sequence = str(piece) * self.k  # Gewinnsequenz entspricht dem k-fachen von Piece als Str

        for row in self.board:  # "Für jede Zeile im Board..."
            if win_sequence in ''.join(str(int(e)) for e in row):  # "...wenn die Gewinnsequenz in einer Zeile vorhanden ist"
                return True  # "... dann gebe 'wahr' wieder"

        for col in self.board.T:  # gleiches Verfahren wie in 24 - 26, wobei nun die Gewinnsequenz in einer Spalte analysiert wird
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
    
