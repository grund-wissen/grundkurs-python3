Leistungsaufgabn
================

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wxmax1001/D1007_F_MO_PU_Leistungsaufgabe.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.

Bei dieser Aufgabe handelt es sich um ein einfaches Dreisatzproblem.

*Aufgabe:*

Eine Anzahl von :math:`n_1=8` Bauarbeitern, alle mit gleicher Leistung, benötigt
:math:`t_1=87` Tage, um ein Haus zu bauen. Wie viele Tage :math:`t_2` sind zum
Hausbau nötig, wenn :math:`n_2=24` Bauarbeiter mit der selben Leistung daran
arbeiten?

*Lösung:*

Diese Dreisatzaufgabe lässt sich als einfach Verhältnisgleichung darstellen. Da
die insgesamt benötigte Zeit als indirekt proportional zur Anzahl der Arbeiter
angenommen wird, ist das Verhältnis :math:`\frac{t_1}{t_2}` der benötigen Zeiten
gleich dem Verhältnis :math:`\frac{n_2}{n_1}` der Arbeiterzahlen:

.. math::

    \frac{t_1}{t_2} = \frac{n_1}{n_2}

Diese Gleichung lässt sich auch ohne Computer-Algebra-System leicht nach
:math:`t_2` auflösen (insbesondere, wenn man auf beiden Seiten die Kehrwerte
bildet, d.h. die Gleichung :math:`\frac{t_2}{t_1} = \frac{n_1}{n_2}`
betrachtet). Dennoch soll an dieser Stelle die Aufgabe als Beispiel für vielfach
vorkommende Dreisatzaufgaben mit :ref:`Sympy <Sympy>` gelöst werden:

.. code-block:: python

    import sympy as sy

    # Sympy-Variablen initiieren:
    n1, n2 = sy.S( [8, 24] )
    t1 = sy.S( 87 )
    t2 = sy.S( 't2' )

    # Gleichung formulieren:
    equation = sy.Eq( t1/t2 , n2/n1 )

    # Gleichung lösen:
    result = sy.solve(equation)

    # Ergebnis: [29]

Die gesuchte Zeit beträgt somit :math:`t_2 = \unit[29]{Tage}`.


