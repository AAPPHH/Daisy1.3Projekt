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

darstellung matrix

Spielstatistiken:

Gewinnrate: Die Häufigkeit, mit der ein Spieler oder eine Strategie gewinnt.
Durchschnittliche Spielzüge: Die durchschnittliche Anzahl von Zügen, die für den Abschluss eines Spiels benötigt werden.
Spielzeit: Die durchschnittliche oder Gesamtdauer der Spiele.
Spieler- und Strategieanalyse:

Effektivität verschiedener Strategien: Wie gut bestimmte Strategien gegenüber anderen abschneiden.
Fehleranalyse: In welchen Situationen machen Spieler oder Algorithmen Fehler oder suboptimale Züge.
Anpassungsfähigkeit: Wie gut sich ein Spieler oder eine Strategie an unterschiedliche Spielstile oder unerwartete Züge des Gegners anpasst.
Spielverlaufsanalyse:

Häufige Muster und Formationen: Welche Markierungsmuster oder Formationen am häufigsten zum Gewinn führen.
Schlüsselzüge: Züge, die signifikant die Wahrscheinlichkeit des Gewinnens oder Verlierens ändern.
Spielphasen: Analyse der unterschiedlichen Phasen des Spiels (Anfang, Mitte, Ende) und wie Strategien sich in diesen Phasen ändern.
Computergestützte Analyse:

Suchtiefe und -effizienz: Bei Verwendung von Algorithmen wie Minimax oder Alpha-Beta-Pruning, wie tief und effizient sucht der Algorithmus.
Heuristische Bewertung: Effektivität der verwendeten heuristischen Methoden zur Bewertung von Spielbrettern.
Statistische Daten:

Verteilung der Gewinne nach Spieler: Gibt es einen signifikanten Unterschied in der Gewinnverteilung zwischen den Spielern?
Verteilung der Spielzüge: Welche Züge sind am häufigsten und welche führen am häufigsten zum Sieg?
Maschinelles Lernen:

Lernfortschritte: Wenn maschinelles Lernen eingesetzt wird, wie schnell und effizient verbessert sich der Algorithmus?
Strategieinnovation: Entwickelt der lernende Algorithmus neue, kreative oder unerwartete Strategien?
Die Auswertung dieser Faktoren kann Ihnen helfen, ein tieferes Verständnis für das Spiel und die beteiligten Strategien zu gewinnen. Sie können auch dazu beitragen, die Fähigkeiten eines KI-Spielers zu verbessern oder interessante Einblicke in das Spielverhalten von Menschen zu gewinnen.