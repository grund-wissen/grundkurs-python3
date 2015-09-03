Altersaufgabe
=============

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wxmax1001/D1009_F_MO_PU_Altersaufgabe.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.


Bei dieser Aufgabe geht es um die Formulierung und das Lösung einer
Funktionsgleichung.

*Aufgabe:*

Wenn K. heute :math:`m=3` mal so alt wäre wie vor :math:`n=6` Jahren, dann wäre
K. nun :math:`j=38` Jahre älter. Wie alt ist K. heute?


*Lösung:*

Die gesuchte Variable :math:`x` gebe das heutige Alter von K. an. Dann lässt
sich aus den obigen Bedingungen folgende Gleichung aufstellen:

.. math::

    m * (x - n) = x + j

Diese Gleichung kann folgendermaßen mit :ref:`Sympy <Sympy>` gelöst werden:

.. code-block:: python

    import sympy as sy

    # Sympy-Variablen initiieren:
    x = sy.S( 'x' )
    m,n,j = sy.S([3, 6, 38] )

    # Gleichung formulieren:
    equation = sy.Eq( m * (x-n) , x + j )

    # Gleichung lösen:
    sy.solve(equation)

    # Ergebnis: [28]

\K. ist somit heute :math:`28` Jahre alt.

