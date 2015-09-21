
.. _Kontrollstrukturen:

Kontrollstrukturen
==================

Die folgenden Kontrollstrukturen können zur Steuerung eines Programms verwendet
werden, wenn einzelne Code-Blöcke nur unter bestimmten Bedingungen oder auch
mehrfach ausgeführt werden sollen. In Python werden dabei keine Klammern zur
Markierung von Code-Blöcken verwendet; stattdessen werden Einrückungen zur
Gruppierung und Kenntlichmachung einzelner Code-Blöcke genutzt. Üblicherweise
wird für jede Einrückungstiefe ein Tabulator-Zeichen (entspricht vier
Leerzeichen) verwendet.

.. index:: if
.. _Fallunterscheidungen:

``if``, ``elif`` und ``else`` -- Fallunterscheidungen
-----------------------------------------------------

Mit Hilfe von ``if``-Abfragen ist es möglich, Code-Teile nur unter bestimmten
Bedingungen ablaufen zu lassen. Ist die ``if``-Bedingung wahr, so wird der
anschließende, mit einer Einrückung hervorgehobene Code ausgeführt.

.. code-block:: python

    if bedingung:

        ... Anweisungen ...

Optional können nach einem ``if``-Block mittels ``elif`` eine oder mehrere
zusätzliche Bedingungen formuliert werden, die jedoch nur dann untersucht
werden, wenn die erste ``if``-Bedingung falsch ist. Schließlich kann auch eine
``else``-Bedingung angegeben werden, die genau dann ausgeführt wird, wenn die
vorherige Bedingung (beziehungsweise alle vorherigen Bedingungen bei Verwendung
eines ``elif``-Blocks) nicht zutreffen.

Insgesamt kann eine Fallunterscheidung beispielsweise folgenden Aufbau haben:

.. code-block:: python

    if bedingung_1:
        ...

    elif bedingung_2:
        ...

    else:
        ...

Bei der Untersuchung der einzelnen Bedingungen werden die Werte von Variablen
häufig mittels :ref:`Vergleichsoperatoren <Operatoren>` überprüft. Mehrere
Teilbedingungen können zudem mittels logischer Operatoren zu einer
Gesamtbedingung verknüpft werden:

* Werden zwei Bedingungen mit ``and`` verknüpft, so ist das Ergebnis genau dann
  wahr, wenn beide Bedingungen erfüllt sind.
* Werden zwei Bedingungen mit ``or`` verknüpft, so ist das Ergebnis dann wahr,
  wenn mindestens eine der beiden Bedingungen (oder beide zugleich) erfüllt
  sind.
* Der Operator ``not`` kehrt den Wahrheitswert einer Bedingung um, eine wahre
  Bedingung liefert also ``False`` als Ergebnis, eine falsche Bedingung
  ``True``.


 .. .. list-table::
 ..     :name: tab-vergleichsoperatoren
 ..     :widths: 50 50

 ..     * - Operator
 ..       - Bedeutung
 ..     * - ``==``
 ..       - gleich
 ..     * - ``!=``
 ..       - ungleich
 ..     * - ``>``
 ..       - größer als
 ..     * - ``>=``
 ..       - größer gleich oder gleich
 ..     * - ``<``
 ..       - kleiner als
 ..     * - ``<``
 ..       - kleiner gleich oder gleich



..  Python erlaubt auch "abgekürzte" Bereichsabfragen für numerische Variablen.
..  Beispielsweise kann anstelle ``if value_1 <= value_2 and value_2 <= value_3``
..  auch einfacher ``if value_1 <= value_2 <= value_3`` geschrieben werden.

Da die logischen Operatoren eine geringer Priorität haben als die
Vergleichsoperatoren, können mehrere Vergleiche auch ohne Klammern mittels
``and`` beziehungsweise ``or`` verbunden werden.

.. code-block:: python

    # Beispiel:

    var_1 = (578 + 94) / 12
    var_2 = (1728) / 144

    if var_1 > var_2:
        print("var_1 is larger als var_2.")
    elif var_1 < var_2:
        print("var_1 is smaller als var_2.")
    else:
        print("var_1 is equal var_2.")

    # Ergebnis: var_1 is equal var_2.

Beinhaltet eine Variable :math:`var` einen Listentyp, beispielsweise ein
:ref:`Tupel <Tupel>`, einen :ref:`String <String>` , ein :ref:`Dict <dict>`
oder ein Set, so ergibt ``if var`` den Wert ``False``, falls die Länge der Liste
gleich Null ist, und ``True``, falls die jeweilige Liste mindestens ein Element
beinhaltet.


..  .. code-block:: python
..  if 50 <= var_1 <= 100:
..  print("var_1 liegt im Intervall [50 ; 100].")


.. _Schleifen:

``while`` und ``for`` -- Schleifen
----------------------------------

Mittels Schleifen kann ein Code-Abschnitt wiederholt ausgeführt werden. Python
bietet hierfür zweierlei Möglichkeiten: Mittels einer ``while``-Schleife wird
Code so lange ausgeführt, solange eine angegebene Bedingung wahr ist; mit einer
``for``-Schleife lassen sich auch komplexere Schleifentypen erzeugen.

.. index:: while
.. _while:

.. rubric:: ``while``-Schleifen

Eine ``while``-Schleife hat allgemein folgende Syntax:

.. code-block:: python

    while bedingung:

        ... Anweisungen ...


Ist die Bedingung wahr, so werden die im unmittelbar folgenden Block stehenden
Anweisungen ausgeführt. Vor jedem weiteren Durchlauf wird wieder geprüft, ob die
angegebene Bedingung erfüllt ist; sobald dies nicht der Fall ist, wird die
Schleife abgebrochen.

Unmittelbar an den ``while``-Block kann optional auch noch ein ``else``-Block
angefügt werden, der genau einmal ausgeführt wird, sobald die
``while``-Bedingung das erste mal den Wahrheitswert ``False`` annimmt. Damit
kann beispielsweise eine Programmstruktur folgender Art geschaffen werden:

.. code-block:: python

    while eingabe != passwort:

        ... weitere Texteingabe ...

    else:

        ... richtiges Passwort ...



.. rubric:: ``break`` und ``continue``

Der Ablauf einer ``while`` kann durch folgende beide Schlüsselwörter im Inneren
des Anweisungsblocks beeinflusst werden:

* Mittels ``break`` wird die Schleife unmittelbar an der jeweiligen Stelle
  beendet.

* Mittels ``continue`` kann der Rest des aktuellen Schleifendurchlaufs
  übersprungen werden; die Schleife wird anschließend mit dem nächsten
  Schleifendurchlauf fortgesetzt.

Mittels der ``break``-Anweisung können beispielsweise Endlos-Schleifen
programmiert werden, die nur unter einer bestimmten Bedingung beendet werden:

.. code-block:: python

    while True:

        ... Anweisungen ...

        if bedingung:
            break

Die Schlüsselwörter ``break`` und ``continue`` können ebenfalls in
``for``-Schleifen eingesetzt werden.


.. index:: for
.. _for:

.. rubric:: ``for``-Schleifen

Eine ``for``-Schleife hat allgemein folgende Syntax:

.. code-block:: python

    for var in iterierbares-objekt:

        ... Anweisungen ...

Ein iterierbares Objekt kann beispielsweise eine Liste, ein Tupel, oder auch ein
String sein. Im einfachsten Fall kann auch mittels der Funktion :ref:`range()
<range()>` ein iterierbares Objekt mit bestimmter Länge erzeugt werden:

.. code-block:: python

    summe = 0
    for i in range(1,10):
        summe += i

    print(summe)
    # Ergebnis: 45

Im diesem Beispiel durchläuft die Zählvariable ``i`` alle Werte im angegebenen
Zahlenbereich, wobei bei Verwendung von ``range()`` die untere Schranke zum
Zahlenbereich dazugehört, die obere jedoch nicht; es werden im obigen Beispiel
also alle Zahlen von ``1`` bis ``9`` aufsummiert.

.. Auch ``for``-Schleifen können einen ``else``-Zweig haben, der einmalig
.. aufgerufen wird, wenn die for-Bedingung nicht (mehr) zutrifft.

.. NOW!!

.. index:: pass
.. _pass:

``pass`` -- Die Platzhalter-Anweisung
-------------------------------------

Beim Entwickeln eines Programms kann es passieren, dass eine Kontrollstruktur
Funktion oder Fehlerroutine zunächst nur teilweise implementiert wird. Eine
Anweisung ohne Inhalt würde allerdings einen Syntaxfehler zur Folge haben. Um
dies zu vermeiden, kann die ``pass``-Anweisung eingefügt werden, die keine
weitere Bedeutung für das Programm hat. Beispiel:

.. code-block:: python

    var_1 = None

    if var_1 is None:
        pass
    else:
        print( "The value of var_1 is %s." % var_1 )

Die ``pass``-Anweisung stellt somit eine Erleichterung beim Entwickeln von
Programmen dar, da man sich mit ihrer Hilfe zunächst an wichtigeren
Programmteilen arbeiten kann. In fertigen Programmen werden ``pass``-Anweisungen
nur selten verwendet.


