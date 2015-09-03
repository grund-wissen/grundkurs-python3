
Punktspiegelung
===============

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wx1/D1015_F_MO_Punktspiegelung.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.

Bei sollen für einem gegebenen Punkt die Koordinaten eines neuen Punktes
bestimmt werden, der sich durch Spiegelung an der :math:`x`- oder
:math:`y`-Achse ergibt.

*Aufgabe:*

Eine bestimmter Punkt :math:`\rm{P}` soll entweder um die :math:`x`- oder
:math:`y`-Achse gespiegelt werden. Die Koordinaten des Punktes sowie die Wahl
der Spiegelungsachse sollen durch den Benutzer eingegeben werden.

*Lösung:*

Die Koordinaten des gespiegelten Punkts lassen sich einfach berechnen, indem die
jeweilige Koordinate mit ``(-1)`` multipliziert wird.

Um eine Eingabe von einem Benutzer zu erhalten, kann in Python die
``input()``-Funktion genutzt werden, welche die eigegebene Textzeile als
String-Variable speichert. Diese wird im folgenden Beispiels schrittweise
überarbeitet, indem zunächst mögliche runde Klammern mit der String-Funktion
``strip`` entfernt werden, der String anschließend am Kommazeichen in eine
Liste zweier Strings zerlegt wird, und zuletzt eine neue Liste mittels einer
List Comprehension anhand der Elemente der bestehenden Liste erstellt wird.
Dieser Schritt ist notwendig, um aus den als Strings gespeicherten Zahlenwerten
Float-Variablen zu erzeugen.


.. code-block:: python

    # Koordinaten des ursprünglichen Punktes einlesen:
    original_point = input("Bitte die Koordinaten des Punktes eingeben \
                            [ beispielsweise (3.0, -1.5) ]: ")
    axis = input("Um welche Achse soll gespiegelt werden [x oder y]? ")

    # Eingabe-String in Liste von Float-Werten umwandeln:
    opoint = [float(num) for num in original_point.strip('()').split(',')]

    new_point = []

    if axis == 'x':

        new_point.append( opoint[0] * (-1) )
        new_point.append( opoint[1] )

    if axis == 'y':

        new_point.append( opoint[0] )
        new_point.append( opoint[1] * (-1) )

    print("Der an der %s-Achse gespiegelte Punkt hat die \
            Koordinaten %s" % (axis, tuple(new_point)) )


Der obige Code zeigt nur die grundlegende Logik auf. In einem "richtigen"
Programm sollte die Eingabe nach falscher Syntax hin untersucht und
gegebenenfalls ein entsprechendes Exception-Handling vorgenommen werden.

..  Wird die Datenverarbeitung als Funktion implementiert, kann beispielsweise
..  innerhalb einer Schleife der Benutzer so lange nach der Eingabe eines neuen
..  Punkts gefragt werden, bis dieser die Schleife abbricht.


