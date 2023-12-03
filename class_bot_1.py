from class_player import *
from class_board import *

class GomokuBot:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col

class GomokuBot:
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col
        # Initialize any necessary variables or data structures
    def make_move(self, board):
        import random
        random_row = random.randint(0, 4)
        return random_row
        random_col = random.randint(0, 4)
        return random_col
        if board[random_row][random_col] == 1:
            st_invalid_move = False
            return st_invalid_move
        elif board[random_row][random_col] == 2:
            nd_invalid_move = False
            return nd_invalid_move
        elif board[random_row][random_col] == 0:
            board[random_row][random_col] = 2
            return True
        while st_invalid_move == False or nd_invalid_move == False:
            random_row = random.randint(0, 4)
            random_col = random.randint(0, 4)
            if board[random_row][random_col] == 0:
                board[random_row][random_col] = 2
                return True

        

class GomokuBot(Player):
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col

    def make_move(self, board):
        import random
        random_row = random.randint(0, 4)
        random_col = random.randint(0, 4)
        if board[random_row][random_col] == 1:
            return False
        elif board[random_row][random_col] == 2:
            return False
        elif board[random_row][random_col] == 0:
            board[random_row][random_col] = 2
            return True
        else:
            return False
        while st_invalid_move == False or nd_invalid_move == False:
            random_row = random.randint(0, 4)
            random_col = random.randint(0, 4)
            if board[random_row][random_col] == 0:
                board[random_row][random_col] = 2
                return True


class GomokuBot(Player):
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col

    def make_move(self, board):
        import random
        random_row = random.randint(0, 4)
        random_col = random.randint(0, 4)
        while board[random_row][random_col] != 0:
            random_row = random.randint(0, 4)
            random_col = random.randint(0, 4)
        board[random_row][random_col] = 2




