.. _Quader:

Quader
======

Bei dieser einfachen Aufgabe soll anhand der Länge, Breite und Höhe
eines Quaders dessen Volumen, Oberfläche und Raumdiagonale bestimmt werden.

*Aufgabe:*

Bestimme zu den Massen :math:`l=10`, :math:`b=8` und :math:`c=6` das Volumen,
die Oberfläche und die Raumdiagonale eines Quaders.

*Lösung:*

Die gesuchten Größen lassen sich folgendermaßen berechnen:

.. math::

    V _{\rm{Quader}} &= h \cdot b \cdot l \\[4pt]
    A _{\rm{Quader}} &= 2 \cdot (h \cdot b + b \cdot l + l \cdot h) \\[4pt]
    d _{\rm{Quader}} &= \sqrt{l^2 + b^2 + h^2}

Die rechte Seite der letzten Gleichung entspricht dem Betrag eines
dreidimensionalen Vektors.

Zur Berechnung der Quaderdiagonale kann die Funktion ``sqrt()`` aus dem `math
<https://docs.python.org/3/library/math.html>`_-Modul genutzt werden:

.. code-block:: python

    import math as m
    import functools as ft

    cuboid_dimensions = [10,8,6]

    cuboid_volume = ft.reduce(lambda x,y: x*y , cuboid_dimensions)

    cuboid_surface = lambda
    cuboid_surface = 2 * (
        cuboid_dimensions[0] * cuboid_dimensions[1] +
        cuboid_dimensions[0] * cuboid_dimensions[2] +
        cuboid_dimensions[1] * cuboid_dimensions[2]
    )

    cuboid_diagonal = m.sqrt(
        cuboid_dimensions[0]**2 +
        cuboid_dimensions[1]**2 +
        cuboid_dimensions[2]**2
    )

    # Ergebnisse:

    # cuboid_volume:   480
    # cuboid_surface:  376
    # cuboid_diagonal: 14.142135623730951

Bei der Berechnung des Quadervolumens wurde, um Schreibarbeit zu sparen, die
Funktion ``reduce()`` aus dem `functools
<https://docs.python.org/3/library/functools.html>`_-Modul verwendet. Diese
führt die durch das erste Argument angegebene Funktion schrittweise von links
nach rechts auf alle Elemente einer als zweites Argument übergebenen Sequenz
aus; ein Aufruf von ``ft.reduce(lambda x,y: x*y, [1,2,3,4,5])``. würde
beispielsweise ``((((1*2)*3)*4)*5)`` berechnen.

Anstelle des Lambda-Ausdrucks (quasi einer Funktion ohne Namen) kann auch die
Funktion ``mul()`` aus dem Modul `operator
<https://docs.python.org/3/library/operator.html>`_ verwendet werden. Diese
wertet das Produkt aller Werte einer (als eingigem Argument übergebenen) Liste
aus:

.. code-block:: python

    import operator as op

    ft.reduce(op.mul, [1,2,3]) == ft.reduce(lambda x,y: x*y, [1,2,3])

    # Ergebnis: True

Zudem könnte die Schreibarbeit durch die Definition von Funktionen entsprechend
Aufgabe :ref:`Quaderliste -- Volumen und Oberfläche <Quaderliste -- Volumen und
Oberfläche>` weiter reduziert werden.


