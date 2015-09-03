.. _Datentypen:

Datentypen
==========

Im folgenden Abschnitt werden die zum Python-Standard gehörenden Datentypen kurz
vorgestellt. In Skripten oder im interaktiven Modus kann der Datentyp eines
Objekts oder einer Variable jederzeit mittels ``type(variable)`` angezeigt
werden.

..  Die folgenden Datentypen gehören zum Python-Standard.

.. index:: None
.. _None:

``None`` -- Der Nichts-Typ
--------------------------

Durch den Datentyp ``None`` wird in Python beispielsweise symbolisiert, dass
eine Variable keinen Wert beinhaltet. Dies ist beispielsweise sinnvoll, wenn man
eine Variable definieren, ihr aber erst späteren einen konkreten Wert zuweisen
will; ein anderer Anwendungsfall wäre die Rückgabe eines Ergebniswerts bei einer
erfolglosen Suche.

Um einer Variablen den Wert ``None`` zuzuweisen, gibt man folgendes ein:

.. code-block:: python

    var_1 = None

    # Test:

    print(var_1)
    # Ergebnis: None

``None`` ist ein :ref:`Singleton <Singleton>`, es gibt also stets nur eine
Instanz dieses Typs; ``None`` kann somit stets wie eine Konstante verwendet
werden. Ebenso kann mittels des ``None``-Typs abgefragt werden, ob eine Variable
einen Wert beinhaltet oder nicht. Eine solche Abfrage kann prinzipiell so
aussehen:

.. code-block:: python

    if var_1 is None:
        print("var_1 has no value.")
    else:
        print("the value of var_1 is " var_1)

Mittels des Schlüsselworts ``is`` wird im obigen Beispiel überprüft, ob
``var_1`` eine Instanz des Typs ``None`` ist. Durch ``if var_1 is not None``
kann sichergestellt werden, dass ein Code-Teil nur dann ausgeführt wird, wenn
der Variablen ``var_1`` bereits ein Wert zugewiesen wurde.


.. _Numerische Datentypen:

Numerische Datentypen
---------------------

.. index::
    single: True
    single: False

.. _True und False:

``True`` und ``False`` -- Boolesche Werte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Eine boolesche Variable kann nur ``True`` (wahr) oder ``False`` (falsch) als
Werte annehmen. Von Python wird ``True`` als ``1`` beziehungsweise ``False`` als
``0`` interpretiert, so dass sich theoretisch auch mit Variablen des Datentyps
``bool`` rechnen lässt (beispielsweise ergibt ``True + True`` den Wert ``2``).

Der boolesche Wahrheitswert eines beliebigen Ausdrucks kann mittels der
Standard-Funktion :ref:`bool() <bool()>` ermittelt werden, beispielsweise
liefert ``bool(1)`` den Wert ``True``.

.. index:: int
.. _Ganze Zahlen:

``int`` -- Ganze Zahlen
^^^^^^^^^^^^^^^^^^^^^^^

Ganzzahlige Werte werden in Python durch den Datentyp ``int`` repräsentiert.

Um die Anzahl an Ziffern einer ``int``-Zahl zu bestimmen, kann diese mittels
``str()`` in eine Zeichenkette umgewandelt werden; anschließend kann die
Länge dieser Zeichenkette mittels ``len()`` bestimmt werden:

.. code-block:: python

    num_1 = 58316

    # Zahl in Zeichenkette umwandeln:

    str(num_1)
    # Ergebnis: '58316'

    # Anzahl der Ziffern der Zahl ausgeben:

    len(str(num_1))
    # Ergebnis: 5

Wird im umgekehrten Fall eine Zahl beispielsweise mittels der Funktion
``input()`` eingelesen, so liegt sie als Zeichenkette vor; mittels ``int()`` ist
dann eine Konvertierung in eine gewöhnliche Zahl möglich.

Bisweilen werden Zahlen auch in einer binären, oktalen oder hexadezimalen
Darstellung verwendet. Um eine dezimale ``int``-Zahl mit einer anderen
Zahlenbasis (``2``, ``8`` oder ``16``) darzustellen, gibt es folgende Funktion:

.. code-block:: python

    num_1 = 78829

    bin(num_1)
    # Ergebnis: '0b10011001111101101'

    oct(num_1)
    # Ergebnis: '0o231755'

    hex(num_1)
    # Ergebnis: '0x133ed'

Das Ergebnis sind jeweils Zeichenketten, die mit ``0b`` (binär), ``0o`` (oktal)
oder ``0x`` (hexadezimal) beginnen. Um eine derartige Zeichenkette wieder in
eine gewöhnliche ``int``-Zahl zu konvertieren, kann man die ``int()``-Funktion
nutzen, wobei die ursprüngliche Zahlenbasis als zweites Argument angegeben
werden muss:

.. code-block:: python

    # Binärzahl in Dezimalzahl umwandeln:

    int('0b10011001111101101', base=2)
    # Ergebnis: 78829

.. index:: min(), max()

Um die größte beziehungsweise kleinste mindestens zweier Zahlen (``int`` oder
``float``) zu bestimmen, können die Funktionen ``min()`` oder ``max()`` genutzt
werden:

.. code-block:: python

    min(-5, 17842, 30911, -428)
    # Ergebnis: -428

    max(-5, 17842, 30911, -428)
    # Ergebnis: 30911


.. Fußnote: Auch Liste als Argument möglich

Der Absolutwert einer ``int`` oder ``float``-Zahl kann mittels der
Standardfunktion :ref:`abs(number) <abs()>` ausgegeben werden.


.. index:: float
.. _Gleitkommazahlen:

``float`` -- Gleitkommazahlen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zahlen mit Nachkommastellen werden in Python durch den Datentyp ``float``
repräsentiert. Die Nachkommastellen werden dabei -- wie im englischen Sprachraum
üblich -- nicht durch ein Komma, sondern durch einen Punkt ``.`` von dem
ganzzahligen Anteil getrennt. Zudem ist es möglich, sehr große oder sehr kleine
``float``-Zahlen mittels ``e`` oder ``E`` in Exponential-Schreibweise anzugeben.
Die Zahl hinter dem ``e`` gibt dabei an, um wie viele Stellen der Dezimalpunkt
innerhalb der Zahl verschoben wird.

.. code-block:: python

    4.3e5 == 430000
    # Ergebnis: True

    7.92e-5 == 0.0000792
    # Ergebnis: True

Um eine ``float``-Zahl auf :math:`n` Nachkomma-Stellen zu runden, kann die
Funktion ``round(float_num, n)`` genutzt werden. Wird das Argument ``n``
weggelassen, wird auf die nächste ganze Zahl gerundet. Eine Gleitkommazahl
``float_1`` kann ebenso mittels ``int(float_1)`` in eine ganze Zahl umgewandelt
werden; dabei werden jedoch eventuell vorhandene Nachkommastellen abgeschnitten,
es also stets die betragsmäßig nächst kleinere ganze Zahl als Ergebnis zurück
gegeben.

.. TODO: Fußnote
.. floor() und ceil() des ``math``-Moduls (siehe :ref:`Standardbibliothek <math-Modul>`)


.. index:: complex()
.. _Komplexe Zahlen:

``complex`` -- Komplexe Zahlen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Komplexe Zahlen <gwm:Komplexe Zahlen>` bestehen aus einem Realteil und
einem Imaginärteil. Der Imaginärteil besteht aus einer reellen Zahl, die mit der
imaginären Einheit ``j`` multipliziert wird. [#]_

Um eine komplexe Zahl zu definieren, gibt man in Python etwa folgendes ein:

.. code-block:: python

    z_1 = 4 + 3j
    z_2 = 5.8 + 1.5j

Für das Arbeiten mit komplexen Zahlen kann das ``cmath``-Modul aus der
Standardbibliothek genutzt werden.

.. index:: String, Zeichenkette, str()
.. _Zeichenketten:
.. _String:

``str`` -- Zeichenketten
------------------------

Zeichenketten ("Strings") sind eine Folge von Zeichen, die wahlweise in
einfachen oder doppelten Anführungszeichen geschrieben werden. [#]_ Nahezu jedes
Python-Objekt kann mittels ``str(object)`` in eine Zeichenkette umgewandelt
werden, um beispielsweise eine druckbare Darstellung mittels ``print()`` zu
ermöglichen.

.. code-block:: python

    string_1 = "Hallo"
    string_2 = "Welt!"
    string_3 = str(539)     # Ergebnis: '539'

Zeichenketten können mittels ``+`` miteinander kombiniert werden. Möchte man
eine Zeichenkette beliebiger Länge in mehrfacher Wiederholung, so kann diese
mittels ``*`` und einer ganzzahligen Zahl vervielfacht werden. Da Zeichenketten
in Python (wie :ref:`Tupel <Listen und Tupel>`) unveränderbar sind, wird bei den
obigen Beispielen stets eine neue Zeichenkette erzeugt. Die ursprüngliche
Zeichenkette bleibt jeweils unverändert:

.. code-block:: python

    string_1 + " " + string_2
    # Ergebnis: "Hallo Welt!"

    string_1 * 3
    # Ergebnis: "HalloHalloHallo"

Die Länge einer Zeichenkette kann mittels ``len()`` bestimmt
werden:

.. code-block:: python

    len("Hallo Welt")
    # Ergebnis: 10


Zur besseren Lesbarkeit sollten Code-Zeilen zudem nicht mehr als 80 Zeichen lang
sein. Längere Strings können allerdings in der nächsten Zeile fortgesetzt
werden, wenn die vorangehende Zeile mit einem einzelnen Backslash ``\`` als
Zeile-Fortsetzungs-Zeichen abgeschlossen wird:

.. code-block:: python

    long_string = "Das ist eine lange Zeichenkette, die für eine bessere \
                   Lesbarkeit über zwei Zeilen verteilt geschrieben wird."

Durch den Backslash werden also beide Zeilen zu einer logischen Einheit
verbunden; hinter dem Backslash darf allerdings kein Kommentarzeichen stehen.


.. index:: Docstring
.. _Docstring:

Mehrzeilige Zeichenketten können ebenso in dreifache Anführungszeichen gesetzt
werden. Solche "Docstrings", um längere Code-Abschnitte, Funktionen, Klassen
oder Module zu dokumentieren, denn sie bleiben vom Interpreter unbeachtet. Beim
Schreiben von Docstrings sollten die `offiziellen Empfehlungen
<https://www.python.org/dev/peps/pep-0257/>`_ beachtet werden.

Zeichenketten können allgemein folgende Sonderzeichen beinhalten:

.. list-table::
    :name: tab-sonderzeichen
    :widths: 10 50

    * - Zeichen
      - Bedeutung
    * - ``\t``
      - Tabulator
    * - ``\n``
      - Newline (Zeilenumbruch)
    * - ``\r``
      - Carriage Return
    * - ``\\``
      - Backslash
    * - ``\'``
      - Einfaches Anführungszeichen
    * - ``\"``
      - Doppeltes Anführungszeichen
    * - ``\xnn``
      - Sonderzeichen (:ref:`ASCII <ASCII-Codes>`), repräsentiert durch eine
        zweistellige Hexadezimalzahl, beispielsweise ``\xe4``
    * - ``\unnnn``
      - Sonderzeichen (16-bit-Unicode), repräsentiert durch eine vierstellige
        Hexadezimalzahl, beispielsweise ``\u7fe2``

Möchte man das Interpretieren der obigen Sonderzeichen unterbinden, kann dies
durch ein vorangestelltes ``r`` ("raw") geschehen; beispielsweise wird in
``r"a\tb"`` das ``\t`` nicht als Tabulator-Zeichen interpretiert.

..  ord('\n') Ergebnis: 10 Ascii-Code

.. _Indizierung von Zeichenketten:

Indizierung von Zeichenketten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Auf die einzelnen Zeichen einer Zeichenkette kann mittels des Index-Operators
``[ ]`` zugegriffen werden. Dabei wird das erste Zeichen, wie in der
Programmiersprache ``C`` üblich,  mit ``0`` indiziert. Auf das letzte Element
eines :math:`n` Zeichen langen Strings kann entsprechend mit dem Index ``n-1``,
oder in Kurzschreibweise mit dem Index ``-1`` zugegriffen werden. Ein größerer
Index als ``n-1`` löst einen Fehler (``IndexError``) aus.

.. code-block:: python

    example = "Hallo Welt"

    # Erstes und zweites Zeichen:

    example[0]
    # Ergebnis: 'H'

    example[1]
    # Ergebnis: 'a'

    # Vorletztes und letztes Zeichen:

    example[-2]
    # Ergebnis: 'l'

    example[-1]
    # Ergebnis: 't'

Der Index-Operator kann ebenso genutzt werden, um Bereiche ("Slices") einer
Zeichenkette auszugeben. Hierzu werden in den eckigen Klammern zwei Index-Zahlen
``n_1`` und ``n_2`` durch einen Doppelpunkt getrennt angegeben. Es muss dabei
allerdings beachtet werden, dass in Python bei Bereichsangaben die obere Grenze
*nicht* im Bereich eingeschlossen ist:

.. code-block:: python

    example[0:5]
    # Ergebnis: 'Hallo'

    example[6:-1]
    # Ergebnis: 'Wel'

    example[6:]
    # Ergebnis: 'Welt'

Lässt man von der Bereichsangabe die Zahl vor oder nach dem Doppelpunkt weg, so
wird die Zeichenkette von Beginn an beziehungsweise bis zum Ende ausgegeben.

Bei der Verwendung von Slices kann optional noch ein dritter Parameter angegeben
werden, der die "Schrittweite" festlegt, also angibt, jedes wie vielte Zeichen
ausgewählt werden soll:

.. code-block:: python

    example[::2]
    # Ergebnis: "Hlo"

Wird für die Schrittweite ein negativer Wert angegeben, so wird der String von
hinten nach vorne abgearbeitet.


.. _String-Funktionen:

String-Funktionen
^^^^^^^^^^^^^^^^^

Für Zeichenketten gibt es in Python einige Funktionen, die in der Form
``liste.funktionsname()`` angewendet werden können.

.. rubric:: Suchen und Ersetzen

Da Zeichenketten unveränderbar sind, kann der Index-Operator nicht auf der
linken Seite des Zuweisungsoperators ``=`` stehen; beispielsweise würde die
Eingabe von ``example[0:5] = "Salut"`` einen ``TypeError`` erzeugen. Um eine
solche Veränderung vorzunehmen, kann jedoch beispielsweise die speziell für
Zeichenketten definierte ``replace()``-Funktion genutzt werden, und der daraus
resultierende String wieder der ursprünglichen Variable zugewiesen werden:

.. code-block:: python

    # "Hallo" durch "Salut" ersetzen:
    example = example.replace("Hallo", "Salut")

Statt ``Hallo`` könnte im obigen Beispiel wiederum ``example[0:5]`` geschrieben
werden. Um zu prüfen, ob und an welcher Stelle ein Teilstring in einer
Zeichenkette enthalten ist, kann die String-Funktion ``find()`` genutzt werden:

.. code-block:: python

    example.find("Welt")
    # Ergebnis: 6

Der Teilstring ``"Welt"`` ist also ab der Index-Position ``6`` im
Beispiel-String enthalten. Wird der gesuchte String im Zielstring nicht
gefunden, liefert die ``find()``-Funktion den Wert ``-1`` als Ergebnis.

.. _Groß- und Kleinschreibung ändern:

.. rubric:: Groß- und Kleinschreibung ändern

Python achtet bei der Behandlung von Zeichenketten auf die Groß- und
Kleinschreibung. Sollen also beispielsweise zwei Wörter hinsichtlich nur ihres
Inhalts, nicht jedoch hinsichtlich der Groß- und Kleinschreibung verglichen
werden, so werden üblicherweise beide zunächst in Kleinbuchstaben umgewandelt.
Hierfür kann die Funktion ``lower()`` verwendet werden:

.. code-block:: python

    "Hallo".lower() == "hallo"
    # Ergebnis: True

Die Funktion ``upper()``, wandelt in umgekehrter Weise alle Buchstaben einer
Zeichenkette in Großbuchstaben um. Zwei ähnliche Funktionen sind ``capitalize()``,
bei einer Zeichenkette nur den ersten Buchstaben als Großbuchstaben und die
restlichen als Kleinbuchstaben ausgibt sowie ``title()``, die bei jedem Wort
einer Zeichenkette den ersten Buchstaben als Großbuchstaben und die übrigen als
Kleinbuchstaben ausgibt. Mit ``swapcase()`` können zudem alle Großbuchstaben
einer Zeichenkette in Kleinbuchstaben und umgekehrt umgewandelt werden.

.. rubric:: Leerzeichen entfernen

Mittels der Funktionen ``lstrip()`` oder ``rstrip()`` können Leerzeichen am
Anfang oder am Ende einer Zeichenkette entfernt werden; mittels ``strip()``
werden Leerzeichen sowohl am Anfang wie auch am Ende einer Zeichenkette
entfernt.

Die Funktion ``rstrip()`` wird häufig eingesetzt, um beim Einlesen einer
Textdatei alle Leerzeichen am Ende der einzelnen Zeilen zu entfernen.


.. The transformer group of method functions includes center(), expandtabs(),
.. ljust(), rjust(), and zfill(). These methods all make general changes to the
.. characters of a string to create a transformed result. Methods such as lower()
.. and upper() are used frequently to normalize case for comparisons:


Eine `vollständige Liste an String-Funktionen
<https://docs.python.org/3/library/stdtypes.html#str>`_ erhält man, indem man
die Funktion ``dir()`` auf einen beliebigen String anwendet, beispielsweise
``dir(string_1)``. Nähere Informationen können dann beispielsweise mittels
``help(string_1.replace)`` aufgerufen werden.

.. todo: split(), strip(), center(), startswidth(),
.. endswidth(), count() hier erwähnen?

.. anystring.count(substring) -> number of matches
.. anystring.find(substring)  -> position
.. anystring.find(substring, position+1) -> next position

.. rfind() -> letztes Vorkommen des Suchbegriffs im Text

.. _Formatierung von Zeichenketten:

.. rubric:: Formatierung von Zeichenketten

Bisweilen mag man beispielsweise mit ``print()`` den Wert einer Variablen als
Teil einer Zeichenkette ausgeben. Zu diesem Zweck können in die Zeichenkette
Platzhalter eingebaut werden, die dann durch die gewünschten Werte ersetzt
werden. Dies funktioniert der "klassischen" Methode nach (wie etwa in :ref:`C
<gwic:Grundkurs C>` so:

.. code-block:: python

    var = 5829

    "Der Wert von var ist %s." % var
    # Ergebnis: "Der Wert von var ist 5829."

Sollen an mehreren Stellen Ersetzungen vorgenommen werden, werden die
Platzhalter in der gleichen Reihenfolge durch die Elemente eines gleich langen
Variablen-Tupels ersetzt:

.. code-block:: python

    var_1 = 8913
    var_2 = 7824

    print("Der Wert von var_1 ist %s, \
           der Wert von var_2 ist %s" % (var_1, var_2) )

    # Ergebnis: "Der Wert von var_1 ist 8913, der Wert von var_2 ist 7824."

Nach der neueren, mehr pyton-artigen Variante können Ersetzungen in
Zeichenketten auch mittels der Funktion ``format()`` vorgenommen werden:

.. code-block:: python

    var   = 5829
    var_1 = 8913
    var_2 = 7824

    print( "Der Wert von var ist {}.\n".format(var) )
    # Ergebnis: "Der Wert von var ist 5829."

    print( "Der Wert von var_1 ist {}, \
            der Wert von var_2 ist {}.\n".format(var_1, var_2) )

In diesem Fall werden die geschweiften Klammern innerhalb der Zeichenkette als
Platzhalter angesehen und durch die als Argumente der Funktion ``format()``
angegebenen Variablen ersetzt. Als einzige Besonderheit müssen bei dieser
Methode "echte" geschweifte Klammern, die als Textsymbole in der Zeichenkette
vorkommen sollen, durch ``{{`` bzw. ``}}`` dargestellt werden.


.. index:: Liste, Tupel, list(), tuple()
.. _Listen und Tupel:
.. _list:
.. _tuple:
.. _Tupel:
.. _Liste:

``list`` und ``tuple`` -- Listen und Tupel
------------------------------------------

Listen und Tupel dienen der Sequenzierung von Objekten beliebigen Datentyps. Sie
können unterschiedliche Datentypen in beliebiger Reihenfolge beinhalten. Listen
werden in Python durch eckige Klammern, Tupel durch runde Klammern
gekennzeichnet; die einzelnen Elemente werden durch jeweils ein Komma-Zeichen
voneinander getrennt.

.. code-block:: python

    liste_1 = ['a', 'b', 'c', 1, 2, 3]  # oder:  list( 'a', 'b', 'c', 1, 2, 3 )
    tupel_1 = ('a', 'b', 'c', 1, 2, 3)  # oder: tuple( ['a', 'b', 'c', 1, 2, 3] )

Der einzige Unterschied zwischen Listen, die mit ``[`` und ``]`` gekennzeichnet
sind, und Tupeln, deren Elemente zwischen ``(`` und ``)`` stehen, liegt darin,
dass die Inhalte von Listen verändert werden können, während die Inhalte von
Tupeln unveränderbar sind. [#]_ Tupel können genutzt werden, um die Datensicherheit
bestimmter Variablen, die an verschiedenen Stellen eines Programms genutzt
werden, zu gewährleisten; im allgemeinen werden jedoch bevorzugt Listen
genutzt.

Mittels der Schlüsselwörter ``in`` beziehungsweise ``not in`` kann geprüft
werden, ob ein Objekt in einer Liste enthalten ist oder nicht:

.. code-block:: python

    'a' in liste_1
    # Ergebnis: True

.. _Indizierung von Listen und Tupeln:

Indizierung von Listen und Tupeln
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Auf die einzelnen Elemente einer Liste kann mit Hilf des mit Hilfe des
Index-Operators ``[ ]`` zugegriffen werden. Die Syntax stimmt mit der
:ref:`Indizierung von Zeichenketten <Indizierung von Zeichenketten>` überein, da
es sich bei diesen letztlich ebenfalls um Listen einzelner Buchstaben handelt:

.. code-block:: python

    # Erstes und zweites Element der Liste:

    liste_1[0]
    # Ergebnis: 'a'

    liste_1[1]
    # Ergebnis: 'b'

    # Vorletztes und letztes Element der Liste:

    liste_1[-2]
    # Ergebnis: '2'

    liste_1[-1]
    # Ergebnis: '3'

Bereiche ("Slices") einer Liste können mit Hilfe des Index-Operators ausgewählt
werden, indem man zwei mit einem Doppelpunkt getrennte Index-Zahlen ``n1`` und
``n2`` angibt; dabei muss beachtet werden, dass in Python bei Bereichsangaben
die obere Grenze *nicht* im Bereich eingeschlossen ist:

.. code-block:: python

    liste_1[3:5]
    # Ergebnis: [1, 2]

Wird bei der Verwendung von Slices die obere und/oder die untere Bereichsangabe
weggelassen, so werden die Elemente vom Anfang an beziehungsweise bis zum Ende
hin ausgewählt. Ebenso wie bei Zeichenketten kann zudem ein dritter Parameter
angegeben werden, der festlegt, jedes wie vielte Element ausgewählt werden soll:

.. code-block:: python

    liste_1[3:5]
    # Ergebnis: ['a', 'c', 2]

Ist der Wert des dritten Parameters negativ, so wird die Liste von hinten nach
vorne abgearbeitet.


.. _Mehrdimensionale Listen:

.. rubric:: Mehrdimensionale Listen

Listen können "verschachtelt" sein, eine Liste kann also weitere Listen als
Elemente beinhalten. Durch eine derartige Struktur könnten beispielsweise die
Werte einer Tabelle gespeichert werden, die aus mehreren Zeilen besteht, wobei
jede Zeile wiederum mehrere Spalten enthält.

Bei der Indizierung von verschachtelten Listen kann der Index-Operator mehrmals
hintereinander angewendet werden:

.. code-block:: python

    liste_3 = [ ['a','b','c'], ['d','e','f'], ['g','h','i'] ]

    # Zweites Listenelement ("Zeile") auswählen:

    liste_3[1]
    # Ergebnis: ['d','e','f']

    # Drittes Element ("Spalte") dieser Zeile auswählen:
    liste_3[1][2]
    # Ergebnis: 'f'

Durch die erste Indizierung wird im obigen Beispiel eine Teilliste ausgewählt;
auf diese Liste als Ergebnis der ersten Indizierung kann erneut der
Indexoperator angewendet werden, um ein darin enthaltenes Element (oder auch
einen Bereich) auszuwählen.

.. _Listen-Funktionen:

Listen-Funktionen
^^^^^^^^^^^^^^^^^

Für Listen existieren Funktionen, die in der Form ``liste.funktionsname()``
angewendet werden können.

.. _Listen verknüpfen:

.. rubric:: Listen verknüpfen

Durch ``liste_1.extend(liste2)`` können zwei Listen miteinander kombiniert
werden:

.. code-block:: python

    liste_1 = [1, 2, 3]
    liste_2 = [4, 5, 6]

    liste_1.extend(liste_2)

    liste_1
    # Ergebnis: [1, 2, 3, 4, 5, 6]

.. index:: extend()


Durch die Funktion ``extend()`` wird die erste Liste um die Elemente der zweiten
Liste erweitert; die Funktion ``extend()`` selbst liefert den Wert ``None`` als
Ergebnis zurück. Möchte man eine derartige neue Liste erstellen, ohne dabei die
ursprünglichen Listen zu verändern, kann der ``+``-Operator verwendet werden:

.. code-block:: python

    liste_1 = [1, 2, 3]
    liste_2 = [4, 5, 6]

    liste3 = liste_1 + liste_2

    liste_1
    # Ergebnis: [1, 2, 3]

    liste_2
    # Ergebnis: [4, 5, 6]

    liste_3
    # Ergebnis: [1, 2, 3, 4, 5, 6]

.. index:: append()

Ebenso kann beispielsweise mittels ``3 * liste_1`` eine Liste erzeugt werden,
die aus einer dreifachen Wiederholung der ``liste_1`` besteht:

.. code-block:: python

    liste_4 = 3 * liste_1 ; liste_4
    # Ergebnis: [1, 2, 3, 1, 2, 3, 1, 2, 3]

Möchte man eine zweite Liste als eigenes Element zu einer Liste hinzufügen, so
kann die Funktion ``append()`` verwendet werden:

.. code-block:: python

    liste_1.append(liste_2)
    # Ergebnis: [1, 2, 3, [4, 5, 6]]

.. _Listen sortieren:

.. rubric:: Listen sortieren

Mittels der Funktion ``sort()`` können die Elemente einer Liste in aufsteigender
Reihenfolge, mittels ``reverse()`` in absteigender Reihenfolge sortiert werden:

.. code-block:: python

    liste_5 = [3, 1, -5, 8, 2]

    # Liste sortieren:

    liste_5.sort()

    liste_5
    # Ergebnis: [-5, 1, 2, 3, 8]

    liste_5.reverse()

    liste_5
    # Ergebnis: [8, 3, 2, 1, -5]

.. rubric:: Elemente indizieren, einfügen und entfernen

Um zu prüfen, wie häufig ein bestimmtes Element in einer Liste enthalten ist,
kann die Funktion ``count()`` angewendet werden:

.. code-block:: python

    liste_1.count(3)
    # Ergebnis: 1

Soll nur geprüft werden, *ob* ein Element in einer Liste enthalten ist, so kann
auch das Schlüsselwort ``in`` verwendet werden; im obigen Beispiel könnte somit
``3 in liste_1`` geschrieben werden, um zu prüfen, ob das Element ``3`` in der
Liste vorkommt.

Die Position (des ersten Auftretens) eines Elements innerhalb einer Liste kann
mittels der Funktion ``index()`` bestimmt werden: [#]_

.. code-block:: python

    liste_1.index(3)
    # Ergebnis: 2

Demnach kann der Wert ``3`` im obigen Beispiel mittels ``liste_1[2]`` aufgerufen
werden und ist somit das dritte Element der Liste. Vor der Verwendung von
``index()`` sollte allerdings stets geprüft werden, ob sich das Element in der
Liste befindet, da ansonsten ein ``ValueError`` auftritt.

Mittels ``insert(indexnummer, element)`` kann ein neues Element
*vor* der angegebenen Indexnummer eingefügt werden:

.. code-block:: python

    # Neues Element vor dem dritten Element (Index 2) einfügen:
    liste_1.insert(2, "Hallo")

    liste_1
    # Ergebnis: [1, 2, "Hallo", 3]


Mittels ``remove(element)`` oder ``pop(indexnummer)`` können Elemente wieder aus
der Liste entfernt werden:

.. code-block:: python

    # Element "Hallo" aus Liste entfernen:
    liste_1.remove("Hallo")

    # Drittes Element entfernen:
    liste_1.pop(2)

    liste_1
    # Ergebnis: [1, 2]

Beim Aufruf der ``pop()``-Funktion wird das aus der Liste entfernte Objekt als
Ergebnis zurückgegeben, was beispielsweise in "Stacks" durchaus erwünscht ist.
Das Löschen eines Listenbereichs zwischen zwei Indexnummern ist mittels ``del
liste[n1:n2]`` möglich; auch bei dieser Bereichsangabe wird die obere Grenze
nicht mit eingeschlossen.

Zu beachten ist wiederum, dass ``remove()`` einen ``ValueError`` auslöst, wenn
sich das zu entfernende Element nicht in der Liste befindet, und ``pop()`` einen
``IndexError`` auslöst, wenn die Liste kürzer als die angegebene Indexnummer
oder leer ist.

.. rubric:: Listen kopieren

Listen können nicht einfach mittels des Zuweisungsoperators kopiert werden.
Versucht man dies, so wird lediglich eine neue Referenz erstellt, die auf die
gleiche Liste zeigt und die Inhalte der ursprünglichen Liste verändern kann:

.. code-block:: python

    # Liste erstellen:
    liste_1 = [0,1,2,3,4,5]

    # Neue Referenz auf die Liste:
    liste_2 = liste_1

    # Liste mittels der Referenz ändern:
    liste_2[0] = 1

    # Test:

    liste_1
    # Ergebnis: [1, 1, 2, 3, 4, 5]

Der Grund für dieses scheinbar seltsame Verhalten des Python-Interpreters liegt
darin, dass auf diese Weise Listen direkt verändert werden können, wenn sie als
:ref:`Argumente an Funktionen <Veränderliche und unveränderliche Argumente>`
übergeben werden. Da dies wesentlich häufiger vorkommt als das "echte" Kopieren
einer Liste, ist es in Python der Standard.

Um eine echte Kopie einer Liste zu erstellen, muss die Funktion ``copy()`` auf
die ursprüngliche Liste angewendet werden:

.. code-block:: python

    # Liste erstellen:
    liste_1 = [0,1,2,3,4,5]

    # Kopie der Liste erstellen:
    liste_2 = liste_1.copy()

Werden jetzt die Inhalte der zweiten Liste geändert, so bleiben die Inhalte der
ersten Liste bestehen.

.. TODO Listen kopieren mit copy(), sonst nur Referenzen!

.. _List-Comprehensions:

List-Comprehensions
^^^^^^^^^^^^^^^^^^^

Mit Hilfe so genannter List-Comprehensions können aus bestehenden Listen neue
Listen erzeugt werden; dabei können beispielsweise Filter auf die die Elemente
der bestehenden Liste angewendet werden; ebenso ist es möglich, Funktionen auf
alle Elemente der bestehenden Liste anzuwenden und die jeweiligen Ergebnisse in
der neuen Liste zu speichern.

*Beispiele:*

* Alle Elemente einer bestehenden Liste sollen quadriert werden:

  .. code-block:: python

      # Ausgangsliste erstellen:
      alte_liste = [1, 2, 3, 4, 5]

      # List Comprehension anwenden:
      neue_liste = [i**2 for i in alte_liste]

      neue_liste
      # Ergebnis: [1, 4, 9, 16, 25]

  In diesem Beispiel wird für jedes Element der bestehenden Liste, das jeweils
  mit einer temporären Variablen ``i`` bezeichnet wird, der Quadratwert ``i**2``
  berechnet und das Ergebnis als neue Liste gespeichert.

* Aus einer bestehenden Liste sollen alle geradzahligen Werte ausgewählt werden:

  .. code-block:: python

      # Ausgangsliste erstellen:
      alte_liste = [1, 2, 3, 4, 5]

      # List Comprehension anwenden:
      neue_liste = [i for i in alte_liste if i % 2 == 0]

      neue_liste
      # Ergebnis: [2, 4]

  In diesem Beispiel werden die Elemente der bestehenden Liste, wiederum
  kurz mit ``i`` bezeichnet, unverändert in die neue Liste aufgenommen, sofern
  sie die angegebene Bedingung ``i % 2 == 0`` erfüllen.

* Aus zwei bestehenden Listen sollen alle Elemente ausgewählt werden, die in
  beiden Listen enthalten sind:

  .. code-block:: python

      # Ausgangslisten erstellen:
      liste_1 = [1, 2, 3, 4, 5]
      liste_1 = [2, 3, 4, 5, 6]

      # List Comprehension anwenden:
      gemeinsame_elemente = [i for i liste_1 if i in liste_2]

      gemeinsame_elemente
      # Ergebnis: [2, 3, 4, 5]

  In diesem Beispil wird mittels der temporären Variablen ``i`` schrittweise
  geprüft, ob die Elemente der ersten Liste auch in der zweiten Liste enthalten
  sind und gegebenenfalls in die neue Liste aufgenommen.

* Die Werte zweier Listen sollen elementweise miteinander multipliziert werden:

  .. code-block:: python

      # Ausgangslisten erstellen:
      liste_1 = [1, 2, 3, 4, 5]
      liste_2 = [2, 3, 4, 5, 6]

      # List Comprehension anwenden:
      produkte = [liste_1[i] * liste_2[i] for i in range(5)]

      produkte
      # Ergebnis: [2, 6, 12, 20, 30]

  In diesem Beispiel wurde mit Hilfe der Funktion :ref:`range() <range()>` ein
  Bereich an ganzen Zahlen festgelegt, den die Variable ``i`` durchlaufen soll.
  Die Variable ``i`` bezeichnet in diesem Fall also nicht ein konkretes Element
  einer Liste, sondern vielmehr eine Indexnummer; mittels dieser Indexnummer
  kann dann auf die Elemente der Ausgangslisten zugegriffen werden.

  Auch eine zusätzliche :ref:`if <if>`-Bedingung, beispielsweise ``if liste_1[i]
  > 2`` wäre in diesem Fall möglich, würde logischerweise aber zu einem anderen
  Ergebnis führen.

List Comprehensions ermöglichen es allgemein, neue Listen schnell und gut lesbar
zu erzeugen.


.. index:: Menge, set, frozenset
.. _Mengen:

``set`` und ``frozenset`` -- Mengen
-----------------------------------

Ein Set bezeichnet in Python eine Menge an Objekten beliebigen Datentyps, wobei
jedes Objekt nur ein einziges Mal in der Menge enthalten sein darf. Sets werden
in Python in geschweifte Klammern gesetzt: Durch Anwendung von Operatoren auf
paarweise je zwei Sets können -- entsprechend den Regeln der :ref:`Mengenlehre
<gwm:Mengenlehre>` -- neue Sets gebildet werden.

.. code-block:: python

    set_1 = {"a", "b", "c", 1, 2, 3}    # oder: set( ["a", "b", "c", 1, 2, 3] )
    set_2 = {"b", "c", "d", 2, 3, 4}

    # Schnittmenge:

    set_1 & set_2
    # Ergebnis: {'b', 'c', 2, 3}

    # Vereinigungsmenge:

    set_1 | set_2
    # Ergebnis: {'a', 'b', 'c', 'd', 1, 2, 3, 4}

    # Differenzmenge:

    set_1 \ set_2
    # Ergebnis: {'a', 1}

    # Symmetrische Differenz (Entweder-Oder):

    set_1 ^ set_2
    # Ergebnis: {'a', 1, 4, 'd'}


    # Test, ob set_1 eine Obermenge von set_2 ist:

    set_1 > set_2
    # Ergebnis: False

Mengen können unter anderem dazu genutzt werden, um aus einer Liste alle
mehrfach vorkommenden Elemente heraus zu filtern. Hierzu wird etwa folgende
Syntax genutzt:

.. code-block:: python

    any_list = ["a", "a", "b", "c", 1, 2, 2, 3]

    list_with_unique_elements = list(set(any_list))
    # Ergebnis: ["a", "b", "c", 1, 2, 3]

Zum Arbeiten mit Mengen sind zusätzlich folgende Funktionen nützlich:

* Mit der ``add()``-Funktion lassen sich Elemente zu einer Menge hinzufügen,
  beispielsweise ``my_set.add('x')``.
* Mit der ``discard()``-Funktion lassen sich Elemente aus einer Menge entfernen,
  beispielsweise ``my_set.discard('x')``.
* Mit der ``copy()``-Funktion kann eine Kopie einer Menge erstellt werden,
  beispielsweise ``my_set2 = my_set_.copy()``.
* Mit der ``clear()``-Funktion können alle Elemente einer Menge gelöscht
  werden, beispielsweise ``my_set2.clear()``.

Neben üblichen Sets können mittels der Funktion ``frozenset()``  auch
unveränderliche Listen erzeugt werden.

.. index:: dict
.. _Wörterbücher:
.. _dict:

``dict`` -- Wörterbücher
------------------------

In Python existiert ein weiterer Datentyp für Schlüssel-Wert-Paare. Ein
solches ``dict`` ist somit aufgebaut wie ein Wörterbuch, das zu jedem Eintrag
(Schlüssel) eine passende Erläuterung (Wert) liefert.

Zur Darstellung von ``dicts`` werden in Python geschweifte Klammern verwendet.
Als Schlüssel werden meist ``strings`` genutzt, die zugehörigen Werte werden
durch einen Doppelpunkt getrennt angegeben. Die einzelnen Schlüssel-Wert-Paare
werden -- wie die Elemente einer Liste -- mit je einem Komma voneinander
getrennt aufgelistet.

.. code-block:: python

    # Beispiel:

    address-book = {
        name_1 : adresse_1,
        name_2 : adresse_2,
        name_3 : adresse_3,
        ...
        }

Auf die einzelnen Werte eines ``dicts`` kann mittels des Index-Operators
zugegriffen werden, wobei jedoch nicht ein numerischer Wert, sondern der Name
eines Schlüssels in den eckigen Klammern angegeben wird:

.. code-block:: python

    address-book[name_1]
    # Ergebnis: adresse_1

.. index:: View, keys() (dict-Methode), values() (dict-Methode), items() (dict-Methode)

Mittels der ``dict``-Funktionen ``keys()``, ``values()`` und ``items()`` lassen
sich so genannte "Views" eines Wörterbuchs erzeugen. Bei einem View handelt es
sich um eine Listen-Variable, die automatisch aktualisiert wird, wenn das
zugehörige ``dict`` geändert wird.

.. list-table::
    :name: tab-dict-funktionen
    :widths: 20 50 30

    * - Funktion
      - Ergebnis
      - Beschreibung
    * - ``anydict.keys()``
      - ``[key_1, key_2, ...]``
      - Liste mit allen Schlüsseln
    * - ``anydict.values()``
      - ``[value_1, value_2, ...]``
      - Liste mit allen Werten
    * - ``anydict.items()``
      - ``[(key_1, value_1), (key_2, value_2), ...]``
      - Liste von Schlüssel-Wert-Tupeln

Mit ``key_1 in anydict`` kann geprüft werden, ob der Schlüssel ``key_1`` im
Wörterbuch ``anydict`` vorhanden ist (Ergebnis: ``True`` oder ``False``).

Um den zum Schlüssel ``key_1`` gehörigen Wert von ``anydict`` auszugeben, kann
der Index-Operator ``[ ]`` genutzt werden:

.. code-block:: python

    anydict[key_1]
    # Ergebnis: value_1 oder Error

Ist der Schlüssel nicht vorhanden, wird ein ``KeyError`` ausgelöst. Möchte
man dies verhindern, so kann man folgenden Code nutzen:

.. code-block:: python

    anydict.get(key1, default=None)
    # Ergebnis: value_1 oder None

.. Eintrag löschen: del()
.. Einträge in dict1 ergänzen bzw. aktualisieren mittels neuem dict: dict_1.update(dict_2)
.. Anzahl der Elemente: len(mydict)

.. index:: file
.. _Dateien:

``file`` -- Dateien
-------------------

Datei-Objekte stellen in Python die Hauptschnittstelle zu externen Dateien auf
dem Computer dar. Sie können genutzt werden, um Dateien beliebigen Typs zu
lesen oder zu schreiben.

Datei-Objekte werden erzeugt, indem man die Funktion ``open()`` aufruft, und
dabei den Namen der Datei sowie ein Kürzel für den gewünschten
Bearbeitungsmodus angibt:

.. code-block:: python

    myfile = open("file.txt", "r")

Als Bearbeitungsmodus kann ``"r"`` (lesen), ``"w"`` (schreiben) oder ``"rw"``
(lesen und schreiben) gewählt werden. Sollen binäre Dateien gelesen
beziehungsweise geschrieben werden, muss an das jeweilige Kürzel ein ``b``
angehängt werden, beispielsweise bezeichnet ``"rb"`` den Lesemodus einer
binären Datei.


.. _Einlesen von Dateien:

.. rubric:: Einlesen von Dateien

Wird eine Datei im Lesemodus geöffnet, so kann sie beispielsweise mittels der
Funktion ``read()`` im Ganzen als ein einziger String eingelesen werden:

.. code-block:: python

    # Datei als einzelnen String einlesen:
    long_string = myfile.read()

Diese Methode ist für größere Dateien nicht empfehlenswert. Besser ist es,
mittels der Funktion ``readline()`` eine Datei Zeile für Zeile einzulesen.
Bei jedem solchen Aufruf wird die jeweils eingelesene Zeile als Ergebnis
zurückgegeben und der "Cursor" für die aktuelle Position in der Datei auf die
nächste Zeile gesetzt.

Noch einfacher ist ein zeilenweises Einlesen, indem die Datei-Variable selbst
als iterierbares Objekt an eine :ref:`for <for>`-Schleife übergeben wird:

.. code-block:: python

    # Schleife über alle Zeilen der Datei:
    for line in myfile:

        # Gib die aktuelle Zeile aus:
        print(line)

Am Ende eines Lesezugriffs sollte die Datei mittels ``close(myfile)`` wieder
geschlossen werden.


.. _Schreiben in Dateien:

.. rubric:: Schreiben in Dateien

Um Text in eine Datei zu schreiben, wird diese zunächst im Schreibmodus
geöffnet:

.. code-block:: python

    myfile = open("file.txt", "w")

Anschließend kann mittels der Funktion ``write()`` eine (gegebenenfalls auch
mehrzeilige) Zeichenkette in die Datei geschrieben werden:

.. code-block:: python

    myfile.write("Hallo Welt!\n")

Am Ende eines Schreibzugriffs *muss* die Datei mittels ``close(myfile)`` wieder
geschlossen werden, da nur dann das Datei-Attribug ``mtime``
("Modifikationszeit") korrekt gesetzt wird.

..  seek moves to a new file position.

.. https://docs.python.org/3/library/io.html

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] In der Mathematik wird die imaginäre Einheit meist mit :math:`i`
    bezeichnet, in der Elektrotechnik wird hingegen oft :math:`j` verwendet.
    In Python kann sowohl ``j`` als auch ``J`` als Symbol für die imaginäre
    Einheit geschrieben werden.

.. [#] Python behandelt einfache und doppelte Anführungszeichen gleichwertig,
    anders als beispielsweise die Linux-Shell. Innerhalb eines Strings, der in
    einfache Anführungszeichen gesetzt wird, können doppelte
    Anführungszeichen vorkommen und umgekehrt.

    Sollen einfache Anführungszeichen in einem String vorkommen, der ebenfalls
    durch einfache Anführungszeichen begrenzt ist, so muss vor die inneren
    Anführungszeichen jeweils ein Backslash (``\``) als Escape-Sequenz gesetzt
    werden.

.. [#] Genau genommen sind bei einem Tupel (oder auch einem ``frozenset``) nur
    die Referenzen auf die enthaltenen Objekte unveränderlich. Enthält ein Tupel
    beispielsweise als erstes Argument eine Liste namens ``l``, so kann dieser
    mittels ``l.insert(0, "Hallo!")`` ein neues Element hinzugefügt werden. Das
    Tupel ändert sich dabei nicht, da die ID der Liste ``l`` unverändert bleibt.

.. [#] Die Funktionen ``count()`` und ``index()`` sind die einzigen beiden
    Listenfunktionen, die auch für die unveränderlichen Tupel definiert sind.

..  .. [#] Zeichen werden von Python wie unveränderliche Listen einzelner Zeichen behandelt.
       ..  Hat man beispielsweise eine Liste mit einzelnen Buchstaben oder Ziffern,
       ..  die man zu einem String zusammenfügen möchte, so kann man dies mittels
       ..  ``''.join(mylist)`` (Verbindung aller Zeichen ohne Leerzeichen) oder
       ..  ``' '.join(mylist)`` (Verbindung aller Zeichen mit Leerzeichen)
       ..  erreichen.

