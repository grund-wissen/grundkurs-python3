.. _Einführung:

Einführung
===========

.. only:: latex

    Python ist eine Programmiersprache, die einfach zu erlernen ist und ein
    schnelles Entwickeln von Programmen ermöglicht. Aufgrund der verhältnismäßig
    hohen Lesbarkeit und einiger hilfreicher Mathematik-Module wird Python auch im
    akademischen und schulischen Bereich häufig verwendet.


.. _Interaktiver Modus:

Interaktiver Modus
------------------

Um Python im interaktiven Modus zu starten, ruft man den Interpreter in einer
Shell ohne weitere Parameter auf:

.. code-block:: bash

    python3

Nach dem Eingabeprompt ``>>>`` kann beliebiger Python-Code eingegeben werden.
Drückt man die Enter-Taste, so wird dieser unmittelbar ausgeführt. So lässt sich
der Python-Interpreter beispielsweise als besserer Taschenrechner benutzen: [#]_

.. code-block:: python

    >>> 5 + 3       # Addition
    8
    >>> 7 * 21      # Multiplikation
    147
    >>> 15 ** 2     # Potenz
    225
    >>> 14 / 80     # Division
    0.175

Möchte man ausführlicher im interaktiven Modus arbeiten, so lohnt es sich,
:ref:`Ipython zu installatieren <Installation von Ipython3>` und ``ipython3``
als Shell-Version beziehungsweise ``ipython3 qtconsole`` als GUI-Version
aufzurufen. Beide Varianten von Ipython bieten Vervollständigungen der Eingabe
durch Drücken der Tab-Taste, die GUI-Version beitet zudem Syntax-Highlighting
und ein automatisches Einblenden von Funktionsbeschreibungen (":ref:`Docstrings
<Docstring>`").



.. index:: help()
.. rubric:: Interne Hilfe

Jeder Python-Interpreter bietet dem Nutzer im interaktiven Modus die
Möglichkeit, weitere Informationen oder Dokumentationen zu Python-Objekten
(Funktionen, Operatoren usw.) anzuzeigen. Um Hilfe zu einem beliebigen
Python-Objekt zu erhalten, kann die Funktion ``help()`` genutzt werden:

.. code-block:: python

    # Hilfe zur print()-Funktion anzeigen:
    help(print)

.. index:: id()

Ebenso können Variablen an die Help-Funktion übergeben werden, um Hilfe zum
jeweiligen Objekttyp zu erhalten. Mit ``type(object_name)`` kann der Typ eines
Objekts, mit ``id(variable_name)`` zusätzlich die aktuelle Speicheradresse des
Objekts angezeigt werden.

.. _Python-Skripte:

Python-Skripte
--------------

Python-Code, der bei der interaktiven Benutzung des Interpreters eingegeben
werden kann, kann in gleicher Form ebenso in Textdateien ("Skripte"),
üblicherweise mit der Endung ``.py``, geschrieben werden. Derartige Dateien
können entweder in einer interaktiven Python-Sitzung mittels
``execfile("skriptname.py")`` oder folgendermaßen in einem Shellfenster
aufgerufen werden:

.. code-block:: bash

    python3 skriptname.py

Beim Aufruf eines Skripts wandelt Python den Quellcode in so genannten
"Bytecode" um und führt diesen aus. Wird eine Quellcode-Datei anderen Dateien
importiert, so legt Python automatisch eine zusätzliche Datei ``skriptname.pyc``
im gleichen Verzeichnis an.

Es ist auch möglich, eine Skriptdatei direkt als ausführbare Datei aufzurufen.
Dazu fügt man zunächst folgende Zeilen am Anfang der Skriptdatei ein:

.. code-block:: python

    #!/usr/bin/python3
    # -*- coding: utf-8 -*-

Die erste Zeile wird "Shebang" genannt und gibt den Pfad zum Python-Interpreter
an, der beim Aufruf des Skripts geladen werden soll; die zweite Zeile gibt an,
welcher Zeichensatz in der Datei verwendet wird (``utf-8`` ist Standard unter
Linux).

Mit der obigen Ergänzung kann die Skriptdatei dann mittels :ref:`chmod
<gwl:chmod>` ausführbar gemacht werden:

.. code-block:: bash

    chmod +x skriptname.py

Das Skript kann damit mittels ``./skriptname.py`` aus dem aktuellen Pfad heraus
oder allgemein mittels ``pfad-zum-skript/skriptname.py`` aufgerufen werden. Soll
es benutzerweit aufrufbar sein, so empfiehlt es sich, einen :ref:`Symlink
<gwl:Symlink>` zum Skript im Verzeichnis ``~/bin`` zu erstellen und dieses
durch folgenden Eintrag in der ``~/.bashrc`` zum Systempfad hinzuzufügen: [#]_

.. code-block:: bash

    if [ -d "$HOME/bin" ] ; then
        PATH="$HOME/bin:$PATH"
        export PATH;
    fi

Das Schreiben von Code-Dateien ist in Python gegenüber der interaktiven
Benutzung des Interpreters unter anderem deshalb von Vorteil, da Python
beispielsweise bei der Definition von :ref:`Funktionen <Funktionen>` und
:ref:`Kontrollstrukturen <Kontrollstrukturen>` Einrückungen statt Klammern zur
Gliederung des Quellcodes verwendet.

Gute Texteditoren machen den Umgang mit Einrückungen einfach und bieten
obendrein Vorteile wie Syntax-Highlighting, Eingabe-Vervollständigungen,
Snippets, usw. Bei Verwendung von :ref:`Vim <gwl:Texteditor Vim>` und des
:ref:`Vicle <gwl:Vicle>`-Plugins ist es zudem auch während des Schreibens der
Textdateien möglich, einzelne Code-Zeilen oder auch ganze Code-Blöcke an eine
laufende Interpreter-Sitzung zu senden; so können die Vorteile des Interpreters
(beispielsweise Ausgabe von Variablenwerten und Zwischenergebnissen) und des
Texteditors kombiniert werden.

Umfangreichere Skripte sollten zur besseren Lesbarkeit mit Kommentaren versehen
werden. Kommentare werden durch das Raute-Symbol ``#`` eingeleitet und gehen bis
zum Ende der Zeile.


.. index:: Variable
.. _Variablen:

Variablen
---------

Eine wichtige Eigenschaft von Computer-Programmen ist, dass sie nahezu beliebig
viele Werte und Zeichen in entsprechenden Platzhaltern ("Variablen") speichern
und verarbeiten können. Auf so gespeicherte Werte kann man im Verlauf des
Programms wieder zugreifen und/oder den Variablen neue Werte zuweisen.

In Python können Variablennamen aus Groß- und Kleinbuchstaben, Ziffern und dem
Unterstrich-Zeichen bestehen, wobei sie nicht mit einer Ziffer beginnen dürfen.
Bei der Benennung von Variablen ist außerdem auf Groß- und Kleinschreibung zu
achten, beispielsweise bezeichnen ``var_1`` und ``Var_1`` zwei unterschiedliche
Variablen. Zudem dürfen keine von der Programmiersprache reservierten Wörter als
Variablennamen verwendet werden (beispielsweise ``and, or, is, type, key`` usw.)

.. Sonderzeichen sollten ebenso vermieden werden, also laenge statt länge.

Ein Wert kann in einer Variablen mittels des Zuweisungs-Operators ``=``
gespeichert werden:

.. code-block:: python

    var_1 = "Hallo!"
    var_2 = 42

In Python dient das ``=``-Zeichen somit ausschließlich der Zuweisung von Werten;
für einen Werte-Vergleich muss hingegen das doppelte Istgleich-Zeichen ``==``
verwendet werden.

Im interaktiven Modus wird der Wert einer Variablen angezeigt, indem man deren
Namen in einer neuen Zeile eingibt und ``Enter`` drückt. In Skripten werden die
Werte von Variablen oftmals mittels der Funktion ``print()`` angezeigt:

.. code-block:: python

    print(var_1)
    print(var_2)

Bei der Verwendung von ``print()`` werden dabei die Variable als
:ref:`Zeichenkette <Zeichenketten>` ausgegeben.

Variablen werden in Python dynamisch typisiert, das heißt in der gleichen
Variablen können im Verlauf des Programms verschiedene :ref:`Datentypen
<Datentypen>` zugewiesen werden.

.. Löschen von Variablen mit del(), Garbate Collection?

.. index:: Operator
.. _Operatoren:

Operatoren
----------

Bei der Auswertung einzelner mathematischer Ausdrücke gilt wie üblich
"Punkt vor Strich". Um eine andere Auswertungsreihenfolge zu bewirken,
können einzelne Ausdrücke, wie in der Mathematik üblich, durch runde
Klammern zusammengefasst werden.

.. index:: Auswertungsreihenfolge

Für die in Python üblichen Operatoren ist eine allgemein gültige "Rangfolge" für
die Auswertungsreihenfolge festgelegt. In der folgenden Tabelle sind die
Operatoren mit der höchsten Priorität stehen oben, gleichberechtigte Operatoren
(die von links nach rechts ausgewertet werden) stehen in der gleichen Zeile.
[#]_

.. only:: html

    .. list-table::
        :name: tab-rangfolge-von-operatoren
        :widths: 10 50

        * - Operator
          - Bedeutung
        * - ``()``
          - Gruppierung
        * - ``x[]``, ``x.attribute``
          - Listenzugriff (siehe :ref:`Listen <Listen und Tupel>`),
            Objekteigenschaft
        * - ``**``
          - Potenz
        * - ``+`` und ``-``
          - Positives beziehungsweise negatives Vorzeichen einer Zahl
        * - ``*``, ``/``, ``//``, ``%``
          - Multiplikation, Division, Ganzzahl-Division, Rest (Modulo)
        * - | ``==``, ``<=``, ``<``,
            | ``!=``, ``>=``, ``>``,
            | ``is``, ``is not``,
            | ``in``, ``not in``
          - | Wertevergleich (gleich, kleiner als oder gleich, kleiner als,
            |                 ungleich, größer als oder gleich, größer als)
            | Identitätsvergleich
            | Test auf Mengenzugehörigkeit
        * - ``not``
          - Logisches Nicht
        * - ``and``
          - Logisches Und
        * - ``or``
          - Logisches Oder

.. raw:: latex

    \begin{table}[h!]
    \label{tab-rangfolge-von-operatoren}
    \begin{center}
    \begin{tabular}{|p{3.35cm}|p{9cm}|}
        \hline
        Operator & Bedeutung \\\hline
        \verb|()|
        & Gruppierung \\\hline
        \verb|x[]|, \verb|x.attribute| &
        Listenzugriff (siehe \hyperref[Listen und Tupel]{\emph{Listen}}),
            Objekteigenschaft \\\hline
        \verb|**| &  Potenz \\\hline
        \verb|+| und \verb|-| &
        Positives beziehungsweise negatives Vorzeichen einer Zahl \\\hline
        \verb|*|, \verb|/|, \verb|//|, \verb|%| &
        Multiplikation, Division, Ganzzahl-Division, Rest (Modulo) \\\hline
        \verb|==|, \verb|<=|, \verb|<|,
        \verb|!=|, \verb|>=|, \verb|>|,
        \verb|is|, \verb|is not|,
        \verb|in|, \verb|not in| &
        Wertevergleich (gleich, kleiner als oder gleich, kleiner als,
                        ungleich, größer als oder gleich, größer als),
        Identitätsvergleich,
        Test auf Mengenzugehörigkeit \\\hline
        \verb|not| & Logisches Nicht \\\hline
        \verb|and| & Logisches Und \\\hline
        \verb|or| & Logisches Oder \\\hline
    \end{tabular}
    \end{center}
    \end{table}

..  (siehe :ref:`Klassen <Klassen>`)


In Python muss zwischen dem Wertevergleich ``==`` und der Objekt-Identität
``is`` unterschieden werden. Beispielsweise liefert ``3/2 == 1.5`` das Ergebnis
``True``, da die numerischen Werte übereinstimmen; hingegen liefert ``3/2 is
1.5`` das Ergebnis ``False``, da es sich einmal um einen mathematischen Ausdruck
und einmal um eine Zahl handelt.

.. index:: Zuweisungsoperator

.. rubric:: Kombinierte Zuweisungsoperatoren

Neben dem gewöhnlichen Zuweisungsoperator ``=`` gibt es in Python weitere,
kombinierte Zuweisungsoperatoren. Mit diesen wird ein mathematischer Operator
mit einer Zuweisung verbunden; die Variable wird dabei also um den jeweiligen
Wert verändert.

.. list-table::
    :name: tab-kombinierte-zuweisungen
    :widths: 20 90

    * - ``+=``
      - Erhöhung der links stehenden Variable um Wert auf der rechten Seite
    * - ``-=``
      - Erniedrigung der links stehenden Variable um Wert auf der rechten Seite
    * - ``*=``
      - Multiplikation der links stehenden Variable mit Wert auf der rechten
        Seite
    * - ``/=``
      - Division der links stehenden Variable durch Wert auf der rechten Seite
    * - ``//=``
      - Ganzzahlige Division der links stehenden Variable durch Wert auf der
        rechten Seite
    * - ``//=``
      - Rest bei ganzzahliger Division der links stehenden Variable durch Wert
        auf der rechten Seite
    * - ``**=``
      - Potenzieren einer Variable mit Wert auf der rechten Seite

Beispielsweise kann auf diese Weise mit ``x **= 2`` der aktuelle Wert der
Variablen ``x`` quadriert werden. Für Zeichenketten existieren nach dem
gleichen Prinzip die Operatoren ``+=`` und ``*=``, die zum String auf der linken
Seite einen weiteren String anhängen bzw. den String auf der linken Seite
mehrfach wiederholt aneinander reihen.


.. _Kombinierte Vergleichsoperatoren:

.. rubric:: Kombinierte Vergleichsoperatoren

Eine weitere Besonderheit in Python liegt darin, dass mehrere
Vergleichsoperatoren unmittelbar miteinander kombiniert werden können;
beispielsweise kann wie in der Mathematik ``1 < 2 < 3`` geschrieben werden.
Die einzelnen Teilausdrücke muss man sich dabei  mit einem ``and``-Operator
verbunden denken, denn der Ausdruck ist genau dann wahr, wenn ``1 < 2 and 2 <
3`` gilt.

Die "Verkettungsregel" gilt für alle Vergleichsoperatoren, auch wenn das
Ergebnis nicht immer mit der eigenen Erwartung übereinstimmen muss.
Beispielsweise könnte man im Fall ``1 == 2 < 3`` das Ergebnis ``True`` erwarten,
wenn man sich die gleichwertigen Operatoren von links nach rechts ausgewertet
denkt, denn ``1 == 2`` ist ``False`` und zudem ist ``False < 3``. Die Aussage
liefert in Python jedoch ``False`` als Ergebnis, denn sie wird als ``1 == 2 and
2 < 3`` interpretiert, und zwei mit ``and`` verknüpfte Aussagen ergeben nur dann
ein wahres Ergebnis, wenn beide Aussagen wahr sind.


Im Zweifelsfall können die einzelnen Teilaussagen jederzeit mit Hilfe von runden
Klammern gruppiert werden, um eine ungewollte Auswertungsreihenfolge zu
vermeiden.

.. index:: Ternärer Operator
.. _Bedingte Wertzuweisung:

.. rubric:: Bedingte Wertzuweisung

In Programmiersprachen wie ``C`` gibt es ein Sprachkonstrukt, dass einem
"ternären" Operator entspricht, also ein Operator mit drei notwendigen
Argumenten. In ``C`` lautet dieser Operator etwa ``x = condition ? a : b``, was
bedeutet, dass der Variablen :math:`x` der Wert ``a`` zugewiesen wird, wenn die
Bedingung ``condition`` wahr ist; andernfalls wird der Variablen ``x`` der Wert
``b`` zugewiesen.

In Python lautet das entsprechende Sprachkonstrukt folgendermaßen:

.. code-block:: python

    x = a if condition else b

Auch hier wird zunächst die Bedingung ``condition`` geprüft. Wenn diese den
Wert ``True`` ergibt, so wird der Variablen ``x`` der Wert ``a`` zugewiesen,
andernfalls der Wert ``b``.



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. index:: divmod()

.. [#] Neben der gewöhnlichen Division mit ``/`` kann auch mit ``//`` eine
    Ganzzahl-Division durchgeführt werden. Bei einer solchen Division wird der
    Divisionsrest weggelassen und stattdessen die nächst kleinere ganze Zahl als
    Ergebnis zurückkgegeben; beispielsweise ergibt ``17 // 5`` den Wert ``3``.
    Der Divisionsrest kann mit dem Modulo-Operator ``%`` bestimmt werden;
    beispielsweise ergibt ``17 % 5`` den Wert ``2``. Beide Werte können auf
    einmal durch die Funktion ``divmod()`` ausgegeben werden; beispielsweise
    ergibt ``divmod(17,5)`` das Zahlenpaar (3,2).

    Wurzeln können entweder als Potenzen mit einer rationalen Zahl als Exponent
    oder mittels der Funktion ``math.sqrt()`` aus dem ``math``-Modul berechnet
    werden.

.. [#] Dieser Trick ist im :ref:`Shell-Skripting <gwl:Aufbau und Aufruf eines
    Shellskripts>`-Tutorial näher beschrieben.

.. [#] Eine Ausnahme bildet der Potenz-Operator ``**``: Werden mehrere Potenzen
    in einem Ausdruck kombiniert, so werden diese von rechts nach links
    ausgewertet. Somit gilt ``2 ** 2 ** 3 == 2 ** 8 == 256``. Für eine
    andere Auswertungsreihenfolge muss ``(2 ** 2) ** 3 == 4 ** 3 == 64``
    geschrieben werden.

