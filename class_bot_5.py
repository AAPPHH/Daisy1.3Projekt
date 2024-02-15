import numpy as np
import random
from class_player import *

class Silly(Player):
     def __init__(self, name, player_number):
        super().__init__(name, player_number)

     def make_move(self, game, board):
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
               if 0 <= move[0] < board.m and 0 <= move[1] < board.n and board.array[move[0]][move[1]] == 0:
                    print(f"{self.name} macht einen Zug an Position {move}!")
                    return Player.make_move(self, move[0], move[1], game, board)
          row = random.randint(0, board.m - 1)
          col = random.randint(0, board.n - 1)
          print(f"{self.name} ==> ({row}, {col})!")
          return Player.make_move(self, row, col, game, board)
