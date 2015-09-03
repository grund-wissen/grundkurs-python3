Aufeinander folgende Zahlen
===========================

Bei dieser Aufgabe geht es um das Lösen einer Summengleichung.

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wxmax1001/D1008_F_MO_PU_aufeinanderfolgende_Zahlen.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.


*Aufgabe:*

Betrachtet wird eine Folge :math:`x _{\rm{n}}` von aufeinander folgenden,
ganzzahligen Werten :math:`(x,n \in \mathbb{N})`.

Die Summe :math:`\sum_{i=1}^{m_1} x _{\rm{i}}` der ersten :math:`m_1` Zahlen sei
um einen Differenzwert :math:`d` kleiner als die Summe :math:`\sum_{i=m_1+1}^{n}
x _{\rm{i}}` der restlichen Zahlen. Wie lässt sich diese Aufgabe mathematisch
formulieren? Welche Lösung ergibt sich für :math:`n=5`, :math:`m_1 = 2` und
:math:`d = 42`?

*Lösung:*

Damit die obige Bedingung erfüllt ist, muss folgende Gleichung gelten:

.. math::

    \sum_{i=1}^{m_1}(x_i) + d =  \sum_{i=m_1+1}^{n}(x_i)

Um diese Aufgabe mit ``sympy`` zu lösen, können beide Summen in der obigen
Gleichung auch in folgender Form dargestellt werden:

.. math::

    \sum_{i=1}^{m_1}(x + i) + d =  \sum_{i=m_1+1}^{n}(x + i)

Hierbei ist der zu bestimmende Initialwert :math:`x` um :math:`1` kleiner als
der erste Wert der Zahlenreihe. Diese Darstellung hat den Vorteil, dass die
Summen leichter formuliert werden können und die Gleichung nur noch eine
Unbekannte aufweist. Der Quellcode zur Lösung der Gleichung mittels :ref:`Sympy
<Sympy>`  kann beispielsweise so aussehen:

.. code-block:: python

    import sympy as sy

    # Sympy-Variablen initiieren:
    n,m1,d = sy.symbols('n m1 d')
    x,i = sy.symbols('x i')

    # Terme festlegen
    s1 = sy.summation(x + i, (i,1,m1))
    s2 = sy.summation(x + i, (i,m1+1,n))

    # Gleichungen formulieren:
    equation = sy.Eq( s1 + d , s2)
    equation_concrete = equation.subs({n:5,m1:2,d:42})

    # Gleichung(en) lösen:
    sy.solve(equation, x, 'dict')
    sy.solve(equation_concrete, x, 'dict')

    # Ergebnisse:

    # Allgemein:
    # [{x: (-d - m1**2 - m1 + n**2/2 + n/2)/(2*m1 - n)}]

    # Konkret:
    # [{x:33}]

Beim Lösen der Gleichung wurde hierbei explizit die Variable :math:`x` als
gesuchte Variable  angegeben; ebenso könnte die Gleichung beispielsweise nach
:math:`d` für einen gegebenen Startwert :math:`x` aufgelöst werden.

Das Ergebnis für die konkrete Aufgabe lautet :math:`x=33`. In diesem Fall sind
die :math:`n=5` Zahlen also gleich :math:`(34,35,36,37,38)`, die Summe der
ersten :math:`m_1=2` Zahlen ist :math:`s_1=34+35=69`, die Summe der weiteren
Zahlen ist gleich :math:`36+37+38 = 111`.


