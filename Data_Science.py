import pickle  # Import der Bibliothek "pickle"
               # -> Speicherung von Data-Frames
               # -> Serialisierung von Python-Instanzen
               # -> Konvertierung von Daten in eine binäre Form
               # -> ggf. Machine-Learning-Applikationen

class Data_Science:  # Erstellung der Klasse Data_Science
    def __init__(self, filename="game_history.pkl"):  # Konstruktor und Parameter: Name der Datei (Default)
        self.filename = filename  # -> self.filename = "game_history.pkl"

    def save_game_history(self, game_history):  # Definition der Methode, die die gesammelten Daten speichert
        with open(self.filename, "wb") as f:  # Öffnung der Datei im Binärmodus
            pickle.dump(game_history, f)  # game_history wird in die Datei geladen

    def load_game_history(self):  # Definition der Methode, die 
        try:  # Versuch...
            with open(self.filename, "rb") as f:  # ... die im Binärmodus gespeicherten Daten zu öffnen...
                return pickle.load(f)  # ... und zurückgegeben
        except FileNotFoundError:  # Wird die Datei nicht gefunden, ...
            return []  # ... dann wird eine leere Liste zurückgegeben
