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

.. _numpy.arange():

.. rubric:: Eindimensionale Arrays mittels ``arange()`` und ``linspace()``

Mittels der Funktion ``arange()`` kann ein (eindimensionales) Numpy-Array auf
Grundlage eines Zahlenbereichs erstellt werden:

.. code-block:: python

    # Numpy-Array aus Zahlenbereich mit angegebener Schrittweite erstellen:
    # Syntax: np.arange(start, stop, step)

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

.. _numpy.linspace():

Eine zweite, sehr ähnliche Möglichkeit zur Erstellung eines Numpy-Arrays bietet
die Funktion ``linspace()``: Bei dieser wird allerdings die Anzahl der Schritte
zwischen dem Start- und dem Endwert angegeben; die Schrittweite wird dann
automatisch berechnet.

.. code-block:: python

    # Numpy-Array aus Zahlenbereich mit angegebener Listen-Länge erstellen:
    # Syntax: np.arange(start, stop, num)

    l = np.linspace(0, 10, 100, endpoint=True)

    l
    # Ergebnis:
    # array([  0.        ,   0.1010101 ,   0.2020202 ,   0.3030303 ,
    #      0.4040404 ,   0.50505051,   0.60606061,   0.70707071,
    #      0.80808081,   0.90909091,   1.01010101,   1.11111111,
    #      1.21212121,   1.31313131,   1.41414141,   1.51515152,
    #      1.61616162,   1.71717172,   1.81818182,   1.91919192,
    #      2.02020202,   2.12121212,   2.22222222,   2.32323232,
    #      2.42424242,   2.52525253,   2.62626263,   2.72727273,
    #      2.82828283,   2.92929293,   3.03030303,   3.13131313,
    #      3.23232323,   3.33333333,   3.43434343,   3.53535354,
    #      3.63636364,   3.73737374,   3.83838384,   3.93939394,
    #      4.04040404,   4.14141414,   4.24242424,   4.34343434,
    #      4.44444444,   4.54545455,   4.64646465,   4.74747475,
    #      4.84848485,   4.94949495,   5.05050505,   5.15151515,
    #      5.25252525,   5.35353535,   5.45454545,   5.55555556,
    #      5.65656566,   5.75757576,   5.85858586,   5.95959596,
    #      6.06060606,   6.16161616,   6.26262626,   6.36363636,
    #      6.46464646,   6.56565657,   6.66666667,   6.76767677,
    #      6.86868687,   6.96969697,   7.07070707,   7.17171717,
    #      7.27272727,   7.37373737,   7.47474747,   7.57575758,
    #      7.67676768,   7.77777778,   7.87878788,   7.97979798,
    #      8.08080808,   8.18181818,   8.28282828,   8.38383838,
    #      8.48484848,   8.58585859,   8.68686869,   8.78787879,
    #      8.88888889,   8.98989899,   9.09090909,   9.19191919,
    #      9.29292929,   9.39393939,   9.49494949,   9.5959596 ,
    #      9.6969697 ,   9.7979798 ,   9.8989899 ,  10.        ])

Setzt man im obigen Beispiel ``endpoint=False``, so ist das mit ``linspace()``
erzeugte Array ``l`` mit dem Array ``r`` aus dem vorherigen Beispiel identisch.

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

.. rubric:: Links

* `Numpy-Tutorial (en.) von Nicolas P. Rougier
  <http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html>`__
* `100 Numpy Exercises (en.)
  <http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html>`__



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
 
