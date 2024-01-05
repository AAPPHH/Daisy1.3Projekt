from class_player import *  # Allgemeiner Import der Klasse class_player
from class_board import *  # Allgemeiner Import der Klasse class_board

class Player:  # Erstellung der Klasse Player
    def __init__(self, name, player_number):  # Konstruktor und Parameter: Name, Spielernummer
        self.name = name
        self.player_number = player_number


    def place_piece(self, row, col, game, board):  # Definition der Methode, die den Stein setzt, Parameter: Zeilenzahl, Spaltenzahl, Spiel, Spielbrett
        """
        Definition der Methode, die den Stein setzt, Parameter: Zeilenzahl, Spaltenzahl, Spiel, Spielbrett.
        Wenn die Eingabe (row, col) des Spielers gültig is (... == True), ...
        ... dann entspricht das Feld auf dem Spielbrett der Spielernummer (vorher 0).
        True wird zurückgegeben, sofern der Code entsprechend läuft.
        Andernfalls (if nicht gültig) wird False (ungültiger Spielzug) zurückgegeben.
        """
        if board.is_valid_move(row, col):  # Wenn die Eingabe (row, col) des Spielers gültig is (... == True), ...
            board.board[row][col] =  self.player_number  # ... dann entspricht das Feld auf dem Spielbrett der Spielernummer (vorher 0)
            return True  # True wird zurückgegeben, sofern der Code entsprechend läuft
        return False  # Andernfalls (if nicht gültig) wird False (ungültiger Spielzug) zurückgegeben

---


from class_board import *

class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number


    def place_piece(self, row, col, game, board):
        if board.is_valid_move(row, col): 
            board.board[row][col] =  self.player_number 
            return True  
        return False  
