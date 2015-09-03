
Zahlenrätsel (Division)
=======================

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wxmax1001/D1002_F_MO_PU_Zahlenraetsel_Division.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.

Bei dieser Aufgabe handelt es sich um eine Knobelaufgabe bzw. um eine einfache
Übungsaufgabe für lineare Gleichungssysteme.

*Aufgabe:*

Die Problemstellung lautet eine Zahl :math:`x` zu finden, die, wenn sie durch
:math:`(x-a)` geteilt wird, eine gegebene Zahl :math:`b` ergibt (:math:`a` sei
ebenfalls ein bekannter, konstanter Wert). Die Aufgabe soll für :math:`a = 10`
und :math:`b = 1\frac{5}{21}` gelöst werden.

*Lösung:*

Es muss prinzipiell folgende Gleichung gelöst werden:

.. math::

    \frac{x}{x-a} = b

Für :math:`a=10` und :math:`b = 1 \frac{5}{21}` lautet die Gleichung konkret:

.. math::

    \frac{x}{x-10} = 1 \frac{5}{21}

Diese Gleichung kann bereits ohne weitere Vereinfachungen mittels :ref:`Sympy
<Sympy>` gelöst werden. Der Code dazu lautet folgendermaßen:


.. code-block:: python

    import sympy as sy

    # Sympy-Variablen initiieren:
    x    = sy.S( 'x' )
    a, b = sy.S( [10, 1+5/21] )

    # Gleichung formulieren:
    equation = sy.Eq( x/(x-a) , b )

    # Gleichung lösen:
    sy.solve(equation)

    # Ergebnis: [52.0000000000000]

Das Ergebnis der Aufgabe lautet somit :math:`x=52`.


