.. _Quadratfläche aus Diagonale:

Quadratfläche aus Diagonale
===========================

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wxmax1001/D1006_F_MO_PU_Textaufgabe_geradliniger_Flug.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.


Bei dieser Aufgabe geht es um die Formulierung und das Lösung einer
geometrischen Funktionsgleichung.

*Aufgabe:*

Gegeben ist die Diagonale :math:`d = 3 \cdot \sqrt{2}` eines Quadrats. Wie
lässt sich daraus die Fläche :math:`A` des Quadrats berechnen?


*Lösung:*

Allgemein gilt für die Diagonale :math:`d` eines Quadrats in Abhängigkeit von
der Seitenlänge :math:`a`:

.. math::

    d = \sqrt{2} \cdot a

Umgekehrt gilt somit für die Seitenlänge :math:`a` in Abhängigkeit von
:math:`d`:

.. math::

    a = \frac{d}{\sqrt{2}}

Somit lässt sich aus :math:`d` die Seitenlänge :math:`a` und damit die Fläche
:math:`A = a^2` des Quadrats berechnen. Ein Beispielcode mit :ref:`Sympy
<Sympy>`  kann beispielsweise so aussehen:

.. code-block:: python

    import sympy as sy

    # Sympy-Variablen initiieren:
    d = sy.S( 3 * sy.sqrt(2) )
    a = sy.S( 'a' )

    # Seitenlänge berechnen:
    a = d / sy.sqrt(2)

    # Fläche berechnen:
    A = a**2

    # Ergebnis: 9

Die Fläche des Quadrats beträgt somit :math:`9` Flächeneinheiten.

