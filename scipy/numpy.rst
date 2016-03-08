.. index:: numpy
.. _Numpy:

``numpy`` -- eine Bibliothek für numerische Berechnungen
========================================================

`Numpy <http://www.numpy.org/>`__ ist eine Python-Bibliothek mit Datentypen und
Funktionen, die für numerische Berechnungen optimiert sind. Meist lassen sich
solche Aufgaben zwar auch mit den normalen Python-Funktionen berechnen, gerade
bei großen Zahlenmengen ist Numpy allerdings wesentlich schneller.

Numpy ist nicht im Python3-Standard enthalten und muss daher separat installiert
werden :

.. code-block:: python

    sudo aptitude install python3-numpy

    # oder easy_install3 numpy nach Installation von python3-setuptools

Der zentrale Objekttyp in Numpy ist das ``ndarray`` (meist kurz "Array"
genannt), das viele Gemeinsamkeiten mit der normalen `Liste` aufweist. Ein
wesentlicher Unterschied besteht allerdings darin, dass alle im Array
gespeicherten Elemente den gleichen Objekttyp haben müssen. Die Größe von
Numpy-Arrays kann zudem nicht verändert werden, und es sind keine leeren Objekte
erlaubt. Durch derartige Eigenschaften können Numpy-Arrays vom
Python-Interpreter schneller durchlaufen werden. Darüber hinaus stellt Numpy
etliche grundlegende Funktionen bereit, um mit den Inhalten solcher Arrays zu
arbeiten und/oder Änderungen an solchen Arrays vorzunehmen.


.. _Numpy-Arrays erstellen:

Numpy-Arrays erstellen
----------------------

Ein neues Numpy-Array kann folgendermaßen aus einer normalen Liste, deren
Elemente alle den gleichen Datentyp haben müssen, erzeugt werden:

.. code-block:: python

    import numpy as np

    nums = [1,2,3,4,5]

    # Eindimensionales Array erstellen:
    a = np.array(nums)

    a
    # Ergebnis: array([1, 2, 3, 4, 5])

Die beim Funktionsaufruf von ``array()`` übergebene Liste kann auch
aus mehreren Teillisten bestehen, um beispielsweise zeilenweise die Werte einer
Matrix als Numpy-Array zu speichern:

.. code-block:: python

    # Zweidimensionale Matrix erstellen
    m1 = np.array([ [1,2,3], [4,5,6], [7,8,9] ])

    m1
    # Ergebnis:
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

Durch ein zweites Argument kann beim Aufruf der ``array()``-Funktion der
Datentyp der Elemente explizit festgelegt werden. Beispielsweise könnten im
obigen Beispiel durch eine zusätzliche Angabe von ``dtype=float`` die in der
Liste enthaltenen Integer-Werte automatisch in Gleitkomma-Zahlen umgewandelt
werden.

Da auch Matrizen voller Nullen oder Einsen häufig vorkommen, können diese
mittels der dafür vorgesehenen Funktionen ``zeros()`` bzw. ``ones()`` erzeugt
werden. Dabei wird als erstes Argument ein Tupel als Argument angegeben, welches
die Anzahl an Zeilen und Spalten der Matrix festlegt, sowie als zweites Argument
wiederum optional der Datentyp der einzelnen Elemente:

.. code-block:: python

    # 2x3-Matrix aus Nullen erstellen:

    # Zweidimensionale Matrix erstellen
    m2 = np.zeros( (2,3), int)

    m2
    # Ergebnis:
    # array([[0, 0, 0],
    #    [0, 0, 0]])

Zudem kann mittels der Funktion ``arange()`` ein Array auf Grundlage eines
Zahlenbereichs erstellt werden:

.. code-block:: python

    # Numpy-Array aus Zahlenbereich erstellen:
    r = np.arange(0, 10, 0.1)

    r
    # Ergebnis:
    # array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ,
    #         1.1,  1.2,  1.3,  1.4,  1.5,  1.6,  1.7,  1.8,  1.9,  2. ,  2.1,
    #         2.2,  2.3,  2.4,  2.5,  2.6,  2.7,  2.8,  2.9,  3. ,  3.1,  3.2,
    #         3.3,  3.4,  3.5,  3.6,  3.7,  3.8,  3.9,  4. ,  4.1,  4.2,  4.3,
    #         4.4,  4.5,  4.6,  4.7,  4.8,  4.9,  5. ,  5.1,  5.2,  5.3,  5.4,
    #         5.5,  5.6,  5.7,  5.8,  5.9,  6. ,  6.1,  6.2,  6.3,  6.4,  6.5,
    #         6.6,  6.7,  6.8,  6.9,  7. ,  7.1,  7.2,  7.3,  7.4,  7.5,  7.6,
    #         7.7,  7.8,  7.9,  8. ,  8.1,  8.2,  8.3,  8.4,  8.5,  8.6,  8.7,
    #         8.8,  8.9,  9. ,  9.1,  9.2,  9.3,  9.4,  9.5,  9.6,  9.7,  9.8,
    #         9.9])

Die Funktion ``arange()`` verhält sich also genauso wie die Funktion
:ref:`range() <range()>`, liefert allerdings ein Numpy-Array mit den
entsprechenden Werten als Ergebnis zurück. [#]_


.. _Inhalte von Numpy-Arrays abrufen und verändern:

Inhalte von Numpy-Arrays abrufen und verändern
----------------------------------------------

Entspricht ein Numpy-Array einem eindimensionalen Vektor, so kann auf die
einzelnen Elemente in gleicher Weise wie bei einer Liste zugegriffen werden:

.. code-block:: python

    nums = [1,2,3,4,5]

    a = np.array(nums)

    a[3]
    # Ergebnis: 4

    a[-1]
    # Ergebnis: 5

Als positive Indizes sind Werte zwischen ``i >= 0`` und ``i < len(array)``
möglich; sie liefern jeweils den Wert des ``i+1``-ten Listenelements als
Ergebnis zurück. Für negative Indizes sind Werte ab ``i <= -1`` möglich; sie
liefern jeweils den Wert des ``i``-ten Listenelements -- vom Ende der Liste her
gerechnet -- als Ergebnis zurück. Die Indizierung kann ebenso genutzt werden, um
den Inhalt des Arrays an einer bestimmten Stelle zu verändern:

.. code-block:: python

    a[-1] = 10

    a
    # Ergebnis: array([1, 2, 3, 4, 10])

Um auf Zahlenbereiche innerhalb eines Numpy-Arrays zuzugreifen, können wiederum
-- wie bei der Indizierung von :ref:`Listen und Tupeln <Indizierung von Listen
und Tupeln>` -- so genannte :ref:`Slicings <slice()>` genutzt werden.
Dabei wird innerhalb des Indexoperators ``[]`` der auszuwählende Bereich mittels
der Syntax ``start:stop`` festgelegt, wobei für ``start`` und ``stop`` die
Index-Werte der Bereichsgrenzen eingesetzt werden:

.. code-block:: python

    r = np.arange(10)

    # Intervall selektieren:

    r[3:8]
    # Ergebnis: array([3, 4, 5, 6, 7])

    # Jedes zweite Element im angegebenen Intervall auswählen:

    r[3:8:2]
    # Ergebnis: array([3, 5, 7])

Wie üblich wird bei Slicings die untere Grenze ins Intervall mit eingeschlossen,
die obere nicht. Mit der Syntax ``start:stop:step`` kann bei Slicings zudem
festgelegt werden, dass innerhalb des ausgewählten Zahlenbereichs nur jede durch
die Zahl ``step`` bezeichnete Zahl ausgewählt wird. Wird für ``start`` oder
``step`` kein Wert angegeben, so wird der ganze Bereich ausgewählt:

.. code-block:: python

    # Ab dem fünften Element (von hinten beginnend) jedes Element auswählen:

    r[5::-1]
    # Ergebnis: array([5, 4, 3, 2, 1, 0])

Slicings können bei Zuweisungen von neuen Werten auch auf der linken Seite des
``=``-Zeichens stehen. Auf diese Weise kann bisweilen auf eine ``for``-Schleife
verzichtet und der Code somit lesbarer gemacht werden.

Um in mehrdimensionalen Numpy-Arrays Werte zu selektieren, wird folgende Syntax
verwendet:

.. code-block:: python

    m = np.array([ [1,2,3], [4,5,6] ])

    m
    # Ergebnis:
    # array([[1, 2, 3],
    #    [4, 5, 6]])


    # Element in der zweiten Zeile in der dritten Spalte auswählen:

    m[1][2]
    # Ergebnis: 6

Bei Numpy-Arrays können die "Verschachtelungstiefen" wie bei Listen durch eine
mehrfache Anwendung des Index-Operators ``[]`` aufgelöst werden; ebenso ist für
das obige Beispiel allerdings auch die Syntax ``m3[1,2]`` erlaubt und auch
üblich. Bei der Auswahl eines Elements aus einer Matrix können also innerhalb
des Index-Operators die Zeile und Spalte durch ein Komma getrennt ausgewählt
werden; Slicings sind hierbei ebenfalls möglich.


.. _Funktionen für Numpy-Arrays:

Funktionen für Numpy-Arrays
---------------------------

Viele Funktionen wie die Betragsfunktion ``abs()``, die Wurzelfunktion
``sqrt()`` oder trigonometrische Funktionen wie ``sin()``, ``cos()`` und
``tan()``, die im ``math``-Modul definiert sind, existieren in ähnlicher Weise
auch im Numpy-Modul -- mit dem Unterschied, dass sie auf Numpy-Arrays angewendet
werden können. Dabei wird die jeweilige mathematische Funktion auf jedes
einzelne Element des Arrays angewendet, und als Ergebnis ebenfalls ein Array mit
den entsprechenden Funktionswerten zurück gegeben. [#]_

Ebenso können die gewöhnlichen Operationen ``+``, ``-``, ``*`` und ``/``
angewendet werden, um beispielsweise zu allen Elemente eines Numpy-Arrays eine
bestimmte Zahl zu addieren/subtrahieren oder um alle Elemente mit einer
bestimmten Zahl zu multiplizieren. Die Numpy-Funktionen erzeugen dabei stets
neue Numpy-Arrays, lassen die originalen Arrays also stets unverändert.

.. code-block:: python

    r = np.arange(10)

    r
    # Ergebnis: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8, 9])

    r+1
    # Ergebnis: array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

    r**2
    # Ergebnis: array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81])

    np.sqrt(r**4)
    # Ergebnis: array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81])

    np.sin(r)
    # Ergebnis: array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ,
    #  -0.95892427, -0.2794155 ,  0.6569866 ,  0.98935825,  0.41211849])

Zusätzlich gibt es in Numpy Funktionen, die speziell für Zahlenreihen und
Matrizen vorgesehen sind. Beispielsweise kann mit der Numpy-Funktionen
``argmin()`` und ``argmax()`` der Index des kleinsten und größten Elements in
einem Array gefunden werden. Wendet man diese Funktionen auf ein Matrix-Array
an, so erhält man diejenige Index-Nummer des kleinsten beziehungsweise größten
Elements, die sich bei einem eindimensionalen Array mit den gleichen Werten
ergeben würde. Ist man hingegen spalten- oder zeilenweise an den jeweiligen
Minima beziehungsweise Maxima interessiert, so kann beim Aufruf dieser beiden
Funktionen als zweites Argument  ``axis=0`` für eine spaltenweise Auswertung
oder ``axis=1`` für eine zeilenweie Auswertung angegeben werden:

.. code-block:: python

    a = np.array( [3,1,2,6,5,4] )
    m = np.array([ [3,1,2], [6,5,4] ])

    np.argmin(a)
    # Ergebnis: 1

    np.argmin(m)
    # Ergebnis: 1

    np.argmin(m, axis=0)
    # Ergebnis: array([0, 0, 0])

    np.argmin(m, axis=1)
    # Ergebnis: array([1, 2])

Für Matrix-Arrays existieren zusätzlich die Numpy-Funktionen ``dot()``,
``inner()`` und ``outer()``, mit deren Hilfe :ref:`Multiplikationen von Matrizen
<gwm:Multiplikation zweier Matrizen>` beziehungsweise Vektoren durchgeführt werden können.

... to be continued ...

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Auch bei der ``arange()``-Funktion ist die untere Grenze im Zahlenbereich
    enthalten, die obere jedoch nicht.

    Das optionale dritte Argument gibt, ebenso wie bei :ref:`range() <range()>`,
    die Schrittweite zwischen den beiden Zahlengrenzen an. Ist der Zahlenwert
    der unteren Bereichsgrenze größer als derjenige der oberen Bereichsgrenze,
    so muss ein negativer Wert als Schrittweite angegeben werden, andererseits
    bleibt das resultierende Array leer.

.. [#] Die gleichnamigen Funktionen aus dem ``math``-Modul können also auf
    einzelne Elemente eines Numpy-Arrays, nicht jedoch auf das ganze Array an
    sich angewendet werden. Letzteres könnte man zwar beispielsweies mittels
    einer ``for``-Schleife erreichen, doch die Ausführung des Codes bei
    Verwendung der Numpy-Varianten ist erheblich schneller.
 
