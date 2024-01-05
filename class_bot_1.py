from class_board import *
from class_player import *
from class_board import * 
import random

class GomokuBot(Player):
    """
    Erstellung der Klasse GomokuBot und Vererbung der Methode von Player.
    Vererbung der Parameter.
    """
    def __init__(self, name, player_number):
        super().__init__(name, player_number)

    def place_piece(self, game, board):
        """
        Denition der Methode playe_piece mit drei Parametern
        row = zufällige Zahl zwischen 0 und 4
        col = zufällige Zahl zwischen 0 und 4
        Stein wird gemäß der Funktion place_piece gesetzt
        """
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        Player.place_piece(self, row, col, game, board)
