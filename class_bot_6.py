import numpy as np
import random
from class_player import *

class Blocker(Player):
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

    def blocking(self, game, board):
        """
        Gesucht werden die Positionen des Gegners.
        Anschließend wird versucht, den Gegner um seine Position zu blockieren.
        """
        enemy_positions = list(zip(*np.where(board.array == 1)))
        if enemy_positions:
            random_enemy_position = random.choice(enemy_positions)
            shifts = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            for shift in shifts:
                new_row = random_enemy_position[0] + shift[0]
                new_col = random_enemy_position[1] + shift[1]
            if 0 <= new_row < board.m and 0 <= new_col < board.n and board.array[new_row][new_col] == 0:
                print("Blockiert! :-)")
                return Player.make_move(self, new_row, new_col, game, board)
            else:
                exceptional_list = [random_enemy_position[0] - 1, random_enemy_position[0] + 1, random_enemy_position[1] - 1, random_enemy_position[1] + 1]
                valid_rows = [i for i in range(board.m) if i not in exceptional_list]
                valid_columns = [i for i in range(board.n) if i not in exceptional_list]
                random_row = random.choice(valid_rows)
                random_column = random.choice(valid_columns)
                return Player.make_move(self, random_row, random_column, game, board)
        else:
            rdm_row = random.randint(0, board.m - 1)
            rdm_column = random.randint(0, board.n - 1)
            return Player.make_move(self, rdm_row, rdm_column, game, board)
