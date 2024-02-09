# Daisy 1.3 Projekt

Wir Spielen k in a row!

Das Spiel wird durch das auführen der class_game.py gestartet.

Achtung!
Der MinimaxBot wie auch der Montecarlobot benötigen abhängig vom Spielstand zeit für ihr berechnung.
Diese wird jedoch kürzer sobald das spiel voran schreitet.

Für class_bot_4.py, welches die klasse MonteCarloBot beinhalter wir Ray benötigt.
Ray ermöglichet es uns 4 mal schneller Mögliche Spiele zu berechnen!
https://www.ray.io/
Ein pip install ray über einen Prompt ist erforderlich.

Minimax- und MonteCarlobot benutzen pickel um Spielstände für die schon einmal ein zug berechnet wurde zu Speichern.
Das passiert jedoch nur wenn der jewilige bot das spiel gewonnen hatt. 
So werden keine züge gespeichert die in diesem Spiel zu einer niederlage geführt haben.

Good Luck Have Fun! :D

"...(5,5,4) is a draw..."  Lustenberger, 1967

Spielverlaufsanalyse:

Schlüsselzüge: Züge, die signifikant die Wahrscheinlichkeit des Gewinnens oder Verlierens ändern.

Suchtiefe und -effizienz: Bei Verwendung von Algorithmen, wie tief und effizient sucht der Algorithmus.

Verteilung der Gewinne nach Spieler: Gibt es einen signifikanten Unterschied in der Gewinnverteilung zwischen den Spielern?

Lernfortschritte: Wenn maschinelles Lernen eingesetzt wird, wie schnell und effizient verbessert sich der Algorithmus?
Tf agent based Bot