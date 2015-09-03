.. _Quaderliste - minimales oder maximales Volumen:

Quaderliste - minimales oder maximales Volumen
==============================================

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wxmax1001/D1013_F_MO_Quader_minimales_und_maximales_Volumen.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.


Diese Aufgabe lässt sich -- ebenfalls wie die vorherige Aufgabe
:ref:`Quaderliste -- Volumen und Oberfläche` mit der Python-Standardbibliothek
lösen. Zu bestimmen ist das Minimum bzw. Maximimum einer Liste an Werten.


*Aufgabe:*

Gegeben ist folgende Liste an Quadergrößen (Länge, Breite, Höhe):

[(3,4,5),(6,8,10),(1,2,4),(12,13,32), (14,8,22),(17,3,44),(12,5,3),(10,9,11)]

Bestimme das Minumum und Maximum der Quadervolumina, die sich anhand der obigen
Längenmaße ergeben.


*Lösung:*

Das Volumen der einzelnen Quader lässt sich als Produkt der drei Längenangaben
berechnen:

.. math::

    V _{\rm{Quader}} = l \cdot b \cdot h

.. code-block:: python


    # Variablen initiieren:
    cuboid_dimensions = [(3,4,5), (6,8,10), (1,2,4), (12,13,32), (14,8,22),
        (17,3,44), (12,5,3), (10,9,11)
        ]

    # Volumina berechnen:
    cuboid_volumina = [ l * b * h for l,b,h in cuboid_dimensions]

    # Minimum und Maximum bestimmen:
    cuboid_volume_min = min(cuboid_volume_max)
    cuboid_volume_max = max(cuboid_volume_max)

    # Ergebnis: 8 bzw. 4992

Zur Erstellung der Volumina-Liste wurden hierbei eine so genannte `List
Comprehension
<https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions>`_
genutzt. Möchte man wissen, welches Listenelement zum Wert des minimalen bzw.
maximalen Volumens gehört, so kann man die Listen-Index-Funktion nutzen:

.. code-block:: python

    # Position des Minimums bzw. Maximums in der Liste bestimmen:
    cuboid_volumina.index(cuboid_volume_min)
    cuboid_volumina.index(cuboid_volume_min)

    # Ergebnis: 2 bzw. 3

Python beginnt mit der Indizierung von Listenelementen bei Null, so dass die
Ergebniswerte dem dritten und vierten Listenelement entsprechen.

