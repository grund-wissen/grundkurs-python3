Lage eines Kreises und einer Gerade
===================================

Bei dieser Übungsaufgabe geht es das Gleichsetzen zweier geometrischer
Gleichungen.

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wx1/D1017_F_MO_Lage_Gerade_Kreis.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.


*Aufgabe:*

Für eine Kreis- und eine Geradengleichung ist die Lagebeziehung (Sekante,
Tangente, Passante) der beiden geometrischen Objekte zueinander zu bestimmen.

*Lösung:*

* Wenn eine Gerade einen Kreis in zwei Punkten schneidet, dann ist die Gerade eine Sekante.
* Wenn eine Gerade einen Kreis in einem Punkt berührt, dann ist die Gerade eine Tangente.
* Wenn die Gerade und der Kreis keinen Punkt gemeinsam haben, dann ist die Gerade eine Passante.

Mit :ref:`Sympy <Sympy>` kann die Aufgabe folgendermaßen gelöst werden:

.. code-block:: python

    import sympy as sy

    # Funktionsgleichungen als Strings einlesen:
    circle_equation_input = input("Bitte die Funktionsgleichung eines Kreises \
                                   eingeben (beispielsweise x**2 + y**2 = 9): ")
    linear_equation_input = input("Bitte die Funktionsgleichung einer Geraden \
                                   eingeben (beispielsweise 3*x - 2*y   = 4): ")

    # Eingelesenen Strings in Sympy-Ausdrücke umwandeln:
    circle_equation_elements = [sy.S(item) for item in \
                                circle_equation_input.replace("=", ",").split(",")]
    linear_equation_elements = [sy.S(item) for item in \
                                linear_equation_input.replace("=", ",").split(",")]

    # Gleichungssystem aus Sympy-Ausdrücken erstellen:
    equations = [
        sy.Eq(*circle_equation_elements),
        sy.Eq(*linear_equation_elements)
    ]

    # Gleichungssystem lösen
    solutions = sy.solve(equations)

    if len(solutions) == 2:
        print("Die Gerade ist eine Sekante.")
    elif len(solutions) == 1:
        print("Die Gerade ist eine Tangente.")
    else:
        print("Die Gerade ist eine Passante.")

Beim Erstellen des Gleichungssystems wurde bei der Übergabe der einzelnen
Sympy-Elemente der Stern-Operator ``*`` vorangestellt, um nicht die Liste,
sondern deren Inhalt an die ``Eq()``-Funktion zu übergeben.




