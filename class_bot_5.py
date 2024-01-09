import numpy as np
import random
from class_player import *
from class_board import *

class Blocker(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def check_enemy(self, board):
        positions = np.where(self.board == 1)
        enemy_positions = list(zip(positions[0], positions[1]))
        return enemy_positions
    
    def search_enemy(self, board, enemy_positions):
        random_enemy_position = random.choice(enemy_positions)
        if random_enemy_position[0] < self.m and random_enemy_position[1] < self.n and self.m > 0 and self.n > 0:
            found_enemy = True
        else:
            found_enemy = False

    def block_enemy(self, game, board, found_enemy, random_enemy_position):
        if found_enemy:
            if self.board[random_enemy_position[0] - 1][random_enemy_position[1]] == 0:
                Player.place_piece(self, random_enemy_position[0] - 1, random_enemy_position[1], game, board)
            elif self.board[random_enemy_position[0] + 1][random_enemy_position[1]] == 0:
                Player.place_piece(self, random_enemy_position[0] + 1, random_enemy_position[1], game, board)
            elif self.board[random_enemy_position[0]][random_enemy_position[1] - 1] == 0:
                Player.place_piece(self, random_enemy_position[0], random_enemy_position[1] - 1, game, board)
            elif self.board[random_enemy_position[0]][random_enemy_position[1] + 1] == 0:
                Player.place_piece(self, random_enemy_position[0], random_enemy_position[1] + 1, game, board)
            elif self.board[random_enemy_position[0] - 1][random_enemy_position[1] - 1] == 0:
                Player.place_piece(self, random_enemy_position[0] - 1, random_enemy_position[1] - 1, game, board)
            elif self.board[random_enemy_position[0] - 1][random_enemy_position[1] + 1] == 0:
                Player.place_piece(self, random_enemy_position[0] - 1, random_enemy_position[1] + 1, game, board)
            elif self.board[random_enemy_position[0] + 1][random_enemy_position[1] - 1] == 0:
                Player.place_piece(self, random_enemy_position[0] + 1, random_enemy_position[1] - 1, game, board)
            elif self.board[random_enemy_position[0] + 1][random_enemy_position[1] + 1] == 0:
                Player.place_piece(self, random_enemy_position[0] + 1, random_enemy_position[1] + 1, game, board)
            else:
                exceptional_list = [random_enemy_position[0] - 1, random_enemy_position[0] + 1, random_enemy_position[1] - 1, random_enemy_position[1] + 1]
                valid_rows = [i for i in range(self.m) if i not in exceptional_list]
                valid_columns = [i for i in range(self.n) if i not in exceptional_list]
                random_row = random.choice(valid_rows)
                random_column = random.choice(valid_columns)
                Player.place_piece(self, random_row, random_column, game, board)
        else:
            rdm_row = random.randint(0, self.m - 1)
            rdm_column = random.randint(0, self.n - 1)
            Player.place_piece(self, rdm_row, rdm_column, game, board)
