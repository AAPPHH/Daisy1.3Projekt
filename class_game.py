import time
import copy
import pandas as pd
from class_board import *
from class_player import *
from class_bot_1 import *
from class_bot_2 import *
from class_bot_3 import *
from class_bot_4 import *
from class_bot_5 import *
from class_bot_6 import *
from class_bot_7 import *
from Data import *

class Game:
    def __init__(self, board):
        self.m = board.m  # Zeilen
        self.n = board.n  # Spalten
        self.k = board.k  # Gewinnbedingung
        self.board = board #array objekt der klasse board
        self.player1 = Player("", 1)
        self.player2 = Player("", 2)
        self.current_player = self.player1
        self.game_arrays = []
        self.winner = None
        self.starter = None

    def start(self):
        self.language = input("Deutsch (1), English (2), Español (3) ")
        if self.language == "1":
            self.start_german()
        elif self.language == "2":
            self.start_english()
        elif self.language == "3":
            self.start_spanish()

    def start_german(self):
        try:
            start_choice = input("Let's play five in row! Wollen Sie oder soll der Computer spielen? (1/2): ")
            if start_choice == "1":
                self.valid_name_player_german()
                choice = input(f"Hallo {self.player1.name}, möchtest du gegen einen anderen Spieler oder gegen den Computer spielen? (1/2): ")
                if choice == "1":
                    self.player2.name = input("Spieler 2: ")
                    self.whos_first_german()
                elif choice == "2":
                    choice = input(f"Hallo {self.player1.name}, möchtest du gegen einen RandomBot, Silly, MinimaxBot, MonteCarloBot, Blocker oder Kölsche_Jung spielen? (1/2/3/4/5/6): ")
                    if choice == "1":
                        self.player2 = GomokuBot("GomokuBot", 2)
                        self.whos_first_german()
                    elif choice == "2":
                        self.player2 = Silly("Silly", 2)
                        self.whos_first_german()
                    elif choice == "3":
                        self.player2 = MinimaxBot("MinimaxBot", 2)
                        self.whos_first_german()
                    elif choice == "4":
                        self.player2 = MonteCarloBot("MonteCarloBot", 2)
                        self.whos_first_german()
                    elif choice == "5":
                        self.player2 = Blocker("Blocker", 2)
                        self.whos_first_german()
                    elif choice == "6":
                        self.player2 = Kölsche_Jung("Kölsche_Jung", 2)
                        self.whos_first_german()
                    else:
                        print("Bitte geben Sie eine gültige Zahl ein. ")
            elif start_choice == "2":
                choice_bot_1 = input("Möchtest du, dass RandomBot, Silly, MinimaxBot, MonteCarloBot, Blocker oder Kölsche_Jung Player One ist? (1/2/3/4/5/6): ")
                if choice_bot_1 == "1":
                    self.player1 = GomokuBot("GomokuBot", 1)
                elif choice_bot_1 == "2":
                    self.player1 = Silly("Silly", 1)
                elif choice_bot_1 == "3":
                    self.player1 = MinimaxBot("MinimaxBot", 1)
                elif choice_bot_1 == "4":
                    self.player1 = MonteCarloBot("MonteCarloBot", 1)
                elif choice_bot_1 == "5":
                    self.player1 = Blocker("Blocker", 1)
                elif choice_bot_1 == "6":
                    self.player1 = Kölsche_Jung("Kölsche_Jung", 1)
                else:
                    print("Bitte geben Sie eine gültige Zahl ein. ")
                self.current_player = self.player1
                choice_bot_2 = input("Möchtest du, dass RandomBot, Silly, MinimaxBot, MonteCarloBot, Blocker oder Kölsche_Jung Player Two ist? (1/2/3/4/5/6): ")
                if choice_bot_2 == "1":
                    self.player2 = GomokuBot("GomokuBot_2", 2)
                elif choice_bot_2 == "2":
                    self.player2 = Silly("Silly", 2)
                elif choice_bot_2 == "3":
                    self.player2 = MinimaxBot("MinimaxBot_2", 2)
                elif choice_bot_2 == "4":
                    self.player2 = MonteCarloBot("MonteCarloBot_2", 2)
                elif choice_bot_2 == "5":
                    self.player2 = Blocker("Blocker_2", 2)
                elif choice_bot_2 == "6":
                    self.player2 = Kölsche_Jung("Kölsche_Jung_2", 2)
                num_games = input("Wie viele Runden möchtest du spielen? (1-10000): ")
                try:
                    for game_number in range(int(num_games)):
                            print(f"Spiel {game_number + 1} von {num_games}")
                            self.game_loop()
                            self.game_arrays = []
                            self.board.reset_board()
                    print("Alle Spiele wurden gespielt.")
                except ValueError:
                    print("Bitte geben Sie eine gültige Zahl ein.")
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein.")

    def start_english(self):
        try:
            start_choice = input("Let's play five in row! Do you want to play against another player or against the computer? (1/2): ")
            if start_choice == "1":
                self.valid_name_player_english()
                choice = input(f"Hello {self.player1.name}, do you want to play against another player or against the computer? (1/2): ")
                if choice == "1":
                    self.player2.name = input("Player 2: ")
                    self.whos_first_english()
                elif choice == "2":
                    choice = input(f"Hello {self.player1.name}, do you want to play RandomBot, Silly, MinimaxBot, MonteCarloBot, Blocker or Koelsche_Jung? (1/2/3/4/5/6): ")
                    if choice == "1":
                        self.player2 = GomokuBot("GomokuBot", 2)
                        self.whos_first_english()
                    elif choice == "2":
                        self.player2 = Silly("Silly", 2)
                        self.whos_first_english()
                    elif choice == "3":
                        self.player2 = MinimaxBot("MinimaxBot", 2)
                        self.whos_first_english()
                    elif choice == "4":
                        self.player2 = MonteCarloBot("MonteCarloBot", 2)
                        self.whos_first_english()
                    elif choice == "5":
                        self.player2 = Blocker("Blocker", 2)
                        self.whos_first_english()
                    elif choice == "6":
                        self.player2 = Kölsche_Jung("Kölsche_Jung", 2)
                        self.whos_first_english()
                    else:
                        print("Invalid input. Try again. ")
            elif start_choice == "2":
                choice_bot_1 = input(f"Hello {self.player1.name}, do you want to play RandomBot, Silly, MinimaxBot, MonteCarloBot, Blocker or Koelsche_Jung? (1/2/3/4/5/6): ")
                if choice_bot_1 == "1":
                    self.player1 = GomokuBot("GomokuBot", 1)
                elif choice_bot_1 == "2":
                    self.player1 = Silly("Silly", 1)
                elif choice_bot_1 == "3":
                    self.player1 = MinimaxBot("MinimaxBot", 1)
                elif choice_bot_1 == "4":
                    self.player1 = MonteCarloBot("MonteCarloBot", 1)
                elif choice_bot_1 == "5":
                    self.player1 = Blocker("Blocker", 1)
                elif choice_bot_1 == "6":
                    self.player1 = Kölsche_Jung("Kölsche_Jung", 1)
                else:
                    print("Invalid input. Try again. ")
                self.current_player = self.player1
                choice_bot_2 = input(f"Hello {self.player2.name}, do you want to play RandomBot, Silly, MinimaxBot, MonteCarloBot, Blocker or Koelsche_Jung? (1/2/3/4/5/6): ")
                if choice_bot_2 == "1":
                    self.player2 = GomokuBot("GomokuBot_2", 2)
                elif choice_bot_2 == "2":
                    self.player2 = Silly("Silly", 2)
                elif choice_bot_2 == "3":
                    self.player2 = MinimaxBot("MinimaxBot_2", 2)
                elif choice_bot_2 == "4":
                    self.player2 = MonteCarloBot("MonteCarloBot_2", 2)
                elif choice_bot_2 == "5":
                    self.player2 = Blocker("Blocker_2", 2)
                elif choice_bot_2 == "6":
                    self.player2 = Kölsche_Jung("Kölsche_Jung_2", 2)
                num_games = input("How many games do you want to play? (1-10000): ")
                try:
                    for game_number in range(int(num_games)):
                            print(f"Spiel {game_number + 1} von {num_games}")
                            self.game_loop()
                            self.game_arrays = []
                            self.board.reset_board()
                    print("Game over.")
                except ValueError:
                    print("Invalid input.")
        except ValueError:
            print("Invalid input. Try again.")

    def start_spanish(self):
        try:
            start_choice = input("¡Juguemos cinco seguidos! ¿Quieres o debería jugar el ordenador? (1/2): ")
            if start_choice == "1":
                self.valid_name_player_spanish()
                choice = input(f"Hola {self.player1.name}, quieres o juegas contra otro jugador o contra el ordenador? (1/2): ")
                if choice == "1":
                    self.player2.name = input("Jugador 2: ")
                    self.whos_first_spanish()
                elif choice == "2":
                    choice = input(f"Hola {self.player1.name}, elige entre RandomBot, Silly, MinimaxBot, MonteCarloBot, Blocker o Kölsche_Jung? (1/2/3/4/5/6): ")
                    if choice == "1":
                        self.player2 = GomokuBot("GomokuBot", 2)
                        self.whos_first_spanish()
                    elif choice == "2":
                        self.player2 = Silly("Silly", 2)
                        self.whos_first_spanish()
                    elif choice == "3":
                        self.player2 = MinimaxBot("MinimaxBot", 2)
                        self.whos_first_spanish()
                    elif choice == "4":
                        self.player2 = MonteCarloBot("MonteCarloBot", 2)
                        self.whos_first_spanish()
                    elif choice == "5":
                        self.player2 = Blocker("Blocker", 2)
                        self.whos_first_spanish()
                    elif choice == "6":
                        self.player2 = Kölsche_Jung("Kölsche_Jung", 2)
                        self.whos_first_spanish()
                    else:
                        print("No número válido. ")
            elif start_choice == "2":
                choice_bot_1 = input("¿Quieres que RandomBot, Silly, MinimaxBot, MonteCarloBot, Blocker o Kölsche_Jung sea el jugador uno? (1/2/3/4/5/6): ")
                if choice_bot_1 == "1":
                    self.player1 = GomokuBot("GomokuBot", 1)
                elif choice_bot_1 == "2":
                    self.player1 = Silly("Silly", 1)
                elif choice_bot_1 == "3":
                    self.player1 = MinimaxBot("MinimaxBot", 1)
                elif choice_bot_1 == "4":
                    self.player1 = MonteCarloBot("MonteCarloBot", 1)
                elif choice_bot_1 == "5":
                    self.player1 = Blocker("Blocker", 1)
                elif choice_bot_1 == "6":
                    self.player1 = Kölsche_Jung("Kölsche_Jung", 1)
                else:
                    print("No número válido. ")
                self.current_player = self.player1
                choice_bot_2 = input("¿Quieres que RandomBot, Silly, MinimaxBot, MonteCarloBot, Blocker o Kölsche_Jung sea el jugador dos? (1/2/3/4/5/6): ")
                if choice_bot_2 == "1":
                    self.player2 = GomokuBot("GomokuBot_2", 2)
                elif choice_bot_2 == "2":
                    self.player2 = Silly("Silly", 2)
                elif choice_bot_2 == "3":
                    self.player2 = MinimaxBot("MinimaxBot_2", 2)
                elif choice_bot_2 == "4":
                    self.player2 = MonteCarloBot("MonteCarloBot_2", 2)
                elif choice_bot_2 == "5":
                    self.player2 = Blocker("Blocker_2", 2)
                elif choice_bot_2 == "6":
                    self.player2 = Kölsche_Jung("Kölsche_Jung_2", 2)
                num_games = input("¿Cuántas rondas quieres jugar? (1-10000): ")
                try:
                    for game_number in range(int(num_games)):
                            print(f"Juego {game_number + 1} de {num_games}")
                            self.game_loop()
                            self.game_arrays = []
                            self.board.reset_board()
                    print("Todos los juegos han sido jugados.")
                except ValueError:
                    print("No número válido.")
        except ValueError:
            print("No número válido.")

    def create_board(self, m=15, n=15, k=5):
        self.spielbrett = Board(m, n, k)


    def valid_name_player_german(self):
        while True:
            self.player1.name = input("Bitte geben Sie Ihren Namen ein: ")
            if self.player1.name.isdigit() or not self.player1.name:
                print("Ungültiger Name. Bitte gib einen Namen mit Buchstaben ein.")
            else:
                break

    def valid_name_player_english(self):
        while True:
            self.player1.name = input("Please enter your name: ")
            if self.player1.name.isdigit() or not self.player1.name:
                print("Invalid name. Please enter a name with letters.")
            else:
                break

    def valid_name_player_spanish(self):
        while True:
            self.player1.name = input("Por favor, introduce su nombre: ")
            if self.player1.name.isdigit() or not self.player1.name:
                print("Nombre inválido. Por favor, insira um nome con letras.")
            else:
                break

    def whos_first_german(self):
        order_choice = input(f"Möchtest du anfangen, {self.player1.name}? (j/n): ")
        if order_choice.lower() == "n":
            self.current_player = self.player2 
            self.game_loop()
        else:
            self.game_loop()

    def whos_first_english(self):
        order_choice = input(f"Would you like to start, {self.player1.name}? (y/n): ")
        if order_choice.lower() == "n":
            self.current_player = self.player2
            self.game_loop()
        else:
            self.game_loop()
    
    def whos_first_spanish(self):
        order_choice = input(f"Desea comenzar, {self.player1.name}? (s/n): ")
        if order_choice.lower() == "n":
            self.current_player = self.player2
            self.game_loop()
        else:
            self.game_loop()

    def switch_player(self):
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def game_loop(self):
            game_over = False
            self.starter = self.current_player.name
            start_time = time.time()
            while not game_over:
                valid_move = True
                self.board.print_board()
                start_turn_time = time.time()
                if isinstance(self.current_player, GomokuBot):
                    valid_move = GomokuBot.place_piece(self.current_player, self, self.board)
                elif isinstance(self.current_player, Silly):
                    valid_move = Silly.make_move(self.current_player, self, self.board)
                elif isinstance(self.current_player, MinimaxBot):
                    MinimaxBot.make_move(self.current_player, self, self.board)
                elif isinstance(self.current_player, MonteCarloBot):
                    valid_move = MonteCarloBot.place_piece(self.current_player, self, self.board)
                elif isinstance(self.current_player, Blocker):
                    valid_move = Blocker.blocking(self.current_player, self, self.board)
                elif isinstance(self.current_player, Kölsche_Jung):
                    valid_move = Kölsche_Jung.halt_op(self.current_player, self, self.board)
                elif isinstance(self.current_player, Player):
                    try:
                        if self.language == "1":
                            row = int(input(f"Spieler {self.current_player.name}, geben Sie die Zeilennummer ein (0-{self.m-1}): "))
                            col = int(input(f"Spieler {self.current_player.name}, geben Sie die Spaltennummer ein (0-{self.n-1}): "))
                        elif self.language == "2":
                            row = int(input(f"Player {self.current_player.name}, please enter the row number (0-{self.m-1}): "))
                            col = int(input(f"Player {self.current_player.name}, please enter the column number (0-{self.n-1}): "))
                        elif self.language == "3":
                            row = int(input(f"Jugador {self.current_player.name}, introduzca el número de fila (0-{self.m-1}): "))
                            col = int(input(f"Jugador {self.current_player.name}, introduzca el número de columna (0-{self.n-1}): "))
                    except ValueError:
                        if self.language == "1":
                            print("Bitte geben Sie gültige ganze Zahlen ein.")
                        elif self.language == "2":
                            print("Please enter valid integers.")
                        elif self.language == "3":
                            print("Por favor, introduzca números enteros válidos.")
                        continue
                    valid_move = Player.place_piece(self.current_player, row, col, self, self.board)
                    if not valid_move:
                        if self.language == "1":
                            print("Bitte geben Sie eine gültige Zahl ein.")
                        elif self.language == "2":
                            print("Please enter a valid number.")
                        elif self.language == "3":
                            print("Por favor, introduzca un número válido.")
                        continue
                if self.board.is_winner(self.current_player.player_number):
                    game_over = True
                    self.board.print_board()
                    end_time = time.time()
                    self.winner = self.current_player.name
                    if self.language == "1":
                        print(f"Gesamtspieldauer: {end_time - start_time} Sekunden.")
                    elif self.language == "2":
                        print(f"Total time: {end_time - start_time} Seconds.")
                    elif self.language == "3":
                        print(f"Tiempo total: {end_time - start_time} Segundos.")
                    Daisy.save_game_state(game)
                    if self.language == "1":
                        print(f"Spieler {self.current_player.name} hat gewonnen!")
                        play_again = input("Wollen Sie eine neue Runde spielen? [Ja (1) oder Nein (2)]: ")
                        if play_again.lower() == '1':
                            how_again = input("Möchtest du die gleiche Runde spielen? [Ja (1) oder Nein (2)]: ")
                            if how_again == '1':
                                self.board.reset_board()
                                self.game_loop()
                            else:
                                self.start()
                        else:
                            print("Das Spiel ist zu Ende! Danke für's Teilnehmen!")
                            self.give_review()
                    elif self.language == "2":
                        print(f"Player {self.current_player.name} has won!")
                        play_again = input("Do you want to play another round? [Yes (1) or No (2)]: ")
                        if play_again.lower() == '1':
                            how_again = input("Would you like to play the same round? [Yes (1) or No (2)]: ")
                            if how_again == '1':
                                self.board.reset_board()
                                self.game_loop()
                            else:
                                self.start()
                        else:
                            print("Game over! Thanks for playing!")
                            self.give_review()
                    elif self.language == "3":
                        print(f"¡El jugador {self.current_player.name} ha ganado!")
                        play_again = input("¿Quieres jugar otra ronda? [Sí (1) o No (2)]: ")
                        if play_again.lower() == '1':
                            how_again = input("¿Te gustaría jugar la misma ronda? [Sí (1) o No (2)]: ")
                            if how_again == '1':
                                self.board.reset_board()
                                self.game_loop()
                            else:
                                self.start()
                        else:
                            print("¡Juego terminado! ¡Gracias por jugar!")
                            self.give_review()
                elif self.board.is_full():
                    game_over = True
                    self.board.print_board()
                    end_time = time.time()
                    print(f'Gesamtspieldauer: {end_time - start_time} Sekunden')
                    Daisy.save_game_state(game)
                    if self.language == "1":
                        print("Das Spiel endet unentschieden!")
                        self.give_review()
                    elif self.language == "2":
                        print("The game ends in a draw!")
                        self.give_review()
                    elif self.language == "3":
                        print("¡El juego termina en empate!")
                        self.give_review()
                else:
                    if valid_move:
                        end_turn_time = time.time()
                        self.game_arrays.append(copy.deepcopy(self.board.board))
                        try:
                            print(f'Spielzugdauer: {end_turn_time - start_turn_time} Sekunden')
                        except:
                            pass
                        self.switch_player()

    def give_review(self):
        if self.language == "1":
            review_prompt = "Möchten Sie das Spiel bewerten? [Ja (1) oder Nein (2)]: "
            star_prompt = "Wie viele Sterne geben Sie dem Spiel? (1-5): "
            thanks_message = "Wir wünschen Ihnen noch einen angenehmen Tag!"
            goodbye_message = "Bis zum nächsten Mal!"
            star_words = ["0 Sterne", "1 Stern", "2 Sterne", "3 Sterne", "4 Sterne", "5 Sterne"]
        elif self.language == "2":
            review_prompt = "Would you like to review the game? [Yes (1) or No (2)]: "
            star_prompt = "How many stars would you rate the game? (1-5): "
            thanks_message = "We wish you a pleasant day!"
            goodbye_message = "Until next time!"
            star_words = ["0 stars", "1 star", "2 stars", "3 stars", "4 stars", "5 stars"]
        elif self.language == "3":
            review_prompt = "¿Te gustaría revisar el juego? [Sí (1) o No (2)]: "
            star_prompt = "¿Cuántas estrellas le darías al juego? (1-5): "
            thanks_message = "¡Le deseamos un día agradable!"
            goodbye_message = "¡Hasta la próxima!"
            star_words = ["0 estrellas", "1 estrella", "2 estrellas", "3 estrellas", "4 estrellas", "5 estrellas"]
        review = input(review_prompt)
        if review.lower() == '1':
            review = input(star_prompt)
            if review.isdigit() and 0 <= int(review) <= 5:
                review = int(review)
                stars_text = star_words[review]
                review_count = [0] * len(star_words)
                review_count[review] += 1

                data = {"Bewertung": star_words, "Anzahl": review_count}
                statistic = pd.DataFrame(data)
                print(statistic.to_string(index=False, header=False))
                print(goodbye_message)
        else:
            print(thanks_message)

Daisy = Data_Science("game_history.pkl")
Spielbrett = Board()
game = Game(Spielbrett)
game.start()
