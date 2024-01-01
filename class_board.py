import numpy as np
from class_player import *

class Board:
    def __init__(self, m=5, n=5, k=4):  # Default-Werte gemäß des Softcodings
        self.m = m  # Zeilenanzahl
        self.n = n  # Spaltenanzahl
        self.k = k  # Länge der Gewinnsequenz
        self.board = np.zeros((m, n))  # Board als Numpy-Array mit allen Feldern auf 0

    def reset_board(self):
        """
        self.board = np.zeros(self.m, self.n)) setzt alle Felder im Board gleich 0.
        """
        self.board = np.zeros((self.m, self.n))

    def reset_board(self):
        self.board = np.zeros((self.m, self.n))

    def print_board(self):
    """
    print(' '.join(str(int(val)) for val in row))
    For-Schleife geht durch alle Zeilen im Board.
    Alle Werte (in den Feldern) werden in eine ganze Zahl (int) und dann in einen String konvertiert.
    ' '.join -> verbindet die Strings miteinander, hält sie jedoch mit einem Leerzeichen getrennt.
    Das Board wird geprintet.
    """
        for row in self.board:
            print(' '.join(str(int(val)) for val in row))

    def is_valid_move(self, row, col):  # Definition der Funktion, die die Gültigkeit eines Spielzuges eruiert
    """
    Definition der Funktion, die die Gültigkeit eines Spielzuges eruiert.
    Erstellung eines Numpy-Arrays mit zwei Dimensionen, Zuweisung der Dimensionen.
    "Liegt row zwischen 0 und m und liegt col zwischen 0 und n und ist der Wert des Feldes 0?"
    "... dann wahr -> valider Zug"
    "andernfalls falsch"
    """
        m, n = self.board.shape  # Erstellung eines Numpy-Arrays mit zwei Dimensionen, Zuweisung der Dimensionen
        if 0 <= row < m and 0 <= col < n and self.board[row][col] == 0:  # "Liegt row zwischen 0 und m und liegt col zwischen 0 und n und ist der Wert des Feldes 0?"
            return True  # "... dann wahr -> valider Zug"
        return False  # "andernfalls falsch"
    
    def is_winner(self, piece):  # Definition der Funktion, die einen Gewinner feststellt
    """
    Definition der Funktion, die einen Gewinner feststellt.
    Gewinnsequenz entspricht dem k-fachen von Piece als Str.
    "Für jede Zeile im Board..."
    "...wenn die Gewinnsequenz in einer Zeile vorhanden ist"
    "... dann gebe 'wahr' wieder"
    Gleiches Verfahren wie davor, wobei nun die Gewinnsequenz in einer Spalte analysiert wird.
    """
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
        """
        return np.all(self.board != 0)
        Methode, die überprüft, ob das alle Werte im Board ungleich 0 sind (np.all(self.board != 0).
        Ausgegeben (return) werden entweder True oder False
        """
        return np.all(self.board != 0)
    
