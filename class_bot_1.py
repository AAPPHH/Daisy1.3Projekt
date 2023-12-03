
# from class_player import *
# from class_board import *
# class GomokuBot(Player):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         # Initialize any necessary variables or data structures
#         pass

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
    def evaluate_position(self, board):
        # Implement the evaluation function to assess the current position on the board
        pass

    def make_move(self, board):
        # Implement the logic for the bot to make a move on the board
        pass

    def evaluate_position(self, board):
        # Implement the evaluation function to assess the current position on the board
        pass
    

    def evaluate_board(self, board):
        # Implement the evaluation function to assess the current state of the board
        pass
    
    # def make_move(self, board):
    #     import random  # Import the random module
    #     random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #     return random_row  # Return the random number
    #     random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #     return random_col  # Return the random number
    #     point = (random_row, random_col)  # Create a tuple of the random numbers
    #     return point  # Return the tuple
    #     import class_board  # Import the class_board module
    #     board = class_board.Board(5, 5)  # Create an instance of the Board class
    #     return board  # Return the instance
    #     if point == 0:
    #         random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #         return random_row  # Return the random number
    #         random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #         return random_col  # Return the random number
    #         point = (random_row, random_col)  # Create a tuple of the random numbers
    #         return point  # Return the tuple
    #         import class_board  # Import the class_board module
    #         board = class_board.Board(5, 5)  # Create an instance of the Board class
    #         return board  # Return the instance
    #         if point == 0:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #             if point == 0:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #         elif point == 1:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #         elif point == 2:
    #             board_after_move = board.replace(0, point)
    #             return board_after_move
    #         elif point == 1:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #             if point == 0:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #         elif point == 1:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #         elif point == 2:
    #             board_after_move = board.replace(0, point)
    #             return board_after_move
    #         elif point == 2:
    #             board_after_move = board.replace(0, point)
    #             return board_after_move
    #     elif point == 1:
    #         random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #         return random_row  # Return the random number
    #         random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #         return random_col  # Return the random number
    #         point = (random_row, random_col)  # Create a tuple of the random numbers
    #         return point  # Return the tuple
    #         import class_board  # Import the class_board module
    #         board = class_board.Board(5, 5)  # Create an instance of the Board class
    #         return board  # Return the instance
    #         if point == 0:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #             if point == 0:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #         elif point == 1:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #         elif point == 2:
    #             board_after_move = board.replace(0, point)
    #             return board_after_move
    #         elif point == 1:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #             if point == 0:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #         elif point == 1:
    #             random_row = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_row  # Return the random number
    #             random_col = random.randint(0, 4)  # Generate a random number between 0 and 4
    #             return random_col  # Return the random number
    #             point = (random_row, random_col)  # Create a tuple of the random numbers
    #             return point  # Return the tuple
    #             import class_board  # Import the class_board module
    #             board = class_board.Board(5, 5)  # Create an instance of the Board class
    #             return board  # Return the instance
    #         elif point == 2:
    #             board_after_move = board.replace(0, point)
    #             return board_after_move
    #         elif point == 2:
    #             board_after_move = board.replace(0, point)
    #             return board_after_move
    #     elif point == 2:
    #         board_after_move = board.replace(0, point)
    #         return board_after_move



