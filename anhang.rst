.. _Anhang:

Anhang
======


.. _Schlüsselwörter:

Schlüsselwörter
---------------

In Python3 sind folgende Schlüsselwörter vordefiniert:

+-------+----------+---------+--------+----------+--------+-------+
| False | assert   | del     | for    | in       | or     | while |
+-------+----------+---------+--------+----------+--------+-------+
| None  | break    | elif    | from   | is       | pass   | with  |
+-------+----------+---------+--------+----------+--------+-------+
| True  | class    | else    | global | lambda   | raise  | yield |
+-------+----------+---------+--------+----------+--------+-------+
| and   | continue | except  | if     | nonlocal | return |       |
+-------+----------+---------+--------+----------+--------+-------+
| as    | def      | finally | import | not      | try    |       |
+-------+----------+---------+--------+----------+--------+-------+

Mittels der Funktion ``iskeyword()`` aus dem Modul ``keyword`` kann getestet
werden, ob eine Zeichenkette ein Schlüsselwort ist:

.. code-block:: python

    from keyword import iskeyword()

    iskeyword("lambda")
    # Ergebnis: True


.. _Standardfunktionen:

Standardfunktionen
------------------

Die im folgenden Abschnitt beschriebenen Funktionen sind standardmäßig in Python
definiert, ohne dass ein zusätzliches Modul geladen werden muss: [#]_

.. index:: abs()
.. _abs():

abs()
^^^^^

Die Funktion ``abs(x)`` gibt den Absolutwert einer Zahl ``x`` als Ergebnis zurück.

.. index:: all()
.. _all():

all()
^^^^^

Die Funktion ``all()`` kann auf ein beliebiges iterierbares Objekt (Listen oder
Mengen) angewendet werden. Als Ergebnis wird ``True`` zurückgegeben, wenn
alle Elemente den :ref:`booleschen <bool()>` Wahrheitswert ``True``
besitzen; andernfalls wird ``False`` als Ergebnis zurückgegeben.


.. index:: any()
.. _any():

any()
^^^^^

Die Funktion ``any()`` kann auf ein beliebiges iterierbares Objekt (Listen oder
Mengen) angewendet werden. Als Ergebnis wird ``True`` zurückgegeben, wenn
zumindest ein Element den :ref:`booleschen <bool()>` Wahrheitswert ``True``
besitzt; andernfalls wird ``False`` als Ergebnis zurückgegeben.


.. index:: bin()
.. _bin():

bin()
^^^^^

Die Funktion ``bin(x)`` gibt eine Zeichenkette mit der Binärdarstellung einer
einer Integer-Zahl als Ergebnis zurück. Eine solche Zeichenkette wird mit ``0b``
eingeleitet, gefolgt von der eigentlichen Binärzahl; beispielsweise ergibt
``bin(42)`` die Zeichenkette ``'0b101010'``.


.. index:: bool()
.. _bool():

bool()
^^^^^^

Die Funktion ``bool()`` gibt den Wahrheitswert eines logischen Ausdrucks an;
dieser kann entweder ``True`` oder ``False`` sein. Als Argument kann entweder
ein mittels :ref`Vergleichsoperatoren <Operatoren>` erzeugter logischer
Ausdruck oder auch ein einzelnes Objekt übergeben werden.

Eine Liste, ein Tupel oder eine Zeichenkette hat beispielsweise den
Wahrheitswert ``True``, wenn sie nicht leer ist (also mindestens ein Zeichen
enthält); Zahlen haben dann den Wahrheitswert ``True``, wenn sie nicht gleich
Null sind. ``bool(None)`` liefert den Wahrheitswert ``False``.


.. index:: bytearray()
.. _bytearray():

bytearray()
^^^^^^^^^^^

Die Funktion ``bytearray()`` erzeugt ein neues Bytearray-Objekt. Dieser Datentyp
besteht aus ganzzahligen Werten zwischen ``0`` und ``255`` und ist, ähnlich wie
der Datentyp ``str`` zur Speicherung von Zeichenketten in Textdateien vorgesehen
ist, zur Speicherung von binären Daten gedacht.


.. index:: bytes()
.. _bytes():

bytes()
^^^^^^^

Die Funktion ``bytes()`` erzeugt ein neues Bytes-Objekt. Dieses entspricht im
Wesentlichen einem :ref:`bytearray <bytearray()>`-Objekt, ist aber nicht
veränderlich (so wie ein :ref:`Tupel <Tupel>` eine unveränderliche :ref:`Liste
<Liste>` darstellt).


.. index:: chr()
.. _chr():

chr()
^^^^^

Die Funktion ``chr()`` gibt zu einem angegebenen Ganzzahl-Wert mit positivem
Vorzeichen das entsprechende Unicode-Zeichen aus; beispielsweise gibt
``chr(97)`` als Ergebnis ``'a'`` zurück.

Für viele Programme reichen die `ASCII-Codes`_ als Teilmenge des
Unicode-Zeichensatzes bereits aus.


.. index:: classmethod()
.. _classmethod():

classmethod()
^^^^^^^^^^^^^

.. Die Funktion ``classmethod()``

.. index:: cmp()
.. _cmp():

cmp()
^^^^^

Die Funktion ``cmp()``

.. index:: compile()
.. _compile():

compile()
^^^^^^^^^

Die Funktion ``compile()``

.. index:: complex()
.. _complex():

complex()
^^^^^^^^^

Die Funktion ``complex()`` erstellt eine neue :ref:`komplexe Zahl <Komplexe
Zahlen>`  aus zwei angegebenen Zahlen oder einem angegebenen String;
beispielsweise erzeugt ``complex(1.5, 2)`` die komplexe Zahl ``(1.5+2j)``.

Wird ein String als Argument angegeben, so muss darauf geachtet werden, dass
kein Leerzeichen zwischen dem Realteil, dem Pluszeichen und dem Imaginärteil
steht; ``complex()`` löst sonst einen ``ValueError`` aus.


.. index:: delattr()
.. _delattr():

delattr()
^^^^^^^^^

Die Funktion ``delattr()``


.. index:: dict()
.. _dict():

dict()
^^^^^^

Die Funktion ``dict()``

.. index:: dir()
.. _dir():

dir()
^^^^^

Die Funktion ``dir()``


.. index:: divmod()
.. _divmod():

divmod()
^^^^^^^^

Die Funktion ``divmod()``

.. index:: enumerate()
.. _enumerate():

enumerate()
^^^^^^^^^^^

Die Funktion ``enumerate()``

.. index:: eval()
.. _eval():

eval()
^^^^^^

Die Funktion ``eval()`` erstellt aus einer Zeichenkette den entsprechenden
Python-Ausdruck; beispielsweise liefert ``eval('myvar')`` gerade die Variable
``myvar`` als Ergebnis.

.. index:: exec()
.. _exec():

exec()
^^^^^^

Die Funktion ``exec()`` führt einen (beispielsweise mittels ``eval()``
konstruierten) Python-Ausdruck aus.

.. index:: filter()
.. _filter():

filter()
^^^^^^^^

Die Funktion ``filter(funktionsname, objekt)`` bietet die Möglichkeit, eine
Filter-Funktion auf alle Elemente eines iterierbaren Objekts (beispielsweise
einer Liste) anzuwenden. Als Ergebnis gibt die ``filter()``-Funktion ein
iterierbares Objekt zurück. Dieses kann beispielsweise für eine ``for``-Schleife
genutzt oder mittels ``list()`` in eine neue Liste umgewandelt werden.

*Beispiel:*

.. code-block:: python

  my_list = [1,2,3,4,5,6,7,8,9]

  even_numbers = filter(lambda x: x % 2 == 0, my_list)

  list(even_numbers)
  # Ergebnis: [2,4,6,8]

Oftmals kann anstelle der ``filter()``-Funktion allerdings auch eine (meist
besser lesbare) :ref:`List-Comprehension <List-Comprehensions>` genutzt werden.
Im obigen Beispiel könnte auch kürzer ``even_numbers = [x for x in my_list if x
% 2 == 0]`` geschrieben werden.



.. index:: float()
.. _float():

float()
^^^^^^^

Die Funktion ``float()`` gibt, sofern möglich, die zur angegebenen Zeichenkette
oder Zahl passende Gleitkomma-Zahl als Ergebnis zurück; wird eine ``int``-Zahl
als Argument übergeben, so wird die Nachkommastelle ``.0`` ergänzt.


.. index:: format()
.. _format():

format()
^^^^^^^^

Die Funktion ``format()`` formattiert Zahlen und Zeichenketten.

.. index:: frozenset()
.. _frozenset():

frozenset()
^^^^^^^^^^^

Die Funktion ``frozenset()``

.. index:: getattr()
.. _getattr():

getattr()
^^^^^^^^^

Die Funktion ``getattr()``

.. index:: globals()
.. _globals():

globals()
^^^^^^^^^

Die Funktion ``globals()`` liefert als Ergebnis ein ``dict`` mit den
Namen und den Werten aller zum Zeitpunkt des Aufrufs existierenden
globalen, das heißt programmweit sichtbaren Variablen.

.. index:: hasattr()
.. _hasattr():

hasattr()
^^^^^^^^^

Die Funktion ``hasattr()``

.. index:: hash()
.. _hash():

hash()
^^^^^^

Die Funktion ``hash()``

.. index:: help()
.. _help():

help()
^^^^^^

Die Funktion ``help()``

.. index:: hex()
.. _hex():

hex()
^^^^^

Die Funktion ``hex()`` gibt eine Zeichenkette mit der Hexadezimaldarstellung
einer Integer-Zahl als Ergebnis zurück. Eine solche Zeichenkette wird mit ``0x``
eingeleitet, gefolgt von der eigentlichen Binärzahl; beispielsweise ergibt
``hex(42)`` die Zeichenkette ``'0x2a'``.


.. index:: id()
.. _id():

id()
^^^^

Die Funktion ``id()``

.. index:: input()
.. _input():

input()
^^^^^^^

Die Funktion ``input()`` dient zum Einlesen einer vom Benutzer eingegebenen
Zeichenkette. Beim Aufruf kann dabei optional ein String angegeben werden, der
dem Benutzer vor dem Eingabe-Prompt angezeigt wird:

.. code-block:: python

    answer = input("Bitte geben Sie Ihren Namen an: ")

    print("Ihr Name ist %s." % answer)

Soll eine Zahl eingelesen werden, so muss die Benutzerantwort mittels
``int()`` bzw. ``float()`` explizit von einem String in eine solche
umgewandelt werden.


.. index:: int()
.. _int():

int()
^^^^^

Die Funktion ``int()`` gibt, sofern möglich, die zur angegebenen Zeichenkette
oder Gleitkomma-Zahl passende Integer-Zahl als Ergebnis zurück; wird eine
``float``-Zahl als Argument übergeben, so werden mögliche Nachkommastellen
schlichtweg ignoriert, beispielsweise ergibt ``int(3.7)`` den Wert ``3``.


.. index:: isinstance()
.. _isinstance():

isinstance()
^^^^^^^^^^^^

Die Funktion ``isinstance()``

.. index:: issubclass()
.. _issubclass():

issubclass()
^^^^^^^^^^^^

Die Funktion ``issubclass()``

.. index:: iter()
.. _iter():

iter()
^^^^^^

Die Funktion ``iter()``

.. index:: len()
.. _len():

len()
^^^^^

Die Funktion ``len()`` gibt die Länge einer Liste oder Zeichenkette als
``int``-Wert an. Bei einer Liste wird die Anzahl an Elementen gezählt, bei einer
Zeichenkette die einzelnen Textzeichen, aus denen die Zeichenkette besteht.


.. index:: list()
.. _list():

list()
^^^^^^

Die Funktion ``list()``

.. index:: locals()
.. _locals():

locals()
^^^^^^^^

Die Funktion ``locals()`` liefert als Ergebnis ein ``dict`` mit den
Namen und den Werten aller zum Zeitpunkt des Aufrufs existierenden
lokalen, das heißt im aktuellen Codeblock sichtbaren Variablen.


.. index:: map()
.. _map():

map()
^^^^^

Die Funktion ``map(function, object)`` wendet eine Funktion auf alle Elemente
eines iterierbaren Objekts (beispielsweise einer Liste) an. Als Ergebnis liefert
``map()`` ein neues iterierbares Objekt, dessen Elemente den einzelnen
Ergebniswerten entsprechen.

*Beispiel:*

.. code-block:: python

    my_list = [3, 5, -10.2, -7, 4.5]
    map(abs, my_list)
    # Ergebnis: [3, 5, 10.2, 7, 4.5]

Oftmals wird anstelle der ``map()``-Funktion eine (meist besser lesbare)
:ref:`List-Comprehension <List-Comprehensions>` genutzt. Im obigen Beispiel
könnte auch ``[abs(x) for x in my_list]`` geschrieben werden.

.. index:: max()
.. _max():

max()
^^^^^

Die Funktion ``max()`` gibt das größte Element einer Liste als Ergebnis zurück.

.. index:: min()
.. _min():

min()
^^^^^

Die Funktion ``min()`` gibt das kleinste Element einer Liste als Ergebnis zurück.

.. index:: next()
.. _next():

next()
^^^^^^

Die Funktion ``next()``

.. index:: object()
.. _object():

object()
^^^^^^^^

Die Funktion ``object()``

.. index:: oct()
.. _oct():

oct()
^^^^^

Die Funktion ``oct()`` gibt eine Zeichenkette mit der Oktaldarstellung einer
``int``-Zahl als Ergebnis zurück. Eine solche Zeichenkette wird mit ``0o``
eingeleitet, gefolgt von der eigentlichen Binärzahl; beispielsweise ergibt
``oct(42)`` die Zeichenkette ``'0o52'``.


.. index:: open()
.. _open():

open()
^^^^^^

Die Funktion ``open()``

.. index:: ord()
.. _ord():

ord()
^^^^^

Die Funktion ``ord()``

.. index:: pow()
.. _pow():

pow()
^^^^^

Die Funktion ``pow()``

.. index:: print()
.. _print():

print()
^^^^^^^

Die Funktion ``print()``

.. index:: property()
.. _property():

property()
^^^^^^^^^^

Die Funktion ``property()``

.. index:: range()
.. _range():

range()
^^^^^^^

Die Funktion ``range()`` erzeugt eine Sequenz ganzzahliger Werte. Sie kann
wahlweise in folgenden Formen benutzt werden:

.. code-block:: python

    range(stop)
    range(start, stop)
    range(start, stop, step)

Wird der ``range()``-Funktion nur ein einziger Wert :math:`n` als Argument
übergeben, so wird eine Zahlensequenz von :math:`0` bis :math:`n-1` generiert;
Werden zwei Werte :math:`m` und :math:`n` übergeben, so wird eine Zahlensequenz
von :math:`m` bis :math:`n-1` erzeugt. Allgemein ist bei Verwendung von
``range()`` die untere Schranke im Zahlenbereich enthalten, die obere hingegen
nicht.

Wird eine dritte Zahl :math:`i \ne 0`  als Argument angegeben, so wird nur jede
:math:`i`-te Zahl im angegebenen Zahlenbereich in die Sequenz aufgenommen. Ist
der Startwert des Zahlenbereichs größer als der Stopwert und :math:`i` negativ,
so wird eine absteigende Zahlensequenz generiert.


.. index:: repr()
.. _repr():

repr()
^^^^^^

Die Funktion ``repr()``

.. index:: reversed()
.. _reversed():

reversed()
^^^^^^^^^^

Die Funktion ``reversed()`` kann auf eine interierbares Objekt (beispielsweise
eine Liste) angewendet werden und gibt dieses in umgekehrter Reihenfolge zurück.

*Beispiel*

.. code-block:: python

    sorted([1,5,2,3])
    # Ergebnis: [5, 3, 2, 1]

.. index:: round()
.. _round():

round()
^^^^^^^

Die Funktion ``round()`` rundet eine ``float``-Zahl auf die nächste ``int``-Zahl
auf beziehungsweise ab und gibt diese als Ergebnis zurück.

.. index:: set()
.. _set():

set()
^^^^^

Die Funktion ``set()`` erzeugt ein neues :ref:`set <Mengen>`-Objekt, also eine
Menge.

.. index:: setattr()
.. _setattr():

setattr()
^^^^^^^^^

Die Funktion ``setattr()``

.. index:: slice()
.. _slice():

slice()
^^^^^^^

Die Funktion ``slice()``

.. index:: sorted()
.. _sorted():

sorted()
^^^^^^^^

Die Funktion ``sorted()`` kann auf eine iterierbares Objekt (beispielsweise
eine Liste) angewendet werden und gibt dieses in sortierter Reihenfolge zurück.

*Beispiel*

.. code-block:: python

    sorted([1,5,2,3])
    # Ergebnis: [1, 2, 3, 5]

.. index:: staticmethod()
.. _staticmethod():

staticmethod()
^^^^^^^^^^^^^^

Die Funktion staticmethod()

.. index:: str()
.. _str():

str()
^^^^^

Die Funktion ``str()``

.. index:: sum()
.. _sum():

sum()
^^^^^

Die Funktion ``sum()`` gibt die Summe eines iterierbaren Objekts als Ergebnis
zurück.

.. index:: super()
.. _super():

super()
^^^^^^^

Die Funktion ``super()``

.. index:: tuple()
.. _tuple():

tuple()
^^^^^^^

Die Funktion ``tuple()``

.. index:: type()
.. _type():

type()
^^^^^^

Die Funktion ``type()``

.. index:: vars()
.. _vars():

vars()
^^^^^^

Die Funktion ``vars()``

.. index:: zip()
.. _zip():

zip()
^^^^^

Die Funktion ``zip()`` verbindet -- ähnlich wie ein Reißverschluss -- Elemente
aus verschiedenen iterierbaren Objekten (beispielsweise Listen) zu einem neuen
iterierbaren Objekt, dessen Elemente Zusammensetzungen der Ausgangselemente
sind.


.. _Standard-Module:
.. _Wichtige Standard-Module:

Wichtige Standard-Module
------------------------


.. _timeit:

``timeit`` -- Laufzeitanalyse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mittels des Pakets ``timeit`` und der gleichnamigen Funktion aus diesem Paket
kann einfach ermittelt werden, wieviel Zeit eine Funktion für einen Aufruf
benötigt:

.. code-block:: python

    import timeit

    timeit.timeit("x = 2 ** 2")
    # Ergebnis: 0.02761734207160771

.. _cProfile:

``cProfile`` -- Profiler
^^^^^^^^^^^^^^^^^^^^^^^^

Mittels des Pakets ``cProfile`` und der darin definierten Funktion ``run()``
kann ermittelt werden, wieviel Zeit für einen Aufruf einer Funktion benötigt
wird. Bei einer Funktion, die weitere Unterfunktionen aufruft, wird zudem
angezeigt, wie viel Zeit auf die einzelnen Schritte entfällt:

.. code-block:: python

    import cProfile
    cProfile.run('sum( range(10000000) )') 

    # Ergebnis:
    # 4 function calls in 0.321 seconds

    # Ordered by: standard name

    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #     1    0.000    0.000    0.321    0.321 <string>:1(<module>)
    #     1    0.000    0.000    0.321    0.321 {built-in method exec}
    #     1    0.321    0.321    0.321    0.321 {built-in method sum}
    #     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Mit dem Profiler können in verschachtelten Funktionen schnell "Bottlenecks"
gefunden werden, also Programmteile, die sehr rechenintensiv sind und daher
bevorzugt optimiert werden sollten.






















.. index:: ASCII-Codes
.. _ASCII-Codes:

ASCII-Codes
-----------

.. _tab-ascii:

+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| Dez | ASCII   | Dez | ASCII   | Dez | ASCII  | Dez | ASCII | Dez | ASCII | Dez | ASCII | Dez | ASCII | Dez | ASCII   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 0   | ``NUL`` | 16  | ``DLE`` | 32  | ``SP`` | 48  | ``0`` | 64  | ``@`` | 80  | ``P`` | 96  |  \`   | 112 | ``p``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 1   | ``SOH`` | 17  | ``DC1`` | 33  | ``!``  | 49  | ``1`` | 65  | ``A`` | 81  | ``Q`` | 97  | ``a`` | 113 | ``q``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 2   | ``STX`` | 18  | ``DC2`` | 34  | ``"``  | 50  | ``2`` | 66  | ``B`` | 82  | ``R`` | 98  | ``b`` | 114 | ``r``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 3   | ``ETX`` | 19  | ``DC3`` | 35  | ``#``  | 51  | ``3`` | 67  | ``C`` | 83  | ``S`` | 99  | ``c`` | 115 | ``s``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 4   | ``EOT`` | 20  | ``DC4`` | 36  | ``$``  | 52  | ``4`` | 68  | ``D`` | 84  | ``T`` | 100 | ``d`` | 116 | ``t``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 5   | ``ENQ`` | 21  | ``NAK`` | 37  | ``%``  | 53  | ``5`` | 69  | ``E`` | 85  | ``U`` | 101 | ``e`` | 117 | ``u``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 6   | ``ACK`` | 22  | ``SYN`` | 38  | ``&``  | 54  | ``6`` | 70  | ``F`` | 86  | ``V`` | 102 | ``f`` | 118 | ``v``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 7   | ``BEL`` | 23  | ``ETB`` | 39  | ``'``  | 55  | ``7`` | 71  | ``G`` | 87  | ``W`` | 103 | ``g`` | 119 | ``w``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 8   | ``BS``  | 24  | ``CAN`` | 40  | ``(``  | 56  | ``8`` | 72  | ``H`` | 88  | ``X`` | 104 | ``h`` | 120 | ``x``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 9   | ``HT``  | 25  | ``EM``  | 41  | ``)``  | 57  | ``9`` | 73  | ``I`` | 89  | ``Y`` | 105 | ``i`` | 121 | ``y``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 10  | ``LF``  | 26  | ``SUB`` | 42  | ``*``  | 58  | ``:`` | 74  | ``J`` | 90  | ``Z`` | 106 | ``j`` | 122 | ``z``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 11  | ``VT``  | 27  | ``ESC`` | 43  | ``+``  | 59  | ``;`` | 75  | ``K`` | 91  | ``[`` | 107 | ``k`` | 123 | ``{``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 12  | ``FF``  | 28  | ``FS``  | 44  | ``,``  | 60  | ``<`` | 76  | ``L`` | 92  | ``\`` | 108 | ``l`` | 124 | ``|``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 13  | ``CR``  | 29  | ``GS``  | 45  | ``-``  | 61  | ``=`` | 77  | ``M`` | 93  | ``]`` | 109 | ``m`` | 125 | ``}``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 14  | ``SO``  | 30  | ``RS``  | 46  | ``.``  | 62  | ``>`` | 78  | ``N`` | 94  | ``^`` | 110 | ``n`` | 126 | ``~``   |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+
| 15  | ``SI``  | 31  | ``US``  | 47  | ``/``  | 63  | ``?`` | 79  | ``O`` | 95  | ``_`` | 111 | ``o`` | 127 | ``DEL`` |
+-----+---------+-----+---------+-----+--------+-----+-------+-----+-------+-----+-------+-----+-------+-----+---------+

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Siehe auch: https://docs.python.org/3/library/functions.html

