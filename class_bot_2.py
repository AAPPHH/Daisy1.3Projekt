from class_player import *
from Decision_table import *

class ChainTreeBot(Player):
    """
    Bot that uses a decision tabel and otherwise places pieces next to his own piece.
    """
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.memo = decision_table

    def make_move(self, game, board):
            board_state = str(board.array)
            if board_state in self.memo:
                print("Memoization!")
                move = self.memo[board_state][0]
                best_score = self.memo[board_state][1]
                print(f"Beste Position: {move} mit Score {best_score}")
                return Player.make_move(self, move[0], move[1], game, board)
            else:
                move = self.direction(board.array, self.player_number)
                return Player.make_move(self, move[0], move[1], game, board)

    def get_pos(self, board, player_number):
        """
        Returns a list of tuples with the coordinates of the player's pieces.
        """
        chain = []
        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                if value == player_number:
                    chain.append((row_index, col_index))
        return chain

    def direction(self, board, player_number):
        """
        Returns a random choice of a move that is next to the player's pieces.
        """
        chain = self.get_pos(board, player_number)
        moves_list = []
        for row_index, col_index in chain:
            potential_moves = [
                (row_index, col_index + 2),
                (row_index, col_index - 2),
                (row_index + 2, col_index),
                (row_index - 2, col_index),
                (row_index + 2, col_index + 2),
                (row_index - 2, col_index - 2),
                (row_index + 2, col_index - 2),
                (row_index - 2, col_index + 2)
            ]
            for move in potential_moves:
                if (0 <= move[0] < len(board) and 0 <= move[1] < len(board[0]) and
                        board[move[0]][move[1]] == 0 and
                        ((move[0], move[1] - 1) in chain or
                         (move[0], move[1] + 1) in chain or
                         (move[0] - 1, move[1]) in chain or
                         (move[0] + 1, move[1]) in chain or
                         (move[0] - 1, move[1] - 1) in chain or
                         (move[0] + 1, move[1] + 1) in chain or
                         (move[0] - 1, move[1] + 1) in chain or
                         (move[0] + 1, move[1] - 1) in chain)):
                    moves_list.append(move)
        if moves_list:
            return random.choice(moves_list)
        else:
            return self.random_move()

    def random_move(self):
        """
        Returns a random move.
        """
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        return (row, col)