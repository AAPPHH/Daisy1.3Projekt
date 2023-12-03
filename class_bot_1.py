import random
import board

class GomokuBot(Player):
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col

    def make_move(self, board):
        random_row = random.randint(0, 4)
        random_col = random.randint(0, 4)
        while board[random_row][random_col] != 0:
            random_row = random.randint(0, 4)
            random_col = random.randint(0, 4)
        board[random_row][random_col] = 2




