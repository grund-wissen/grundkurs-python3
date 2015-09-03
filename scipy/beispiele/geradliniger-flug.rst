Geradliniger Flug
=================

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wxmax1001/D1006_F_MO_PU_Textaufgabe_geradliniger_Flug.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.

Bei dieser Aufgabe geht es darum, eine physikalische Bewegungsgleichung zu
lösen.

*Aufgabe:*

Zwei Flugzeuge verlassen einen Flughafen zur selben Zeit in entgegengesetzte
Richtungen mit den Geschwindigkeiten :math:`v_1 = \unit[490]{km/h}`
beziehungsweise :math:`v_2 = \unit[368]{km/h}`. Nach welcher Zeit :math:`t`
haben sie einen Abstand von :math:`s=\unit[3805]{km}` erreicht?

*Lösung:*

Die beiden Flugzeuge bewegen sich mit der Summe ihrer Geschwindigkeiten, also
mit :math:`v=v_1 + v_2 = \unit[858]{km/h}` auseinander. Aus der Weg-Zeig-Formel
:math:`s = v \cdot t` für Bewegungen mit konstanter Geschwindigkeit lässt sich
die gesuchte Größe :math:`t` berechnen. Der :ref:`Sympy <Sympy>`-Code dazu lautet:

.. code-block:: python

    import sympy as sy

    # Sympy-Variablen initiieren:
    s = sy.S( 3805 )
    v = sy.S(  858 )
    t = sy.S(  't' )

    # Gleichung formulieren:
    equation = sy.Eq( s , v * t )

    # Gleichung lösen:
    result = sy.solve(equation)

    # Ergebnis: [3805/858]

    # Ergebnis als Fließkommazahl ausgeben:
    float(result[0])

    # Ergebnis: 4.434731934731935

Die gesuchte Zeit beträgt somit rund :math:`\unit[4,435]{Stunden}`. Etwas
eleganter ist allerdings die Angabe in Stunden und Minuten. Sie kann
aus dem obigen Ergebnis folgendermaßen berechnet werden:

.. code-block:: python

    import math

    result_f = float(result[0])

    hours = math.floor(result_f)
    # Ergebnis: 4.0

    minutes = (result_f - math.floor(result_f)) * 60
    # Ergebnis: 26.083916083916083

Die gesuchte Zeit beträgt somit rund :math:`4` Stunden und :math:`26` Minuten.


