.. index:: Funktion
.. _Funktionen:

Funktionen
==========

Oftmals werden bestimmte Code-Stücke an verschiedenen Stellen eines Programms
eingesetzt. Derartige Teile, die gewissermaßen kleine "Unterprogramme"
darstellen, werden als Funktionen definiert. Funktionen liefern am Ende stets
genau *ein* Ergebnis zurück; dieses kann jedoch von den übergebenen
Funktionsargumenten und/oder von äußeren Bedingungen abhängig sein. [#]_


.. index:: def()

.. _Definition eigener Funktionen:

Definition eigener Funktionen
-----------------------------

Eine Funktion wird in Python nach folgendem Schema definiert:

.. code-block:: python

    def function_name(argument_1, argument_2, ...):
        """
        Docstring (short description of the function's purpose)
        """

        function_code
        ...

        return result

Zum Benennen von Funktionen werden in Python üblicherweise nur kleine Buchstaben
verwendet. Häufig besteht ein Funktionsname aus einem Verb, das die
Wirkungsweise der Funktion beschreibt; liegt jedoch der Zweck einer Funktion nur
darin, einen bestimmten Wert auszugeben, so kann der Funktionsname auch aus
einem Substantiv bestehen, das den jeweiligen Wert beschreibt -- beispielsweise
wird die Wurzelfunktion meist mit ``sqrt()`` ("square root") anstelle von
``calculate_sqrt()`` bezeichnet. Besteht ein Funktionsname aus mehreren Wörtern,
so werden diese zur besseren Lesbarkeit mittels Unterstrichen getrennt.

Nach ihrer Definition kann die Funktion dann folgendermaßen aufgerufen werden:

.. code-block:: python

    function_name(argument_1, argument_2, ...)

Eine Funktion kann, abhängig von ihrer Definition, beim Aufruf kein, ein oder
auch mehrere Argumente in der jeweiligen Reihenfolge verlangen. Bei jedem Aufruf
wird dann der Funktions-Code ausgeführt und ein entsprechender Ergebniswert
zurück gegeben; ist im Funktionsblock keine ``return``-Anweisung enthalten, wird
von der Funktion automatisch der Wert ``None`` zurückgegeben. [#]_

Beim Aufruf der Funktion werden die einzelnen Argumente üblicherweise gemäß
ihrer Position direkt übergeben, beispielsweise ``argument_1 = 5 ;
function_name(argument_1)``. Es ist jedoch auch für eine gegebenenfalls bessere
Lesbarkeit des Quellcodes möglich, bei der Übergabe von Argumenten deren
Bezeichnung mit anzugeben, beispielsweise ``function_name(argument_1=5)``.

Da jede Funktion ein kleines Unterprogramm darstellt, sollte sie durch einen
Docstring dokumentiert werden. Es gibt Werkzeuge, die Docstrings verwenden, um
automatisch gedruckte Dokumentation zu erzeugen (beispielsweise :ref:`Sphinx
<gwl:Sphinx>`) oder um Benutzer interaktive Hilfe anzubieten
(beispielsweise Ipython). Werden bei einer Funktion Argumente verlangt, so
sollten diese ebenfalls im Docstring kurz beschrieben werden (Typ, Bedeutung).

.. _Optionale Argumente:

Optionale Argumente
-------------------

In Python ist es möglich, bei der Definition von Funktionen optionale Argumente
mit einem Standard-Wert anzugeben. Wird ein solches optionales Argument beim
Aufruf  der Funktion nicht explizit angegeben, so wird stattdessen der
Standard-Wert genutzt.

Die Definition einer solchen Funktion lautet etwa:

.. code-block:: python

    def my_function(argument_1, argument_2="Test")

        return (argument_1, argument_2)

Die Funktion kann anschließend wahlweise mit einem oder mit zwei Argumenten
aufgerufen werden:

.. code-block:: python

    my_function(5)
    # Ergebnis: (5, 'Test')

    my_function(5, 7)
    # Ergebnis: (5, 7)

Hat eine Funktion sowohl "normale" als auch optionale Argumente, so müssen die
optionalen Argumente am Ende der Funktion angegeben werden.

Ebenso ist es möglich, einer Funktion eine optionale Liste oder ein optionales
Dict für zusätzliche Argumente anzugeben. Üblicherweise lautet die Syntax
dafür:

.. code-block:: python

    def any_function(argument_1, argument_2="default value", *args, **kwargs)

        pass

Beim Aufruf der Funktion muss ``argument_1`` angegeben werden, die Angabe von
``argument_2`` ist optional; zusätzlich können weitere unbenannte oder benannte
Argumente angegeben werden, beispielsweise ``any_function(5,2,7,foo=9)``. Im
obigen Beispiel können alle unbenannten Argumente innerhalb der Funktion über
die Variable ``args``, alle benannten über die Variable ``kwargs`` aufgerufen
werden. Werden beim Funktionsaufruf keine weiteren Argumente übergeben, so ist
``args`` innerhalb der Funktion ein leeres Tupel und ``kwargs`` ein leeres Dict.

.. code-block:: python

    def sum_it_up(num_1, num_2, *nums):

        list_sum = functools.reduce(lambda x,y: x+y, nums)

        return num_1 + num_2 + len(nums)

Hat man im Quellcode vorab eine Liste an Objekten definiert, die man dann als
Argumente an eine Funktion übergeben möchte, so muss diese bei der Übergabe
entpackt werden. Dies ist mittels des ``*``-Operators möglich:

.. code-block:: python

    my_list = [1,3,5,7]

    sum_it_up(*my_list)
    # Ergebnis: 6

Im obigen Beispiel wurde die Liste ``my_list`` bei der Übergabe an die Funktion
entpackt; der Aufruf von ``sum_it_up(*my_list)`` ist in diesem Fall also
identisch mit ``sum_it_up(1,3,5,7)``. Die ersten beiden Zahlen werden dabei als
Argumente für ``num_1`` und ``num_2`` angesehen, die verbleibenden beiden
werden innerhalb der Funktion in die Variable ``nums`` gespeichert. [#]_

Nach dem gleichen Prinzip kann ein Dict mit Schlüsselwort-Wert-Paaren mittels
``**`` entpackt an eine Funktion übergeben werden; dabei müssen alle im Dict
enthaltenen Schlüsselwörter als mögliche Funktionsargumente erlaubt sein.


.. _Veränderliche und unveränderliche Argumente:

Veränderliche und unveränderliche Argumente
-------------------------------------------

In Python werden Argumente an Funktionen via Zuweisung (Position oder Benennung)
übergeben. Wird beispielsweise eine Variable ``x = any_object`` als Argument an
eine Funktion übergeben, so wird ``x``, also eine Referenz auf ``any_object``,
als Wert übergeben. Welchen Einfluss die Funktion auf das Argument hat, hängt
dabei vom Objekt-Typ ab:

* Ist ``any_object`` ein veränderliches Objekt, beispielsweise eine Liste, ein
  Dict oder ein Set, so kann dieses durch die Funktion direkt verändert werden:

  .. code-block:: python

      my_list = [1,2,3]

      def foo(any_list):
          any_list.append(4)

      foo()

      print(my_list)
      # Ergebnis: [1,2,3,4]

  Wird allerdings der übergebenen Referenz ``x`` in der Funktion ein neues
  Objekt zugewiesen, so entspricht dies einer Definition einer neuen Variablen
  innerhalb der Funktion als Namensraum. [#]_ Die ursprüngliche Referenz ``x``
  bleibt in diesem Fall unverändert und zeigt nach wie vor auf das ursprüngliche
  Objekt:

  .. code-block:: python

      my_list = [1,2,3]

      def foo(any_list):
          any_list = [1,2,3,4]

      foo()

      print(my_list)
      # Ergebnis: [1,2,3]

* Ist ``any_object`` ein unveränderliches Objekt, beispielsweise ein String oder
  ein Tupel, so wird bei der Übergabe an die Funktion eine Kopie des Objekts
  erzeugt; das ursprüngliche Objekt kann somit durch die Funktion nicht
  verändert werden:

  .. code-block:: python

      my_string = 'Hello World!'

      def foo(any_string):
        any_string.replace('World', 'Python')

      foo()

      print(my_string)
      # Ergebnis: 'Hello World!'

  Möchte man den obigen Beispielcode so umschreiben, dass nach Aufruf der
  Funktion die Variable ``my_string`` den Wert ``'Hello Python!'`` bekommt, so
  muss man folgendermaßen vorgehen:

  .. code-block:: python

      my_string = 'Hello World!'

      def foo(any_string):
        x = any_string.replace('World', 'Python')
        return x

      my_string = foo(my_string)

      print(my_string)
      # Ergebnis: 'Hello Python!'

  Da Strings nicht verändert werden können, kann eine Veränderung der
  zugehörigen Variablen also nur über eine neue Zuweisung erfolgen.

Die Übergabe eines veränderlichen Datentyps, beispielsweise einer Liste, als
Argument an eine Funktion ist zwar performance-technisch günstig, da nur eine
neue Referenz auf die Liste erzeugt werden muss; es können aber unerwartete
Fehler auftreten, wenn durch eine Funktion das übergebene Original der Liste
unmittelbar verändert wird. Durch Verwendung von Tupeln anstelle von Listen kann
dies auf Kosten von CPU und Memory ausgeschlossen werden.


.. _Globaler und lokaler Namensraum:

.. rubric:: Globaler und lokaler Namensraum

Jeder Funktionsblock hat einen eigenen Namensraum, was bedeutet, dass Variablen,
die innerhalb des Funktionsblocks definiert werden, nur im Programm existieren,
bis der Funktionsblock abgeschlossen ist. Derartige Variablen, die nur innerhalb
der Funktion "sichtbar" sind,  werden "lokale" Variablen genannt.

Einer lokalen Variablen kann dabei der gleiche Name zugewiesen werden wie einer
Variablen, die außerhalb des Funktionsblocks definiert wurden; sie "überdeckt"
in diesem Fall die nicht-lokale Variable: Der Interpreter sucht primär im
lokalen Namensraum nach dem Variablennamen und erst sekundär im nicht-lokalen
Namensraum, wenn keine lokale Variable mit dem angegebenen Namen existiert.  und
nur.

Wird einer lokalen Variablen ein Wert zugewiesen, so ändert sich also der
Wert einer nichtlokalen Variablen nicht:

.. code-block:: python
    :emphasize-lines: 6

    # Nicht-lokale Variable definieren:
    x = 0

    # Funktion mit lokaler Variablen definieren:
    def myfunc():
        x = 1
        print(x)

    # Funktion aufrufen:

    myfunc()
    # Ergebnis: 1

    # Wert von x prüfen:

    x
    # Ergebnis: 0


Soll der Wert einer nicht-lokalen Variablen durch die Funktion verändert werden,
so kann diese bei einem veränderlichen Datentyp als Argument an die Funktion
übergeben werden. Variablen mit nicht veränderlichem Datentyp können, wie im
letzten Abschnitt beschrieben, eine Veränderung erreicht werden, nur durch eine
Zuweisung des Rückgabewerts der Funktion geändert werden.

Eine weitere prinzipielle Möglichkeit, die jedoch möglichst vermieden werden
sollte, ist es, mittels des Schlüsselworts ``global`` einen Variablennamen
primär im nicht-lokalen Namensraum zu suchen:

.. code-block:: python
    :emphasize-lines: 6

    # Nicht-lokale Variable definieren:
    x = 0

    # Funktion mit globaler Variablen definieren:
    def myfunc():
        global x = 1
        print(x)

    # Funktion aufrufen:

    myfunc()
    # Ergebnis: 1

    # Wert von x prüfen:

    x
    # Ergebnis: 1

Das Schlüsselwort ``global`` hat nur Auswirkungen innerhalb der Funktion, eine
Variable kann also nicht von außerhalb der Funktion als "global" gekennzeichnet
und als solche der Funktion aufgezwungen werden. Dennoch kann die Verwendung von
``global`` zu unerwarteten Seiteneffekten führen, wenn eine Variable prinzipiell
von mehreren Stellen aus verändert werden kann, da in diesem Fall nicht immer
auf den ersten Blick einwandfrei feststellbar ist, von wo aus die Variable
verändert wurde.

.. TODO: nichtlokaler Namensraum / nonlocal


.. index:: lambda
.. _Lambda-Ausdrücke:

Lambda-Ausdrücke
----------------

Bei so genannten Lambda-Ausdrücken handelt es sich um Mini-Funktionen, die sehr
kompakt implementiert werden können. Das Schlüsselwort zur Definition eines
Lambda-Ausdrucks ist ``lambda``, gefolgt von möglichen Argumenten, die der
Funktion beim Aufruf übergeben werden sollen, und einem Doppelpunkt.
Hinter diesem Doppelpunkt wird in der gleichen Zeile die Wirkungsweise des
Lambda-Ausdrucks definiert, beispielsweise:

.. code-block:: python

    add = lambda x1, x2: x1 + x2

    add(5,3)
    # Ergebnis: 8

Bei der Definition eines Lambda-Ausdrucks entfällt also das Schlüsselwort
``def``, und die Argumente werden unmittelbar hinter dem Schlüsselwort
``lambda`` ohne runde Klammern angegeben.

Ein Nachteil von Lambda-Ausdrücken ist, dass in ihnen keine Schleifen,
Kontrollstrukturen oder komplexeren Anweisungsblöcke vorkommen dürfen. [#]_ Ein
wichtiger Vorteil ist hingegen, dass Lambda-Ausdrücke keinen expliziten Namen
haben müssen. Beispielsweise kann der gesamte Lambda-Ausdruck, wenn man ihn in
runde Klammern setzt, unmittelbar wie eine Funktion aufgerufen werden:

.. code-block:: python

    result = (lambda x1, x2: x_1 + x_2)(5,3)

    print(result)
    # Ergebnis: 8

Lambda-Ausdrücke werden auch häufig in Kombination mit den Builtin-Funktion
``filter()`` und ``map()`` eingesetzt, um jeweils auf alle Elemente einer Liste
angewendet zu werden:

.. code-block:: python

    # Beispiel 1:

    my_list = [1,2,3,4,5,6,7,8,9]

    even_numbers = filter(lambda x: x % 2 == 0, my_list)

    list(even_numbers)
    # Ergebnis: [2,4,6,8]


    # Beispiel 2:

    my_list = [1,2,3,4]

    even_numbers = map(lambda x: x * 2, [1,2,3,4])

    list(even_numbers)
    # Ergebnis: [2,4,6,8]

Ebenso kann ein Lambda-Ausdruck als Kriterium für die ``sort()``-Funktion
genutzt werden, um beispielsweise eine Liste von Zweier-Tupeln nach den ersten
Elementen der Tupel zu sortieren:

.. code-block:: python

    my_list = [(3, 1), (1, 2), (11, -3), (5, 10)]

    my_list.sort(key=lambda x: x[0])

    print(my_list)
    # Ergebnis: [(1, 2), (3, 1), (5, 10), (11, -3)]
..
    Mit Hilfe von Lambda-Ausdrücken können auch so genannte
    "Funktions-Generatoren" nach Bedarf einfach implementiert werden:

    .. code-block:: python

        # Definition eines Funktions-Generators:
        def increase_by(n):
            return lambda x: x + n

        # Erzeugen einer Funktion, die den übergebenen Wert um 4 erhöht:
        f4 = increase_by(4)

        # Aufrufen der neuen Funktion:

        f4(3)
        # Ergebnis: 7

Auch bei der Entwicklung von graphischen Oberflächen sind Lambda-Ausdrücke
nützlich, um einzelnen Maus-Events oder Tastenkombinationen bestimmte Funktionen
zuzuweisen.

.. _Builtin-Funktionen:

Builtin-Funktionen
------------------

Neben der bereits erwähnten ``print()``-Funktion, die zur Anzeige von Texten und
Variablen auf dem Bildschirm dient, gibt es in Python weitere grundsätzlich
verfügbare Funktionen, so genannte "Builtin"-Funktionen; Diese Funktionen sind
ohne das Importieren weiterer :ref:`Module <Module>` unmittelbar verfügbar. Eine
Übersicht über diese Funktionen findet sich im :ref:`Anhang: Standard-Funktionen
<Standardfunktionen>`.


.. eval() und exec()


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Soll eine Funktion mehrere Ergebnisse liefern, so müssen diese als
    :ref:`Liste <Liste>` oder :ref:`Tupel <Tupel>` zurückgegeben werden.

.. [#] In einer Funktionsdefinition können auch, wenn ``if``-Bedingungen in ihr
    vorliegen, an mehreren Stellen ``return``-Anweisungen auftreten. Sobald eine
    ``return``-Anweisung erreicht wird, wird die Funktion unmittelbar beendet
    und der jeweilige Ergebniswert zurück gegeben. Steht nur ``return`` (ohne
    expliziten Ergebniswert), so wird ebenfalls der Wert ``None`` zurück
    gegeben.

    Soll eine Funktion mehrere Werte als Ergebnis liefern, so müssen diese als
    Liste oder Tupel an das Programm zurückgegeben werden.

.. [#] Dass die obige Funktion die Länge der zusätzlichen Zahlenliste zum
    Ergebnis dazu addiert, soll an dieser Stelle nur die Funktionalität der
    optionalen Argumente zeigen. Um alle Elemente dieser Liste zu summieren,
    muss zusätzlich das Modul ``functools`` geladen werden; in der
    Beispielaufgabe :ref:`Quader <Quader>` wird dies näher behandelt.

.. [#] Variablen sind nur innerhalb ihres Namensraums gültig. Ausnahmen sind
    globale Variablen, die beispielsweise zu Beginn eines Moduls definiert sind.
    Eine solche kann dann innerhalb einer Funktion mittels ``global var_name``
    als global gekennzeichnet werden, wobei ``var_name`` der Name der Variablen
    ist.

.. [#] Eine :ref:`Bedingte Wertzuweisung <Bedingte Wertzuweisung>` in der Form
    ``lambda x: a if condition else b`` ist allerdings erlaubt.

