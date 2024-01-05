import numpy as np  # Import der Bibliothek NumPy

from class_player import Player  # Allgemeiner Import der Klasse class_player
from class_board import Board  # Allgemeiner Import der Klasse class_board

class MinimaxBot(Player):  # Erstellung der Klasse MinimaxBot mit Vererbung der Attribute und Methoden der Klasse Player 
    def __init__(self, name, player_number):  # Konstruktor und Parameter: Name, Spielernummer
        super().__init__(name, player_number)  # Initialisierung der übergeordneten Klasse (parent class: Player)

    def make_move(self, row, col, game, board):  # Methode, mit der der Stein gesetzt wird
        best_score = float('-inf')  # der beste Wert wird einem negativ-unendlich-Float gleichgesetzt
        best_move = None  # der beste Zug wird gleich None gesetzt
        for move in self.get_possible_moves(board):  # für jeden Zug in allen möglichen Zügen...
            board_copy = np.copy(board.board)  # ... kopiere das aktuelle Spielbrett ohne Änderungen am Original vorzunehmen...
            score = self.minimax(board_copy, move, 3, True)  # ... und berechne den Score für den aktuellen Zug (3 entspricht der Tiefe)
            if score > best_score:  # Wenn der Score größer ist als der beste Score, ...
                best_score = score  # ... dann überschreibe den Score mit dem besten Score...
                best_move = move  # ... und überschreibe den besten Zug mit dem Zug

        if best_move and board.is_valid_move(best_move[0], best_move[1]):  # Wenn der beste Zug (== True) UND der Zug gültig ist, ...
            board.place_piece(best_move[0], best_move[1], self.player_number)  # ... dann wird der Stein gesetzt
        else:  # Andernfalls...
            print("Kein gültiger Zug gefunden für MinimaxBot")  # Zeige, dass der Zug ungültig ist

    def evaluate_board(self, board):  # Methode, die das Spielbrett bewertet
        return np.sum(board == self.player_number) - np.sum((board != 0) & (board != self.player_number))
        # Anzahl aller Felder mit der Spielernummer subtrahiert mit der Anzahl aller Felder mit 0 UND der Anzahl aller Felder mit der Spielernummer des aktuellen Spielers
        # (Intern: Berechnung mit booleschen Werten, z.B. Anzahl der Trues)

    def get_possible_moves(self, board):  # Methode, die alle möglichen Züge berechnet
            return [(row, col) for row, col in np.ndindex(board.board.shape) if board.board[row, col] == 0]  # Erzeugung einer Liste mit Tuplen mit Koordinaten von Feldern, deren Wert 0 ist

    def minimax(self, board, move, depth, is_maximizing):  
        board[move[0]][move[1]] = self.player_number if is_maximizing else 3 - self.player_number

        if depth == 0 or self.is_game_over(board):  # Wenn die Tiefe gleich 0 ist ODER das Spiel zu Ende ist...
            score = self.evaluate_board(board)  # ... dann berechne den aktuellen Score...
            board[move[0]][move[1]] = 0  # ... und setze das Feld auf 0...
            return score  # ... und gebe score zurück

        if is_maximizing:  # Wenn is_maximizin True ist (is_maximizing == True), ...
            max_eval = float('-inf')  # ... dann ist der maximale Wert ein negativ-unendlicher-Float
            for next_move in self.get_possible_moves(board):  # Für jeden nächsten Zug in allen möglichen Zügen...
                board_copy = np.copy(board)  # kopiere das aktuelle Spielbrett...
                eval = self.minimax(board_copy, next_move, depth - 1, False)  # ... und rekursiver Aufruf der Minimax-Funktion für den nächsten Zug. Die Tiefe (depth) wird um 1 reduziert...
                                                                              # ... und is_maximizing wird auf False gesetzt, da der nächste Zug vom Gegner gemacht wird
                
                max_eval = max(max_eval, eval)  # Aktualisiere den maximalen Wert mit dem Wert des gerade berechneten Zuges...
            board[move[0]][move[1]] = 0  # und setze den vorherigen Zug auf dem Spielbrett zurück...
            return max_eval  # ... und gebe den maximalen Wert zurück
        
        else:  # Andernfalls (elif is_maximizing == False)...
            min_eval = float('inf')  # ... dann ist der minimale Wert ein positiv-unendlicher-Float
            for next_move in self.get_possible_moves(board):  # Für jeden nächsten Zug in allen möglichen Zügen...
                board_copy = np.copy(board)  # kopiere das aktuelle Spielbrett...
                eval = self.minimax(board_copy, next_move, depth - 1, True)  # ... und rekursiver Aufruf der Minimax-Funktion für den nächsten Zug. Die Tiefe (depth) wird um 1 reduziert...
                                                                             # ... und is_maximizing wird auf True gesetzt, da der nächste Zug vom Gegner gemacht wird
                
                min_eval = min(min_eval, eval)  # Aktualisierung des minimalen Wertes
            board[move[0]][move[1]] = 0  # der vorherige Zug wird auf dem Spielbrett rückgängig gemacht
            return min_eval  # der minimale Wert wird zurückgegeben

    def is_game_over(self, board):
        # Diese Methode sollte implementiert werden, um zu prüfen, ob das Spiel vorbei ist
        pass  # Implementieren Sie die Logik basierend auf Ihrem Spiel

----

import numpy as np
import ray
from copy import deepcopy
from class_player import *
import random

class MinimaxBot(Player):
    def __init__(self, name, player_number):
        super().__init__(name, player_number)
        self.use_minimax = False  # Setzen Sie dies auf False, um Alpha-Beta-Pruning zu verwenden
        self.depth = 6  # Tiefe der Minimax-Suche

    # Hauptfunktion, um einen Zug zu machen
    def make_move(self, game, board):
        if self.use_minimax:
            move = self.minimax(game, board, self.depth, self.player_number)
        else:
            move = self.alphabeta_bot(game, board, self.player_number)
        Player.place_piece(self, move[0], move[1], game, board)

    def get_empty_squares(self, board):
        empty_squares = []
        for row_index, row in enumerate(board.board):  # Zugriff auf das NumPy-Array innerhalb des Board-Objekts
            for col_index, value in enumerate(row):
                if value == 0:  # Annahme: 0 repräsentiert ein leeres Feld
                    empty_squares.append((row_index, col_index))
        return empty_squares
    
    def get_enemy(self):
        if self.player_number == 1:
            return 2
        else:
            return 1
        
    def perform_move(self, board, move, player):
        # Erstellt eine Kopie des Bretts und führt darauf einen hypothetischen Zug aus
        board_copy = deepcopy(board)
        row, col = move
        board_copy.board[row][col] = player  # Setzt den Spielerwert an der gewählten Position auf dem internen Array
        return board_copy
    
    def minimax(self, game, board, depth, player):
        moves = self.get_empty_squares(board)
        best_move = moves[0]
        best_score = float('-inf')

        for move in moves:
            clone = self.perform_move(board, move, player)
            score = self.min_play(game, clone, depth-1, move, player)  # Pass the game object here
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def min_play(self, game, position, depth, move, player):
        if position.is_winner(player) or position.is_full() or depth == 0:  # Call is_winner on the game object
            return self.evaluate(position, player)
        moves = self.get_empty_squares(position)
        player = self.get_enemy()
        best_score = float('inf')
        for move in moves:
            clone = deepcopy(position)
            self.perform_move(clone, move, player)
            score = self.max_play(game, clone, depth-1, move, player)
            if score < best_score:
                best_move = move
                best_score = score
        return best_score

    def max_play(self, game, position, depth, lastmove, player):
        if position.is_winner(player) or position.is_full() or depth == 0:
            return self.evaluate(position, depth)
        moves = self.get_empty_squares(position)
        player = self.get_enemy()
        best_score = float('-inf')
        for move in moves:
            clone = deepcopy(position)
            self.perform_move(clone, move, player)
            score = self.min_play(game, clone, depth-1, move, player)
            if score > best_score:
                best_move = move
                best_score = score
        return best_score

    def evaluate(self, pos, dep):
        cur_player = self.player_number
        print(pos.board)
        if pos.is_winner(self.player_number) == True:
            return 10 * (dep+1)
        elif pos.is_winner(self.player_number) == False:
            return -10 * (dep+1)
        return 0

    # Alpha-Beta-Pruning
    def alphabeta(self, position, lastmove, player, alpha, beta, depth):
        if position.is_winner(player) or position.is_full() or depth == 0:
            return self.evaluate(position, depth)
        for move in self.get_empty_squares(position):
            clone = deepcopy(position)
            self.perform_move(clone, move, player)
            val = self.alphabeta(clone, move, self.get_enemy(), alpha, beta, depth-1)
            if player == self.player_number:
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == self.player_number:
            return alpha
        else:
            return beta

    def alphabeta_bot(self, game, position, player):
        a = -2
        choices = []
        if len(self.get_empty_squares(position)) == position.board.size ** 2: # bester erster Zug
            return position.board.size ** 2 // 2 + 1
        for move in self.get_empty_squares(position):
            clone = deepcopy(position)
            self.perform_move(clone, move, player)
            val = self.alphabeta(clone, move, self.get_enemy(), -2, 2, self.depth)
            if val > a:
                a = val
                choices = [move]
            elif val == a:
                choices.append(move)
        return random.choice(choices)
