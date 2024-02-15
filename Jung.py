import numpy as np
import random
from class_player import *

class Kölsche_Jung(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
    
    def recognize_enemy(self, game, board):
        """
        Wenn der aktuelle Spieler 1 ist, wird 2 zurückgegeben, ansonsten 1,
        um den Gegner zu betrachten.
        """
        if self.player_number == 1:
            self.player_number = 2
            return self.player_number
        else:
            self.player_number = 1
            return self.player_number

    def halt_op(self, game, board):
        """
        Gesucht wird eine Kette von drei Einsen auf dem board.
        Zu Beginn gilt found_chain = False.
        Geprüft wird, ob der Anfang btw. das Ende der Kette eine 0 ist.
        Wenn ja, wird an der Kette gesetzt.
        Erst werden erst die Spalten und dann die Zeilen durchlaufen.
        Danach invers.
        Wenn keine Kette gefunden wird, wird zentral gesetzt.
        Gelingt das nicht, wird zufällig gesetzt.
        """
        found_chain = False
        for i in range(board.board.shape[0]):
            for j in range(board.board.shape[1] - 2):
                if np.array_equal(board.board[i, j:j + board.k ], [self.player_number] * board.k):
                    if j > 0 and board.board[i, j-1] == 0:
                        return Player.place_piece(self, i, j - 1, game, board)
                    elif j+3 < board.board.shape[1] and board.board[i, j + board.k] == 0:
                        print("Blockiert! :-) ... Kölsch? ...")
                        return Player.place_piece(self, i, j + board.k, game, board)
                    found_chain = True
        for i in range(board.board.shape[0] - 2):
            for j in range(board.board.shape[1]):
                if np.array_equal(board.board[i:i + board.k, j], [self.player_number] * board.k):
                    if i > 0 and board.board[i - 1, j] == 0:
                        return Player.place_piece(self, i - 1, j, game, board)
                    elif i+3 < board.board.shape[0] and board.board[i + board.k, j] == 0:
                        print("Blockiert! :-) ... Kölsch? ...")
                        return Player.place_piece(self, i + board.k, j, game, board)
                    found_chain = True
        for i in range(board.board.shape[0] - 2 ):
            for j in range(board.board.shape[1] - 2):
                if np.array_equal(board.board[i:i + board.k, j:j + board.k], [self.player_number] * board.k):
                    if i > 0 and j > 0 and board.board[i - 1, j - 1] == 0:
                        return Player.place_piece(self, i - 1, j - 1, game, board)
                    elif i + board.k < board.board.shape[0] and j + board.k < board.board.shape[1] and board.board[i + board.k, j + board.k] == 0:
                        print("Blockiert! :-) ... Kölsch? ...")
                        return Player.place_piece(self, i + board.k, j + board.k, game, board)
        if not found_chain:
            center = (board.m // 2, board.n // 2)
            moves = [center, (center[0] + 1, center[1]), (center[0] - 1, center[1]),
                        (center[0] - 1, center[1] - 1), (center[0] - 1, center[1] + 1),
                        (center[0], center[1] - 1), (center[0], center[1] + 1),
                        (center[0] + 1, center[1] - 1), (center[0] + 1, center[1] + 1),
                        (center[0] + 2, center[1]), (center[0] + 2, center[1] + 1),
                        (center[0] + 2, center[1] - 1), (center[0] + 2, center[1] + 2),
                        (center[0] + 2, center[1] - 2), (center[0] + 1, center[1] + 2),
                        (center[0] + 1, center[1] - 2), (center[0], center[1] + 2),
                        (center[0], center[1] - 2), (center[0] - 1, center[1] + 2),
                        (center[0] - 1, center[1] - 2), (center[0] - 2, center[1] + 2),
                        (center[0] - 2, center[1] - 2), (center[0] - 2, center[1] + 1),
                        (center[0] - 2, center[1] - 1), (center[0] - 1, center[1])]
            for move in moves:
                if 0 <= move[0] < board.m and 0 <= move[1] < board.n and board.board[move[0]][move[1]] == 0:
                        print(f"{self.name} macht einen Zug an Position {move}!")
                        return Player.place_piece(self, move[0], move[1], game, board)
            row = random.randint(0, board.m - 1)
            col = random.randint(0, board.n - 1)
            print(f"{self.name} macht einen zufälligen Zug an Position ({row}, {col})!")
            return Player.place_piece(self, row, col, game, board)
