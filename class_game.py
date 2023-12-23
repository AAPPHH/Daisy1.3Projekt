from class_board import *
from class_player import *
from class_bot_1 import *
from class_bot_2 import *

class Game:  # Erstellung der Klasse Game
    def __init__(self, board):
        self.m = board.m  # Zeilen
        self.n = board.n  # Spalten
        self.k = board.k  # Gewinnbedingung
        self.board = board
        self.player1 = Player("", 1)  # Erzeugung einer Instanz der Klasse Player, der Name ist ein leerer String und die Spielernummer ist 1
        self.player2 = Player("", 2)  # ... die Spielernummer ist 2
        self.current_player = self.player1  # der aktuelle Spieler ist der Spieler 1

    def start(self):  # Definition der Funktion, die das Spiel startet
        print("Let's play five in row!\n Bitte geben Sie Ihre Namen ein: ")  # Willkommenheißung
        time.sleep(1)  # Verzögerung von einer Sekunde
        self.player1.name = input("Spieler 1: ")  # Der eingegebene Name entspricht dem Namen des Player 1
        time.sleep(1)  # Verzögerung von einer Sekunde
        choice = input(
            f"Hallo {self.player1.name}, möchtest du gegen einen anderen Spieler oder gegen den Computer spielen? (1/2): "
        )  # Abfrage durch Input-Funktion. Gegen wen / was möchte gespielt werden?
        time.sleep(1)  # Verzögerung von einer Sekunde
        if choice == "1":  # Wenn die Wahl 1 ist, ...
            self.player2.name = input("Spieler 2: ")  # ... dann ist der Name des Spieler 2 der eingegebene Name des menschlichen Spielers
            self.game_loop()  # Das Spiel wird fortgesetzt
        elif choice == "2":  # Wenn die Wahl 2 ist, ...
            self.player2 = GomokuBot("GomokuBot", 2)  # dann wird eine Instanz der Klasse GomokuBot mit entsprechendem Namen und entsprechender Spielernummer erzeugt
            self.game_loop()  # Das Spiel wird fortgesetzt
        elif choice == "3":
            pass#self.player2 = GomokuBot_2("GomokuBot_2", 2)
        else:
            self.player2 = MinimaxBot("MinimaxBot", 2)
            self.game_loop()  # Das Spiel wird fortgesetzt
        #choice player oder bot dann choice bot1 oder bot2...
    
    def switch_player(self):  # Definition der Funktion, die den Spieler "switched" (wechselt)
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )  # der aktuelle Spieler wird Player 2, wenn der aktuelle Spieler 1 ist. Ansonsten ist der aktuelle Spieler 1

    def game_loop(self):  # Definition der Funktion, die das Spiel nicht ohne Gewinn beendet
        game_over = False  # game_over ist False
        while not game_over:  # Während das Spiel nicht vorbei ist...
            valid_move = True  # ... wird ein valider Spielzug für gültig erklärt
            self.board.print_board()  # Demnach wird das Board (weiterhin) geprintet
            if isinstance(self.current_player, GomokuBot):  # Wenn der aktuelle Spieler der GomokuBot ist...
                GomokuBot.place_piece(self.current_player, self, self.board)  # ... dann setzt der GomokuBot einen Stein

            elif isinstance(self.current_player, MinimaxBot):  # Wenn der aktuelle Spieler der MinimaxBot ist...
                MinimaxBot.make_move(self.current_player, row, col, self, self.board)  # ... dann macht der MinimaxBot einen Zug
            
            # elif isinstance(self.current_player, GomokuBot_2):
            #     GomokuBot_2.place_piece(self.current_player, row, col, self, self.board)    

            elif isinstance(self.current_player, Player):  # Wenn der aktuelle Spieler der menschliche Spieler ist...
                try:  # ... dann VERSUCHE Folgendes:
                    row = int(input(f"Spieler {self.current_player.name}, geben Sie die Zeilennummer ein (0-{self.m-1}): "))  # der aktuelle Spieler gibt eine Eingabe für die Zeile ein, die in einen Int konvertiert wird
                    col = int(input(f"Spieler {self.current_player.name}, geben Sie die Spaltennummer ein (0-{self.n-1}): "))  # ...Eingabe für die Spalte ein, die ...
                except ValueError:  # Wenn die Eingabe ungültig ist...
                    print("Bitte geben Sie gültige ganze Zahlen ein.")  # ... dann soll erneut versucht werden, eine gültige Zahl eingegeben zu werden
                    continue  # Falls erneut eine ungültige Eingabe getätigt wurde, wird 59 - 60 solange ausgeführt bis eine Eingabe gültig ist
                valid_move = Player.place_piece(self.current_player, row, col, self, self.board)  # ein valider Spielzug wird definiert
                if not valid_move:  # Wenn der valide Spielzug nicht wahr (True) ist...
                    print("Bitte geben Sie eine gültige Zahl ein.")  # ... dann wird der Spieler dazu aufgefordert, eine gültige Zahl einzugeben, sodass der Zug valide wird
                    continue  # Initiation einer internen Schleife zur Gewährleistung eines gültigen Spielzuges und der Kontinuation des Spiels bis zum Ende

            if self.board.is_winner(self.current_player.player_number):  # Wenn es einen Gewinner gibt...
                game_over = True  # ... ist das Spiel zu Ende
                self.board.print_board()  # das Board wird noch ein letztes Mal geprintet
                print(f"Spieler {self.current_player.name} hat gewonnen!")  # und es wird gezeigt, wer gewonnen hat
            elif self.board.is_full():  # Wenn das Board voll ist...
                game_over = True  # ... dann ist das Spiel auch zu Ende
                self.board.print_board()  # das Board wird ein letztes Mal geprintet
                print("Das Spiel endet unentschieden!")  # und es wird gesagt, dass keiner gewonnen hat
            else:  # andernfalls:
                if valid_move == True:  # Wenn ein Spielzug gültig ist...
                    self.switch_player()  # ... dann werden die Spieler erneut gewechselt

Spielbrett = Board()  # Die Instanz namens "Spielbrett" ist eine von der Klasse Board
game = Game(Spielbrett)  # Die Instanz namens "game" ist eine von der Klasse Game, wobei das Spiel (Game) die Methoden vom Board (Spielbrett) übernimmt
game.start()  # Das Spiel wird gestartet

