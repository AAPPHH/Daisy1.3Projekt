class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Invalid move. Please try again.')


# Path: class_game
