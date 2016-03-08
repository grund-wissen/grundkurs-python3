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

Die in der obigen Tabelle angegebenen Wörter können nicht als Variablen- oder
Funktionsnamen verwendet werden. Mittels der Funktion ``iskeyword()`` aus dem
Modul ``keyword`` kann getestet werden, ob eine Zeichenkette ein Schlüsselwort
ist:

.. code-block:: python

    from keyword import iskeyword()

    iskeyword("lambda")
    # Ergebnis: True


.. _Standardfunktionen:

Standardfunktionen
------------------

Die im folgenden Abschnitt beschriebenen Funktionen (`Builtin
<https://docs.python.org/3/library/functions.html>`__-Funktionen) sind
standardmäßig in Python definiert, ohne dass ein zusätzliches Modul geladen
werden muss.

.. index:: abs()
.. _abs():

abs()
^^^^^

Die Funktion `abs(x) <https://docs.python.org/3/library/functions.html#abs>`__
gibt den Absolutwert einer Zahl ``x`` als Ergebnis zurück.

*Beispiel:*

.. code-block:: python

    abs( -5.7 )
    # Ergebnis: 5.7

    abs( +5.7 )
    # Ergebnis: 5.7


.. index:: all()
.. _all():

all()
^^^^^

Die Funktion `all(sequenz)
<https://docs.python.org/3/library/functions.html#all>`__ kann auf ein
beliebiges iterierbares Objekt (Listen oder Mengen) angewendet werden. Als
Ergebnis wird ``True`` zurückgegeben, wenn alle Elemente den Wahrheitswert
``True`` besitzen; andernfalls wird ``False`` als Ergebnis zurückgegeben.

*Beispiel:*

.. code-block:: python

    all( [1,3,5,0,7] )
    # Ergebnis: False

    all( [3,7,9,5,2] )
    # Ergebnis: True

.. index:: any()
.. _any():

any()
^^^^^

Die Funktion `any(sequenz)
<https://docs.python.org/3/library/functions.html#any>`__ kann auf ein
beliebiges iterierbares Objekt (Listen oder Mengen) angewendet werden. Als
Ergebnis wird ``True`` zurückgegeben, wenn zumindest ein Element den
Wahrheitswert ``True`` besitzt; andernfalls wird ``False`` als Ergebnis
zurückgegeben.

*Beispiel:*

.. code-block:: python

    any( [0,0,0,0,0] )
    # Ergebnis: False

    any( [0,0,0,1,0] )
    # Ergebnis: True


.. index:: ascii()
.. _ascii():

ascii()
^^^^^^^

Die Funktion `ascii(objekt) <https://docs.python.org/3/library/functions.html#ascii>`__
gibt ebenso wie die Funktion :ref:`repr() <repr()>` als Ergebnis eine
Zeichenkette zurück, die eine kurze charakteristische Beschreibung des Objekts
beinhaltet; häufig entspricht dies einer Angabe der Objekt-Klasse, des
Objekt-Namens und der Speicheradresse.

*Beispiel:*

.. code-block:: python

    ascii(print)
    # Ergebnis: '<built-in function print>'

Ist in der Klasse des angegebenen Objekts eine ``__repr__()``-Methode definiert,
so ist ``repr(objekt)`` identisch mit ``objekt.__repr__()``. Als Zeichensatz
wird für die Ausgabe des Strings allerdings der ASCII-Zeichensatz verwendet, so
dass darin nicht enthaltene Symbole durch Zeichen mit vorangestelltem ``\x``,
``\u`` oder ``\U`` gekennzeichnet werden.


.. index:: bin()
.. _bin():

bin()
^^^^^

Die Funktion `bin(x) <https://docs.python.org/3/library/functions.html#bin>`__
gibt eine Zeichenkette mit der Binärdarstellung einer einer Integer-Zahl als
Ergebnis zurück. Eine solche Zeichenkette wird mit ``0b`` eingeleitet, gefolgt
von der eigentlichen Binärzahl.

*Beispiel:*

.. code-block:: python

    bin(42)
    # Ergebnis: '0b101010'

.. index:: bool()
.. _bool():

bool()
^^^^^^

Die Funktion `bool(ausdruck)
<https://docs.python.org/3/library/functions.html#bool>`__ gibt den
Wahrheitswert eines logischen Ausdrucks an; dieser kann entweder ``True`` oder
``False`` sein. Als Argument kann entweder ein mittels :ref`Vergleichsoperatoren
<Operatoren>` erzeugter logischer Ausdruck oder auch ein einzelnes Objekt
übergeben werden.

* Listen, Tupel und Zeichenketten haben den Wahrheitswert ``True``, wenn sie
  nicht leer sind beziehungsweise mindestens ein Zeichen enthalten.
* Zahlen haben dann den Wahrheitswert ``True``, wenn sie nicht gleich Null sind.
* ``bool(None)`` liefert den Wahrheitswert ``False``.

*Beispiel:*

.. code-block:: python

    bool(-3)
    # Ergebnis: True


.. index:: bytearray()
.. _bytearray():

bytearray()
^^^^^^^^^^^

Die Funktion `bytearray(string, encoding)
<https://docs.python.org/3/library/functions.html#bytearray>`__ erzeugt aus der
angegebenen Zeichenkette eine neue Instanz eines ``bytearray``-Objekts; als
Encoding kann beispielsweise ``'utf-8'`` oder ``'ascii'`` angegeben werden.
Dieser Datentyp besteht aus ganzzahligen Werten zwischen ``0`` und ``255`` und
ist -- ähnlich wie der Datentyp ``str`` zur Speicherung von Zeichenketten in
Textdateien vorgesehen ist -- zur Speicherung von binären Daten gedacht.

*Beispiel:*

.. code-block:: python

    bytearray("Hallo Welt!", 'utf-8')
    # Ergebnis: bytearray(b'Hallo Welt!')

Die für ``bytes`` und ``bytearrays`` verfügbaren Methoden entsprechen im
Wesentlichen den jeweiligen Methoden für Zeichenketten (siehe Abschnitt `Bytes
and Bytearray Operations
<https://docs.python.org/3/library/stdtypes.html#bytes-and-bytearray-operations>`__
der offiziellen Python-Dokumentation).

.. index:: bytes()
.. _bytes():

bytes()
^^^^^^^

Die Funktion `bytes(string, encoding)
<https://docs.python.org/3/library/functions.html#bytes>`__ erzeugt aus der
angegebenen Zeichenkette eine neue Instanz eines ``bytes``-Objekts; als Encoding
kann beispielsweise ``'utf-8'`` oder ``'ascii'`` angegeben werden. Das
``bytes``-Objekt entspricht im Wesentlichen einem :ref:`bytearray
<bytearray()>`-Objekt, ist aber nicht veränderlich (so wie ein :ref:`Tupel
<Tupel>` eine unveränderliche :ref:`Liste <Liste>` darstellt).

*Beispiel:*

.. code-block:: python

    bytes("Hallo Welt!", 'utf-8')
    # Ergebnis: b'Hallo Welt!'

.. index:: callable()
.. _callable():

callable()
^^^^^^^^^^

Die Funktion `callable(objekt)
<https://docs.python.org/3/library/functions.html#callable>`__ gibt in Form
eines booleschen Wahrheitswertes an, ob das als Argument übergebene Objekt (wie
eine Funktion oder Methode) aufrufbar ist oder nicht.

*Beispiel:*

.. code-block:: python

    callable(5)
    # Ergebnis: False

    callable(print)
    # Ergebnis: True


.. index:: chr()
.. _chr():

chr()
^^^^^

Die Funktion `chr(zahl)
<https://docs.python.org/3/library/functions.html#chr>`__ gibt zu einem
angegebenen Ganzzahl-Wert mit positivem Vorzeichen das entsprechende
Unicode-Zeichen aus.

*Beispiel:*

.. code-block:: python

    chr(65)
    # Ergebnis: 'A'

    chr(97)
    # Ergebnis: 'a'

Für viele Programme reichen die `ASCII-Codes`_ als Teilmenge des
Unicode-Zeichensatzes bereits aus.


.. index:: classmethod()
.. _classmethod():

classmethod()
^^^^^^^^^^^^^

Die Funktion `classmethod(methode)
<https://docs.python.org/3/library/functions.html#classmethod>`__ macht die
angegebene Methode zu einer so genannten Klassen-Methode. Üblicherweise wird die
``classmethod()``-Funktion als :ref:`Funktionsdekorator <Dekorator>` verwendet:

.. code-block:: python

    class C():

        @classmethod
        def my_class_method(cls, arguments):

            pass

Bei einer so definierten Methode wird die als erstes Argument der Name der
Klasse angegeben, von der aus die Methode aufgerufen wird. Die Klassen-Methode
des obigen Beispiels kann dann wahlweise mittels ``C.my_class_method()`` oder
ausgehend von einer Instanz der Klasse, also mittels ``C().my_class_method()``
aufgerufen werden; im letzteren Fall wird beim Aufruf nur der Name der
Instanzklasse, nicht die Instanz selbst als erstes Argument an die Methode
übergeben.

Wird eine Klassen-Methode von einer Instanz einer Klasse aufgerufen, welche die
Methode lediglich über eine :ref:`Vererbung <Vererbung>` erhalten hat, so wird
beim Aufruf dennoch der Name der konkreten Instanzklasse (und nicht der
Basis-Klasse) übergeben.

.. index:: compile()
.. _compile():

compile()
^^^^^^^^^

Die Funktion `compile(code, file, mode)
<https://docs.python.org/3/library/functions.html#compile>`__ übersetzt den als
erstes Argument angegebenen Code-String in ein ausführbares, in Maschinensprache
geschriebenes Bytecode-Objekt. Als zweites Argument muss der Pfad einer Datei
angegeben werden, in die gegebenenfalls auftretende Fehler geschrieben werden
sollen. Als drittes Argument muss entweder zum Kompilieren genutzte Modus
angegeben werden:

* ``single``, wenn es sich bei dem angegebenen Code um eine einzelne
  Aussage-Komponente (beispielsweise den Wert einer Variablen) handelt;
* ``eval``, wenn der angegebene Code eine einzelne Aussage darstellt;
* ``exec``, wenn der angegebene Code aus einer oder mehreren Aussagen besteht
  und als Ergebnis ``None`` liefern soll.

Der compilierte Bytecode kann anschließend mittels :ref:`eval() <eval()>`
beziehungsweise :ref:`exec() <exec()>` ausgeführt werden.

*Beispiel:*

.. code-block:: python

    # Bytecode erzeugen:

    a = 5

    compile('a', 'tmp.txt', 'single')
    # Ergebnis: <code object <module> at 0x7f38edc91f60, file "tmp.txt", line 1>

    compile('print("Hallo Welt!")', 'tmp.txt', 'eval')
    # Ergebnis: <code object <module> at 0x7f38edc91c00, file "tmp.txt", line 1>

    compile('for i in range(3): print(i)', 'tmp.txt', 'exec')
    # Ergebnis: <code object <module> at 0x7f38edc94780, file "tmp.txt", line 1>

    # Bytecode ausführen:

    eval( compile('a', 'tmp.txt', 'single') )
    # Rückgabewert / Ergebnis: 5

    eval( compile('print("Hallo Welt!")', 'tmp.txt', 'eval') )
    # Rückgabewert / Ergebnis: Hallo Welt!

    exec( compile('for i in range(3): print(i)', 'tmp.txt', 'exec') )
    # Rückgabewert: None
    # Ergebnis (auf dem Bildschirm):
    # 0
    # 1
    # 2


.. index:: complex()
.. _complex():

complex()
^^^^^^^^^

Die Funktion `complex()
<https://docs.python.org/3/library/functions.html#complex>`__ erstellt eine neue
Instanz einer :ref:`komplexen Zahl <Komplexe Zahlen>`  aus zwei angegebenen
Zahlen oder einem angegebenen String.

*Beispiel:*

.. code-block:: python

    complex(1.5, 2)
    # Ergebnis: (1.5+2j)

Wird ein String als Argument angegeben, so muss darauf geachtet werden, dass
kein Leerzeichen zwischen dem Realteil, dem Pluszeichen und dem Imaginärteil
steht; ``complex()`` löst sonst einen ``ValueError`` aus.


.. index:: delattr()
.. _delattr():

delattr()
^^^^^^^^^

Die Funktion `delattr(objekt, attributname)
<https://docs.python.org/3/library/functions.html#delattr>`__ löscht ein
angegebenes Attribut beziehungsweise einen angegebenen Funktionsnamen (eine
Zeichenkette) aus dem als erstes Argument angegebenen Objekt; dies ist formal
identisch mit ``del objekt.attributname``.

.. code-block:: python

    import math as m

    # Attribut löschen:
    delattr(m, 'cos')

    # Test:
    m.cos( m.pi/4 )
    # Ergebnis: 'module' object has no attribute 'cos'


.. index:: dict()
.. _dict():

dict()
^^^^^^

Die Funktion `dict()
<https://docs.python.org/3/library/functions.html#func-dict>`__ erzeugt eine
neue Instanz eines :ref:`dict <dict>`-Objekts, also ein Dictionary. Formal ist
``d = dict()`` somit identisch mit ``d = {}``.

*Beispiel:*

.. code-block:: python

    # Neues dict erzeugen:
    d = dict()

    # Schlüssel-Wert-Paar hinzufügen:
    d['test'] = 'Hallo Welt!'

    d
    # Ergebnis: {'test': 'Hallo Welt!'}


.. index:: dir()
.. _dir():

dir()
^^^^^

Die Funktion `dir() <https://docs.python.org/3/library/functions.html#dir>`__
gibt, wenn sie ohne ein angegebenes Argument aufgerufen wird, eine Liste mit den
Namen aller in der aktuellen Python-Sitzung definierten Objekt-Namen (als
Strings) zurück.

Wird als Argument ein beliebiges Objekt angegeben, so werden die Attribute und
Methoden des jeweiligen Objekts in Form einer String-Liste ausgegeben.

*Beispiel:*

.. code-block:: python

    import math as m

    dir(m)
    # Ergebnis:
    # ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos',
    # 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign',
    # 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial',
    # 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isfinite', 'isinf',
    # 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'pi',
    # 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']


.. index:: divmod()
.. _divmod():

divmod()
^^^^^^^^

Die Funktion `divmod(zahl1, zahl2)
<https://docs.python.org/3/library/functions.html#divmod>`__ dividiert die als
erstes Argument angegebene Zahl durch die zweite Zahl. Als Ergebnis gibt die
Funktion ein Tupel zweier Werte zurück, wobei der erste Wert das ganzzahlige
Ergebnis der Division und der zweite Wert den Divisionsrest angibt.

*Beispiel:*

.. code-block:: python

    divmod(14,5)
    # Ergebnis: (2, 4)


.. index:: enumerate()
.. _enumerate():

enumerate()
^^^^^^^^^^^

Die Funktion `enumerate(sequenz)
<https://docs.python.org/3/library/functions.html#enumerate>`__ ermöglicht es,
die Einträge einer Liste oder eines Tupels zu nummerieren. Damit lassen sich
beispielsweise ``for``-Schleifen über die Elemente einer Liste konstruieren, in
denen beide Informationen verwendet werden.

*Beispiel:*

.. code-block:: python

    liste = [5, 6, 7, 8, 9]

    for i, num in enumerate(liste):
        print( "Der {}. Eintrag in der Liste ist {}".format(i, num) )

    # Ergebnis:
    # Der 0. Eintrag in der Liste ist 5
    # Der 1. Eintrag in der Liste ist 6
    # Der 2. Eintrag in der Liste ist 7
    # Der 3. Eintrag in der Liste ist 8
    # Der 4. Eintrag in der Liste ist 9


.. index:: eval()
.. _eval():

eval()
^^^^^^

Die Funktion `eval(zeichenkette)
<https://docs.python.org/3/library/functions.html#eval>`__ erstellt aus der
angegebenen Zeichenkette den entsprechenden Python-Ausdruck und wertet diesen
aus; es darf sich dabei allerdings nur um einen einzelnen Ausdruck, nicht um ein
aus vielen einzelnen Aussagen zusammengesetztes Code-Stück handeln.

Der Rückgabewert von ``eval()`` entspricht dabei dem Ergebnis des ausgewerteten
Ausdrucks.

*Beispiel:*

.. code-block:: python

    x = 1

    eval('x+1')
    # Rückgabewert / Ergebnis: 2

    eval('for i in range(3): print(i)')
    # Ergebnis:
    # for i in range(3): print(i)
    #  ^
    # SyntaxError: invalid syntax


Die Funktion ``eval()`` kann ebenso verwendet werden, um einen mittels
``compile()`` erzeugten Ausdruck auszuwerten. Wurde als Compilier-Modus hierbei
``'single'`` oder ``eval`` angegeben, so entspricht der Rückgabewert wiederum
dem Ergebnis des Ausdrucks; bei der Angabe von ``exec()`` als Compilier-Modus
liefert ``eval()`` als Ergebnis stets den Wert ``None``.


.. index:: exec()
.. _exec():

exec()
^^^^^^

Die Funktion `exec(zeichenkette)
<https://docs.python.org/3/library/functions.html#exec>`__ führt -- ähnlich wie
``eval()`` -- einen (beispielsweise mittels :ref:`compile() <compile()>`
konstruierten) Python-Ausdruck aus; es kann sich dabei auch um eine beliebig
lange Zusammensetzung einzelner Python-Ausdrücke handeln. Als Ergebnis wird
stets ``None`` zurückgegeben.

*Beispiel:*

.. code-block:: python

    exec('print("Hallo Welt!")')
    # Rückgabewert: None
    # Ergebnis (Auf dem Bildschirm):
    # Hallo Welt!

    exec('for i in range(3): print(i)')
    # Rückgabewert: None
    # Ergebnis (Auf dem Bildschirm):
    # 0
    # 1
    # 2

    exec('42')
    # Rückgabewert / Ergebnis: None

Die Funktion ``exec()`` kann ebenso verwendet werden, um einen mittels
``compile()`` erzeugten Ausdruck auszuwerten; auch hierbei ist der Rückgabewert
stets ``None``.


.. index:: filter()
.. _filter():

filter()
^^^^^^^^

Die Funktion `filter(funktionsname, objekt)
<https://docs.python.org/3/library/functions.html#filter>`__ bietet die
Möglichkeit, eine Filter-Funktion auf alle Elemente eines iterierbaren Objekts
(beispielsweise einer Liste) anzuwenden. Als Ergebnis gibt die
``filter()``-Funktion ein iterierbares Objekt zurück. Dieses kann beispielsweise
für eine ``for``-Schleife genutzt oder mittels ``list()`` in eine neue Liste
umgewandelt werden.

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

Die Funktion `float()
<https://docs.python.org/3/library/functions.html#float>`__ gibt, sofern
möglich, die zur angegebenen Zeichenkette oder Zahl passende Gleitkomma-Zahl als
Ergebnis zurück; wird eine ``int``-Zahl als Argument übergeben, so wird die
Nachkommastelle ``.0`` ergänzt.

*Beispiel:*

.. code-block:: python

    float(5)
    # Ergebnis: 5.0

    float('3.2')
    # Ergebnis: 3.2

    float('1e3')
    # Ergebnis: 1000.0


.. index:: format()
.. _format():

format()
^^^^^^^^

Die Funktion `format(wert, formatangabe)
<https://docs.python.org/3/library/functions.html#format>`__ formatiert die
Ausgabe des angegebenen Werts. Hierzu können als Format-Angabe die für die
:ref:`Formatierung von Zeichenketten <Formatierung von Zeichenketten>` üblichen
Symbole verwendet werden. Wird kein Format angegeben, so wird die in der
Objektklasse des Werts definierte Funktion ``wertklasse.__format__()``
aufgerufen.

*Beispiel:*

.. code-block:: python

    # Zeichenkette zentriert ausgeben (Gesamtbreite 20):
    format('Hallo Welt!', '^20')
    # Ergebnis: '    Hallo Welt!     '

    # Zeichenkette rechtsbündig ausgeben (Gesamtbreite 20):
    format('Hallo Welt!', '>20')
    # Ergebnis: '         Hallo Welt!'

    # Zahl Pi mit drei Stellen Genauigkeit ausgeben:
    format(m.pi, '.3')
    # Ergebnis: 3.14


.. index:: frozenset()
.. _frozenset():

frozenset()
^^^^^^^^^^^

Die Funktion `frozenset(sequenz)
<https://docs.python.org/3/library/functions.html#func-frozenset>`__ erzeugt aus
der angegebenen Sequenz (beispielsweise einer Liste oder einer Zeichenkette)
eine neue Instanz eines :ref:`frozenset <Mengen>`-Objekts, also eine
unveränderliche Menge.

*Beispiel:*

.. code-block:: python

    frozenset( [1, 3, 5, 7, 9, 9] )
    # Ergebnis: frozenset({1, 3, 5, 7, 9})

    frozenset( "Hallo Welt!" )
    # Ergebnis: frozenset({' ', '!', 'H', 'W', 'a', 'e', 'l', 'o', 't'})


.. index:: getattr()
.. _getattr():

getattr()
^^^^^^^^^

Die Funktion `getattr(objekt, attributname)
<https://docs.python.org/3/library/functions.html#getattr>`__ gibt als Ergebnis
den Wert von ``objekt.attributname`` zurück. Als drittes Argument kann optional
ein Standard-Wert angegeben werden, der als Ergebnis zurück gegeben wird, wenn
das angegebene Attribut nicht existiert.

*Beispiel:*

.. code-block:: python

    # Beispiel-Klasse:
    class Point():

        x = 5
        y = 4

    # Punkt-Objekt erzeugen:
    p = Point()

    getattr(p, 'x')
    # Ergebnis: 5

    getattr(p, 'y')
    # Ergebnis: 4

    getattr(p, 'z', 0)
    # Ergebnis: 0

Wird kein Standard-Wert angegeben und das Attribut existiert nicht, so wird ein
``AttributeError`` ausgelöst.

.. index:: globals()
.. _globals():

globals()
^^^^^^^^^

Die Funktion `globals()
<https://docs.python.org/3/library/functions.html#globals>`__ liefert als
Ergebnis ein ``dict`` mit den Namen und den Werten aller zum Zeitpunkt des
Aufrufs existierenden globalen, das heißt programmweit sichtbaren Variablen.

*Beispiel:*

.. code-block:: python

    globals()
    # Ergebnis:
    # {'__doc__': None, '__spec__': None, '__name__': '__main__',
    # '__package__': None, # '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
    # '__builtins__': <module 'builtins' (built-in)>}


.. index:: hasattr()
.. _hasattr():

hasattr()
^^^^^^^^^

Die Funktion `hasattr(objekt, attributname)
<https://docs.python.org/3/library/functions.html#hasattr>`__ gibt als Ergebnis
den Wahrheitswert ``True`` zurück, falls für das angegebene Objekt ein Attribut
mit dem angegebenen Namen existiert, andernfalls ``False``.

*Beispiel:*

.. code-block:: python

    # Beispiel-Klasse:
    class Point():

        x = 5
        y = 4

    # Punkt-Objekt erzeugen:
    p = Point()

    hasattr(p, 'x')
    # Ergebnis: True

    hasattr(p, 'y')
    # Ergebnis: True

    getattr(p, 'z')
    # Ergebnis: False

Mittels der Funktion ``hasattr()`` kann somit geprüft werden, ob die Funktion
``getattr()`` beim Aufruf einen ``AttributeError`` auslösen wird oder nicht.


.. index:: hash()
.. _hash():

hash()
^^^^^^

Die Funktion `hash(unveraenderliches-objekt)
<https://docs.python.org/3/library/functions.html#hash>`__ liefert zu beliebigen
nicht veränderlichen Python-Objekten (beispielsweise Zeichenketten oder Tupeln)
einen eindeutigen Integer-Wert als Ergebnis zurück; dieser ist nicht abhängig
von der aktuellen Python-Sitzung. Identische Objekte werden durch die
``hash()``-Funktion also auf identische ganzzahlige Werte abgebildet.

*Beispiel:*

.. code-block:: python

    hash("Hallo Welt!")
    # Ergebnis: -2446188496090613429

    hash( (1, 3, 5, 7, 9) )
    # Ergebnis: -4331119994873071480

Die Umkehrung ist leider nicht zwingend eindeutig: Zu einem Hash-Wert können
unterschiedliche Objekte gehören.

.. index:: help()
.. _help():

help()
^^^^^^

Die Funktion `help(objekt)
<https://docs.python.org/3/library/functions.html#help>`__ blendet im
Interpreter eine Hilfe-Seite zum angegebenen Objekt ein, sofern eine
Dokumentation zum angegebenen Objekt vorhanden ist.

*Beispiel:*

.. code-block:: python

    # Hilfe zu Zeichenketten (str) anzeigen:
    help(str)

    # Hilfe zur Funktion print() anzeigen:
    help(str)


.. index:: hex()
.. _hex():

hex()
^^^^^

Die Funktion `hex(int-wert)
<https://docs.python.org/3/library/functions.html#hex>`__ gibt eine Zeichenkette
mit der Hexadezimal-Darstellung einer Integer-Zahl als Ergebnis zurück. Eine
solche Zeichenkette wird mit ``0x`` eingeleitet, gefolgt von der eigentlichen
Binärzahl.

*Beispiel:*

.. code-block:: python

    hex(42)
    # Ergebnis: '0x2a'


.. index:: id()
.. _id():

id()
^^^^

Die Funktion `id(objekt)
<https://docs.python.org/3/library/functions.html#id>`__ liefert für beliebige
Python-Objekte, abhängig von der aktuellen Python-Sitzung, einen eindeutigen
Integer-Wert als Ergebnis zurück; dieser Wert entspricht der Adresse, an der das
Objekt im Speicher abgelegt ist.

*Beispiel:*

.. code-block:: python

    id("Hallo Welt!")
    # Ergebnis: 139882484400688

Mittels der Funktion ``id()`` können somit zwei Objekte auf Gleichheit getestet
werden.


.. index:: input()
.. _input():

input()
^^^^^^^

Die Funktion `input() <https://docs.python.org/3/library/functions.html#input>`__
dient zum Einlesen einer vom Benutzer eingegebenen Zeichenkette. Beim Aufruf
kann dabei optional ein String angegeben werden, der dem Benutzer vor dem
Eingabe-Prompt angezeigt wird:

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

Die Funktion `int() <https://docs.python.org/3/library/functions.html#int>`__
gibt, sofern möglich, die zur angegebenen Zeichenkette oder Gleitkomma-Zahl
passende Integer-Zahl als Ergebnis zurück; wird eine ``float``-Zahl als Argument
übergeben, so werden mögliche Nachkommastellen schlichtweg ignoriert,
beispielsweise ergibt ``int(3.7)`` den Wert ``3``.

*Beispiel:*

.. code-block:: python

    int('5')
    # Ergebnis: 5

    int(3.14)
    # Ergebnis: 3


.. index:: isinstance()
.. _isinstance():

isinstance()
^^^^^^^^^^^^

Die Funktion `isinstance(objekt, klassen-name)
<https://docs.python.org/3/library/functions.html#isinstance>`__ gibt als
Ergebnis den Wahrheitswert ``True`` zurück, wenn das angegebene Objekt eine
Instanz der als zweites Argument angegebenen Klasse (oder einer :ref:`Subklasse
<Vererbung>`) ist; ist dies nicht der Fall, wird ``False`` als Ergebnis
zurückgegeben.

*Beispiel:*

.. code-block:: python

    isinstance("Hallo Welt", str)
    # Ergebnis: True


.. index:: issubclass()
.. _issubclass():

issubclass()
^^^^^^^^^^^^

Die Funktion `issubclass(cls1, cls2)
<https://docs.python.org/3/library/functions.html#issubclass>`__ gibt als
Ergebnis den Wahrheitswert ``True`` zurück, wenn die als erstes Argument
angegebene Klasse eine :ref:`Subklasse <Vererbung>` der als zweites Argument
angegebenen Klasse ist; ist dies nicht der Fall, wird ``False`` als Ergebnis
zurückgegeben.

*Beispiel:*

.. code-block:: python

    isinstance(str, object)
    # Ergebnis: True


.. index:: iter()
.. _iter():

iter()
^^^^^^

Die Funktion `iter(sequenz)
<https://docs.python.org/3/library/functions.html#iter>`__ erstellt eine neue
Instanz eines Iterator-Objekts aus einer listen-artigen Sequenz (genauer: einem
Objekt mit einer ``__iter__()``-Methode). Dieser Iterator kann beispielsweise
verwendet werden, um eine ``for``-Schleife über die in der Sequenz vorkommenden
Elemente zu konstruieren:

*Beispiel:*

.. code-block:: python

    # Iterator generieren:
    iterator = iter( ['Hallo', 'Welt'] )

    # Elemente des Iterator-Objekts ausgeben:
    for i in iterator:
        print(i)

    # Ergebnis:
    # Hallo
    # Welt

Die einzelnen Elemente eines Iterator-Objekts können auch schrittweise mittels
``iteratorname.__next__()`` aufgerufen werden; ist man am Ende der Sequenz
angekommen, so wird ein ``StopIteration``-Error ausgelöst.

Eine zweite Verwendungsmöglichkeit der ``iter()``-Funktion besteht darin, als
erstes Objekt einen Funktions- oder Methodennamen und als zweites Argument eine
Integer-Zahl als "Grenzwert" anzugeben. Wird ein solcher "aufrufbarer" Iterator
mit ``iteratorname.__next__()`` aufgerufen, so wird die angegebene Funktion so
lange aufgerufen, bis diese einen Rückgabewert liefert, der mit dem angegebenen
Grenzwert identisch ist. Wird der Grenzwert nicht erreicht, so kann der Iterator
beliebig oft aufgerufen werden.

*Beispiel:*

.. code-block:: python

    import random

    # Aufrufbaren Iterator generieren:
    iterator = iter( random.random, 1 )

    # Zufallszahlen ausgeben:

    iterator.__next__()
    # Ergebnis: 0.17789467192460118

    iterator.__next__()
    # Ergebnis: 0.7501975823469289


.. index:: len()
.. _len():

len()
^^^^^

Die Funktion `len() <https://docs.python.org/3/library/functions.html#len>`__
gibt die Länge einer Liste oder Zeichenkette als ``int``-Wert an. Bei einer
Liste wird die Anzahl an Elementen gezählt, bei einer Zeichenkette die einzelnen
Textzeichen, aus denen die Zeichenkette besteht.

*Beispiel:*

.. code-block:: python

    len('Hallo Welt!')
    # Ergebnis: 11

    len( str(1000) )
    # Ergebnis: 4

    len( [1,2,3,4,5] )
    # Ergebnis: 5


.. index:: list()
.. _list():

list()
^^^^^^

Die Funktion `list()
<https://docs.python.org/3/library/functions.html#func-list>`__ erzeugt eine
neue Instanz eines :ref:`list <list>`-Objekts, also eine (veränderliche) Liste.
Formal ist ``l = list()`` somit identisch mit ``l = [ ]``.

Wird beim Aufruf von ``list()`` eine Sequenz angegeben, so wird die Liste mit
den in der Sequenz vorkommenden Einträgen gefüllt.

*Beispiel:*

.. code-block:: python

    # Leere Liste erzeugen:
    l1 = list()

    # Liste mit Zahlen 0 bis 9 erzeugen:
    l2 = list( range(10) )

    l2
    # Ergebnis: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


.. index:: locals()
.. _locals():

locals()
^^^^^^^^

Die Funktion `locals()
<https://docs.python.org/3/library/functions.html#locals>`__ liefert als
Ergebnis ein ``dict`` mit den Namen und den Werten aller zum Zeitpunkt des
Aufrufs existierenden lokalen, das heißt im aktuellen Codeblock sichtbaren
Variablen.


.. index:: map()
.. _map():

map()
^^^^^

Die Funktion `map(function, object)
<https://docs.python.org/3/library/functions.html#map>`__ wendet eine Funktion
auf alle Elemente eines iterierbaren Objekts (beispielsweise einer Liste) an.
Als Ergebnis liefert ``map()`` ein neues iterierbares Objekt, dessen Elemente
den einzelnen Ergebniswerten entsprechen.

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

Die Funktion `max() <https://docs.python.org/3/library/functions.html#max>`__
gibt das größte Element einer Liste als Ergebnis zurück.

*Beispiel:*

.. code-block:: python

    max( [5,1,3,9,7] )
    # Ergebnis: 9


.. index:: min()
.. _min():

min()
^^^^^

Die Funktion `min() <https://docs.python.org/3/library/functions.html#min>`__
gibt das kleinste Element einer Liste als Ergebnis zurück.

*Beispiel:*

.. code-block:: python

    min( [5,1,3,9,7] )
    # Ergebnis: 1


.. index:: next()
.. _next():

next()
^^^^^^

Die Funktion ``next(iterator)`` bewirkt einen Aufruf von
``iterator.__next__()``, gibt also das nächste Element der Iterator-Sequenz aus.
Ist der Iterator am Ende der Sequenz angelangt, so wird von ``next(iterator)``
ein ``StopIteration``-Error ausgegeben.

*Beispiel:*

.. code-block:: python

    # Iterator generieren:
    iterator = iter( ['Hallo', 'Welt'] )

    next(iterator)
    # Ergebnis: 'Hallo'

    next(iterator)
    # Ergebnis: 'Welt'

    next(iterator)
    # Ergebnis:
    # ----> 1 next(iterator)
    # StopIteration


.. index:: object()
.. _object():

object()
^^^^^^^^

Die Funktion `object()
<https://docs.python.org/3/library/functions.html#object>`__ erzeugt eine
Instanz eines neuen ``object``-Objekts. Ein ``objekt`` ist die Basisklasse aller
Objekte, hat allerdings keine besonderen Attribute oder Methoden.

Beim Aufruf von ``object()`` dürfen keine weiteren Argumente angegeben werden;
zudem verfügt ein ``object``-Objekt über kein ``__dict__``, so dass der Instanz
keine weiteren Attribute oder Methoden hinzugefügt werden können.

.. index:: oct()
.. _oct():

oct()
^^^^^

Die Funktion `oct(int-wert)
<https://docs.python.org/3/library/functions.html#oct>`__ gibt eine Zeichenkette
mit der Oktaldarstellung einer ``int``-Zahl als Ergebnis zurück. Eine solche
Zeichenkette wird mit ``0o`` eingeleitet, gefolgt von der eigentlichen
Oktalzahl.

*Beispiel:*

.. code-block:: python

    oct(42)
    # Ergebnis: '0o52'


.. index:: open()
.. _open():

open()
^^^^^^

Die Funktion `open(dateiname)
<https://docs.python.org/3/library/functions.html#open>`__ gibt ein zum
angegebenen Pfad passendes Datei-Objekt als Ergebnis zurück, das
zum Lesen oder Schreiben von Dateien verwendet wird.

Die Funktion ``open()`` ist im Abschnitt :ref:`Dateien
<Dateien>` näher beschrieben.


.. index:: ord()
.. _ord():

ord()
^^^^^

Die Funktion `ord(zeichen)
<https://docs.python.org/3/library/functions.html#ord>`__ gibt die Unicode-Zahl
(ein ``int``-Wert) eines angegebenen Zeichens (Buchstabe, Zahl, oder
Sonderzeichen) aus.

*Beispiel:*

.. code-block:: python

    ord('A')
    # Ergebnis: 65

    ord('a')
    # Ergebnis: 97

Für viele Programme reichen die `ASCII-Codes`_ als Teilmenge des
Unicode-Zeichensatzes bereits aus.


.. index:: pow()
.. _pow():

pow()
^^^^^

Die Funktion `pow(zahl1, zahl2)
<https://docs.python.org/3/library/functions.html#pow>`__ gibt beim Aufruf von
``pow(x,y)`` den Wert von ``x ** y``, also ``x`` hoch ``y`` aus (Potenz).

*Beispiel:*

.. code-block:: python

    pow(10, 3)
    # Ergebnis: 1000

    pow(10, -3)
    # Ergebnis: 0.001


.. index:: print()
.. _print():

print()
^^^^^^^

Die Funktion `print(zeichenkette)
<https://docs.python.org/3/library/functions.html#print>`_ gibt die angegebene
Zeichenkette auf dem Bildschirm aus; dabei können unter anderem mittels einer
geeigneten :ref:`Formatierung <Formatierung von Zeichenketten>` auch Werte von
Variablen ausgegeben werden.

*Beispiel:*

.. code-block:: python

    print("Die Antwort lautet %d.", % 42)
    # Ergebnis: Die Antwort lautet 42.


.. index:: property()
.. _property():

property()
^^^^^^^^^^

Die Funktion `property()
<https://docs.python.org/3/library/functions.html#property>`__ wird verwendet,
um auf ein Attribut einer Klasse nicht direkt, sondern mittels einer Methode
zuzugreifen. Hierzu wird in der Klasse des Objekts je eine :ref:`Setter- und
Getter <Property>`-Methode definiert, die zum Zuweisen und Abrufen des Attributs
verwendet werden. Anschließend kann mittels ``my_attribute =
property(fget=getterfunction, fset=setterfunction)`` ein Property-Attribut
erzeugt werden.

"Klassisch" kann die ``property()``-Funktion folgendermaßen verwendet werden:

.. code-block:: python

    # Testklasse definieren:
    class C():

        # Normales Klassen-Attribut anlegen:
        foo = 1

        # Getter-Funktion für 'bar' definieren:
        def get_bar(self):
            return self.foo

        # Setter-Funktion für 'bar' definieren:
        def set_bar(self, value):
            self.foo = value

        # 'bar' zu einer Property machen:
        bar = property(get_bar, set_bar)


Häufiger wird die ``property()``-Funktion allerdings als
:ref:`Funktionsdekorator <Dekorator>` genutzt. Die Bedeutung bleibt dabei
gleich, doch ist die Schreibweise etwas "übersichtlicher":

.. code-block:: python

    # Testklasse definieren:
    class C():

        # Normales Klassen-Attribut anlegen:
        foo = 1

        # Property 'bar' definieren:
        @property
        def bar(self):
            return self.foo

        # Setter für 'bar' definieren:
        @bar.setter
        def bar(self, value):
            self.foo = value

Erzeugt man mittels ``c = C()`` ein neues Objekt der obigen Beispielklasse, so
kann auch mittels ``c.bar`` auf das Attribut ``c.foo`` zugegriffen werden:

.. code-block:: python

    # Instanz der Beispiel-Klasse erzeugen:
    c = C()

    c.bar
    # Ergebnis: 1

    # Wert der Property 'bar' ändern:
    c.bar = 2

    c.foo
    # Ergebnis: 2

Üblicherweise erhält die Zielvariable, die von der Property verändert wird, den
gleichen Namen wie die Property selbst, jedoch mit einem ``_`` zu Beginn des
Variablennamens. Hierdurch wird ausgedrückt, dass die Variable nicht direkt
verändert werden sollte (obgleich dies möglich wäre). In der Setter-Funktion
kann dann beispielsweise explizit geprüft werden, ob eine vorgenommene
Wertzuweisung überhaupt zulässig ist.


.. index:: range()
.. _range():

range()
^^^^^^^

Die Funktion `range()
<https://docs.python.org/3/library/functions.html#func-range>`__ erzeugt eine
Sequenz ganzzahliger Werte. Sie kann wahlweise in folgenden Formen benutzt
werden:

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

*Beispiel:*

.. code-block:: python

    range(10)
    # Ergebnis: range(0,10)

    list( range(0, 10) )
    # Ergebnis: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    list( range(0, 10, 2) )
    # Ergebnis: [0, 2, 4, 6, 8]

    list( range(10, 0, -1) )
    # Ergebnis: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


.. index:: repr()
.. _repr():

repr()
^^^^^^

Die Funktion `repr(objekt)
<https://docs.python.org/3/library/functions.html#repr>`__ gibt als Ergebnis
eine Zeichenkette zurück, die eine kurze charakteristische Beschreibung des
Objekts beinhaltet; häufig entspricht dies einer Angabe der Objekt-Klasse, des
Objekt-Namens und der Speicheradresse.

*Beispiel:*

.. code-block:: python

    repr(print)
    # Ergebnis: '<built-in function print>'

Ist in der Klasse des angegebenen Objekts eine ``__repr__()``-Methode definiert,
so ist ``repr(objekt)`` identisch mit ``objekt.__repr__()``.

Als Zeichensatz wird für die Ausgabe des Strings Unicode verwendet, so dass
beispielsweise auch Umlaute im Ausgabe-String enthalten sein können.


.. index:: reversed()
.. _reversed():

reversed()
^^^^^^^^^^

Die Funktion `reversed(sequenz)
<https://docs.python.org/3/library/functions.html#reversed>`__ kann auf eine
iterierbares Objekt (beispielsweise ein Tupel oder eine Liste) angewendet
werden; sie gibt einen Iterator mit den gleichen Elementen, aber in der
umgekehrten Reihenfolge zurück.

*Beispiel*

.. code-block:: python

    liste = [1,5,2,3]

    liste_rev = reversed(liste)

    liste_rev
    # Ergebnis: <builtins.list_reverseiterator at 0x7f38edce2278>

    for i in liste_rev:
        print(i)

    # Ergebnis:
    # 3
    # 2
    # 5
    # 1


.. index:: round()
.. _round():

round()
^^^^^^^

Die Funktion `round()
<https://docs.python.org/3/library/functions.html#round>`__ rundet eine
``float``-Zahl auf die nächste ``int``-Zahl auf beziehungsweise ab und gibt
diese als Ergebnis zurück. Wird zusätzlich zur Zahl eine zweite Integer-Zahl als
Argument angegeben, also ``round(a, n)``,  so wird die Zahl ``a`` auf ``n``
Stellen gerundet als Ergebnis zurück gegeben.

.. code-block:: python

    round(15.37)
    #Ergebnis: 15

    round(15.37, 1)
    #Ergebnis: 15.4


.. index:: set()
.. _set():

set()
^^^^^

Die Funktion `set()
<https://docs.python.org/3/library/functions.html#func-set>`__ erzeugt ein neues
:ref:`set <Mengen>`-Objekt, also eine Menge.

Wird optional beim Aufruf von ``set()`` eine Sequenz als Argument angegeben, so
wird das Mengen-Objekt mit den Einträgen dieser Menge gefüllt (doppelte Einträge
bleiben ausgeschlossen).

*Beispiel:*

.. code-block:: python

    # Leeres Set-Objekt erstellen:
    s1 = set()

    # Set-Objekt aus einer Liste erstellen:
    s2 = set( [1, 3, 5, 7, 9, 9] )

    s2
    # Ergebnis: set({1, 3, 5, 7, 9})

    # Set-Objekt aus einer Zeichenkette erstellen:
    s3 = set( "Hallo Welt!" )

    s3
    # Ergebnis: set({' ', '!', 'H', 'W', 'a', 'e', 'l', 'o', 't'})


.. index:: setattr()
.. _setattr():

setattr()
^^^^^^^^^

Die Funktion `setattr(objekt, attributname, wert)
<https://docs.python.org/3/library/functions.html#setattr>`__ weist dem
angegebenen Attribut des als erstes Argument angegebenen Objekts den als drittes
Argument angegebenen Wert zu (sofern dies möglich ist); formal ist
``setattr(objekt, attributname, wert)`` somit identisch mit
``objekt.attributname = wert``.

*Beispiel:*

.. code-block:: python

    # Beispiel-Klasse:
    class Point():

        x = 5
        y = 4

    # Punkt-Objekt erzeugen:
    p = Point()

    # Attribut ändern:
    setattr(p, 'x', 3)

    # Attribut abrufen:
    getattr(p, 'x')
    # Ergebnis: 3

    # Attribut neu zuweisen:
    setattr(p, 'z', 2)

    # Attribut abrufen:
    getattr(p, 'z')
    # Ergebnis: 2


.. index:: slice()
.. _slice():

slice()
^^^^^^^

Die Funktion `slice(startwert, stopwert, stepwert)
<https://docs.python.org/3/library/functions.html#slice>`__ erstellt eine neue
Instanz eines Slice-Objekts. Dieses Objekt repräsentiert einen Satz an Indizes,
der durch die angegebenen Werte unveränderbar festgelegt ist.

*Beispiel*

.. code-block:: python

    s = slice(0,10,2)

    s.start
    # Ergebnis:0

    s.stop
    # Ergebnis:10

    s.step
    # Ergebnis:2

Beim Aufruf von ``slice()`` kann als Wert für die Argumente ``start`` und
``stop`` auch ``None`` angegeben werden. Das Slice-Objekt enthält dann nur
``step`` als unveränderlichen Wert. Wird das Slice-Objekt mit ``s`` bezeichnet,
so kann in diesem Fall beispielsweise mittels ``s.indices(100)`` ein neues
Slice-Objekt als Ergebnis geliefert werden, das den angegebenen Wert als
``stop``-Wert hat.

Slice-Objekte werden selten direkt verwendet. Allerdings werden bei Datentypen
wie :ref:`Zeichenketten <Indizierung von Zeichenketten>` oder :ref:`Listen
<Indizierung von Listen und Tupeln>` Slicings gerne zur Auswahl von Elementen
genutzt; ebenso können bei Verwendung von Modulen wie :ref:`numpy <numpy>` oder
:ref:`pandas <pandas>` Slicings eingesetzt werden, um mittels den dabei
resultierenden Indizes Teilbereiche aus Zahlenlisten zu selektieren. Die Syntax
lautet dabei etwa:

.. code-block:: python

    a = numpy.arange(10)

    # Als Zahlenbereich die dritte bis zur siebten Zahl selektieren:

    a[3:8]
    # Ergebnis: array([3, 4, 5, 6, 7])

    # Dabei nur jede zweite Zahl selektieren:

    a[3:8:2]
    # Ergebnis: array([3, 5, 7])

Verwendet man die gleichnamige Funktion ``slice()`` aus dem ``itertools``-Modul,
so wird als Ergebnis statt einem Slice ein entsprechendes Iterator-Objekt
zurückgegeben.


.. index:: sorted()
.. _sorted():

sorted()
^^^^^^^^

Die Funktion `sorted(sequenz)
<https://docs.python.org/3/library/functions.html#sorted>`__ kann auf eine
iterierbares Objekt (beispielsweise ein Tupel oder eine Liste) angewendet
werden; sie gibt eine Liste mit den entsprechenden Elementen in sortierter
Reihenfolge zurück.

*Beispiel*

.. code-block:: python

    sorted([1,5,2,3])
    # Ergebnis: [1, 2, 3, 5]


.. index:: staticmethod()
.. _staticmethod():

staticmethod()
^^^^^^^^^^^^^^

Die Funktion `staticmethod(methode)
<https://docs.python.org/3/library/functions.html#staticmethod>`__ macht die
angegebene Methode zu einer so genannten statischen Methode. Üblicherweise wird
die ``staticmethod()``-Funktion als :ref:`Funktionsdekorator <Dekorator>`
verwendet:

.. code-block:: python

    class C():

        @staticmethod
        def my_static_method(arguments):

            pass

Bei einer so definierten Methode wird weder der Name der Klasse noch der Name
der Instanz angegeben, von der aus die Methode aufgerufen wird.

Die statische Methode des obigen Beispiels kann wahlweise mittels
``C.my_class_method()`` oder ausgehend von einer Instanz der Klasse, also
mittels ``C().my_class_method()`` aufgerufen werden.


.. OLD: Die Funktion ``staticmethod()`` kann innerhalb von einer Klasse verwendet
.. werden, um eine vorangehend und ohne "self" als erstes Argument definierte
.. Methode zu einer :ref:`statische Methode <Statische Methode>` zu deklarieren.
.. Derartige Methoden können wahlweise mittels ``klassenname.methode()`` oder auch
.. mittels ``instanzname.methode()`` aufgerufen werden.


.. index:: str()
.. _str():

str()
^^^^^

Die Funktion `str(objekt)
<https://docs.python.org/3/library/functions.html#func-str>`__ gibt eine
String-Version des als Argument angegebenen Objekts aus. Hierbei wird die
Methode ``objekt.__str__()`` der jeweiligen Klasse aufgerufen.

*Beispiel:*

.. code-block:: python

    str( [1,2,3,4,5] )
    # Ergebnis: '[1, 2, 3, 4, 5]'


.. index:: sum()
.. _sum():

sum()
^^^^^

Die Funktion `sum(sequenz)
<https://docs.python.org/3/library/functions.html#sum>`__ gibt die Summe eines
iterierbaren Objekts (beispielsweise einer Liste) als Ergebnis zurück.

*Beispiel:*

.. code-block:: python

    sum( [1,2,3,4,5] )
    # Ergebnis: 15

    sum( range(100) )
    # Ergebnis: 4950


.. index:: super()
.. _super():

super()
^^^^^^^

.. Die Funktion ``super()``

... todo! ...

.. index:: tuple()
.. _tuple():

tuple()
^^^^^^^

Die Funktion `tuple(sequenz)
<https://docs.python.org/3/library/functions.html#func-tuple>`__ erzeugt aus der
angegebenen Sequenz (beispielsweise einer Liste oder einer Zeichenkette) eine
neue Instanz eines :ref:`tuple <tuple>`-Objekts, also eine unveränderliche
Liste.

*Beispiel:*

.. code-block:: python

    tuple('Hallo Welt!')
    # Ergebnis: ('H', 'a', 'l', 'l', 'o', ' ', 'W', 'e', 'l', 't')

    tuple( range(10) )
    # Ergebnis: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


.. index:: type()
.. _type():

type()
^^^^^^

Die Funktion `type(objekt) <https://docs.python.org/3/library/functions.html#type>`_
gibt als Ergebnis den Namen der Klasse des angegebenen Objekts zurück; dies ist
identisch mit einem Aufruf von ``objekt.__class__``.

*Beispiel:*

.. code-block:: python

    type("Hallo Welt!")
    # Ergebnis: builtins.str

Eine zweite Verwendungsmöglichkeit der ``type()``-Funktion liegt darin, sie als
``type(objektname, basisklasse, attribute-dict)`` aufzurufen, um ein neues
Objekt zu erstellen. Dieses erbt alle Eigenschaften der angegebenen Basisklasse
(oder mehrerer als Liste angegebener Basisklassen); zudem können für das Objekt
in form eines ``dict`` weitere Attribute definiert werden.

Die folgenden beiden Code-Varianten erzeugen jeweils ein Objekt mit gleichen
Eigenschaften:

.. code-block:: python

    # Beispielklasse definieren:
    class C(object):
        x = 1

    # Beispiel-Objekt generieren:
    c1 = C()

    # Type-Objekt mit gleichen Eigenschaften generieren:
    c2 = type('C', (object,), dict(x=1) ) 


.. index:: vars()
.. _vars():

vars()
^^^^^^

Die Funktion `vars() <https://docs.python.org/3/library/functions.html#vars>`__
gibt, sofern sie ohne Argument aufgerufen wird, als Ergebnis ein ``dict`` mit
den Namen und den Werten aller zum Zeitpunkt des Aufrufs existierenden lokalen,
das heißt im aktuellen Codeblock sichtbaren Variablen zurück (ebenso wie
:ref:`locals() <locals()>`).

Wird beim Aufruf von ``vars()`` als Argument ein beliebiges Objekt angegeben, so
wird der Inhalt von ``objekt.__dict__`` als Ergebnis zurückgegeben.


.. index:: zip()
.. _zip():

zip()
^^^^^

Die Funktion `zip() <https://docs.python.org/3/library/functions.html#zip>`__
verbindet -- ähnlich wie ein Reißverschluss -- Elemente aus verschiedenen
iterierbaren Objekten (beispielsweise Listen) zu einem neuen Iterator-Objekt,
dessen Elemente Zusammensetzungen der ursprünglichen Elemente sind.


*Beispiel:*

.. code-block:: python

    zip( ['a', 'b', 'c'], [1, 2, 3, 4] )
    # Ergebnis: <builtins.zip at 0x7f39027b22c8>

    list( zip( ['a', 'b', 'c'], [1, 2, 3, 4] ) )
    # Ergebnis: [('a', 1), ('b', 2), ('c', 3)]



.. _Standard-Module:
.. _Wichtige Standard-Module:

Wichtige Standard-Module
------------------------

Die im folgenden Abschnitt beschriebenen Module sind standardmäßig in Python
enthalten, ohne dass zusätzliche Software-Pakete installiert werden müssen:


.. _cmath:

``cmath`` -- Mathe-Modul für komplexe Zahlen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das `cmath <https://docs.python.org/3/library/cmath.html>`__-Modul umfasst viele
Funktionen des ``math``-Moduls, die allerdings komplexe Zahlen als Argumente
zulassen.

.. _copy:

``copy`` -- Kopien von Objekten erstellen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das `copy <https://docs.python.org/3/library/copy.html>`__-Modul stellt
insbesondere die Funktion ``deepcopy()`` bereit, mit der :math:`1:1`-Kopien von
existierenden Objekten gemacht werden können.

Erstellt man eine Kopie eines Objekts mittels ``objekt2 =
objekt1.copy()``, so wird genau genommen nur eine neue Referenz auf das
bestehende Objekt angelegt. Hat ``objekt1`` beispielsweise ein Attribut ``x``
mit dem Wert ``5``, so würde durch eine Eingabe von ``objekt2.x = 7`` auch der
Attribut-Wert von ``objekt1`` geändert. Ein solches Verhalten ist beispielsweise
bei der Übergabe von Objekten an Funktionen erwünscht, entspricht allerdings
nicht der klassischen Vorstellung einer Kopie. Eine solche kann folgendermaßen
erstellt werden:

.. code-block:: python

    import copy

    objekt2 = copy.deepcopy(objekt1)

Werden nun die Attribut-Werte von ``objekt2`` geändert, so bleiben die Werte des
Original-Objekts unverändert.


.. _cProfile:

``cProfile`` -- Profiler
^^^^^^^^^^^^^^^^^^^^^^^^

Mittels des Pakets `cProfile <https://docs.python.org/3/library/profile.html>`__
und der darin definierten Funktion ``run()`` kann ermittelt werden, wie viel
Zeit für einen Aufruf einer Funktion benötigt wird. Bei einer Funktion, die
weitere Unterfunktionen aufruft, wird zudem angezeigt, wie viel Zeit auf die
einzelnen Schritte entfällt:

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

.. index:: os (Modul)
.. _os:

os - Interaktion mit dem Betriebsystem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das `os <https://docs.python.org/3/library/os.html>`__-Modul stellt einige
nützliche Funktionen und Konstanten bereit, um gewöhnliche Aufgaben auf der
Ebene des Betriebsystems durchführen zu können.

* Mit ``os.chdir()`` wird das als Argument angegebene Verzeichnis zum aktuellen Arbeitsverzeichnis.
* Mit ``os.getcwd()`` wird der Pfad des aktuellen Arbeitsverzeichnisses ausgegeben.
* Mit ``os.listdir()`` wird eine Liste aller Dateinamen des als Argument
  angegebenen Verzeichnisses ausgegeben.
* Mit ``os.mkdir()`` wird das als Argument angegebene Verzeichnis neu erstellt.
* Mit ``os.rmdir()`` wird das als Argument angegebene Verzeichnis gelöscht.
* Mit ``os.remove()`` wird die als Argument angegebene Datei gelöscht.
* Mit ``os.rename(old, new)`` wird einer Datei oder einem Verzeichnis ein neuer
  Name zugewiesen.

Mit der Funktion ``os.popen()`` ist es zudem möglich, ein Programm in einer
gewöhnlichen Shell aufzurufen. Hierzu wird der Funktion ``os.popen()`` als
Argument eine Zeichenkette angegeben, deren Inhalt an den Shell-Interpreter
weitergereicht wird. Die Ausgabe des Programms wird in eine :ref:`Pipe
<gwl:Pipe>` geschrieben, die wie ein :ref:`Datei <file>`-Objekt wahlweise
zeilenweise mittels ``readline()`` oder als Ganzes mittels ``read()`` ausgelesen
werden kann:

.. code-block:: python

    import os

    # Shell-Anweisung festlegen:
    command = 'ls -l'

    # Shell-Anweisung ausführen:
    # (Der Rückgabewert ist ein Filepointer auf die Pipe)
    fp = os.popen(command)

    # Das Ergebnis der Shellanweisung (Pipe) auslesen:
    ergebnis = fp.read()

    # Pipe schließen:
    # (Status == None bedeutet fehlerfreies Schließen)
    status = fp.close()


.. index:: os.path (Modul)
.. _os.path:

os.path - Pfadfunktionen
"""""""""""""""""""""""""

Das `os.path <https://docs.python.org/3/library/os.path.html>`__-Modul stellt einige
nützliche Funktionen bereit, die bei der Arbeit mit Datei- und Verzeichnisnamen
hilfreich sind:

* Mit ``os.path.exists()`` kann geprüft werden, ob der als Argument angegebene
  Dateiname als Pfad im Dateisystem existiert; als Ergebnis gibt die Funktion
  ``True`` oder ``False`` zurück.
* Mit ``os.path.isdir()`` kann geprüft werden, ob der als Argument angegebene
  Pfad ein Verzeichnis ist; als Ergebnis gibt die Funktion
  ``True`` oder ``False`` zurück.
* Mit ``os.path.isfile()`` kann geprüft werden, ob der als Argument angegebene
  Pfad eine Datei ist; als Ergebnis gibt die Funktion
  ``True`` oder ``False`` zurück.
* Mit ``os.path.getsize()`` kann der vom als Argument angegebenen Pfad belegte
  Speicherplatz ausgegeben werden.


Um nicht nur relative, sondern auch absolute Pfadangaben nutzen zu können, kann
die Funktion ``os.path.abspath()`` genutzt werden; diese gibt zu einem
angegebenen (relativen) Dateinamen den zugehörigen absoluten Pfad an.

.. todo os.path.join(verzeichnisname, dateiname)


.. index:: pickle (Modul)
.. _pickle:

pickle - Speichern von Python-Objekten
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Das `pickle <https://docs.python.org/3/library/pickle.html>`__-Modul ermöglicht
es, während einer Python-Sitzung existierende Objekte in Byte-Strings
umzuwandeln und diese auf einer Festplatte zu speichern; ebenso können auf diese
Art festgehaltene Daten mittels ``pickle`` zu einem späteren Zeitpunkt (sogar
nach einem Neustart des Systems) auch wieder gelesen werden.

Um ein beliebiges Python-Objekt mittels ``pickle`` als Zeichenkette zu codieren,
gibt man folgendes ein:

.. code-block:: python

    import pickle

    liste_original = [1,2,3,4,5]

    # Objekt als Byte-String ausgeben:
    storage = pickle.dumps(liste_original)
    b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04K\x05e.'

Hierbei steht ``dumps`` für "dump string". Der erzeugte Byte-String ist zwar für
Menschen nicht unmittelbar lesbar, kann aber vom Computer effizient geschrieben
und auch mittels ``pickle.loads()`` ("load string") wieder ausgelesen werden:

.. code-block:: python

    # Byte-String zurückübersetzen:
    liste_neu = pickle.loads(storage)

    liste_neu
    # Ergebnis: [1,2,3,4,5]

Das wieder geladene Objekt ist inhaltlich mit dem Original identisch, wird vom
Interpreter jedoch als neues Objekt gehandhabt.

Soll das Ablegen eines Objekts unmittelbar in eine Datei erfolgen, so kann
anstelle von ``pickle.dumps()`` die Funktion ``pickle.dump()`` verwendet und
dabei als Argument ein existierender File-Pointer angegeben werden. Umgekehrt
kann mittels ``pickle.load()`` wieder unmittelbar aus dem als Argument
angegebenen Datei-Objekt gelesen werden.


.. index:: Zufallszahlen, random (Modul)
.. _random:

random - Zufallsgenerator
^^^^^^^^^^^^^^^^^^^^^^^^^

Das `random <https://docs.python.org/3/library/random.html>`__-Modul stellt
Funktion zum Erzeugen von Zufallszahlen, für das Auswählen eines zufälligen
Elements aus einer Liste sowie für das Umsortieren von Listen bereit.

Zu Beginn sollte zunächst stets eine neue Basis für die Erzeugung von
Zufallszahlen in der aktuellen Python-Sitzung erstellt werden:

.. code-block:: python

    import random

    # Zufallszahlen initiieren:
    random.seed()

Anschließend können folgende Funktionen genutzt werden:

* Die Funktion ``random.random()`` liefert als Ergebnis eine Zufallszahl
  zwischen ``0.0`` und ``1.0`` (einschließlich dieser beiden Werte).
* Die Funktion ``random.randint(min,max)`` liefert als Ergebnis eine ganzzahlige
  Zufallszahl zwischen ``min`` und ``max`` (einschließlich dieser beiden Werte).
* Die Funktion ``random.choice(sequenz)`` wählt ein zufälliges Element aus einer
  Sequenz (beispielsweise einer Liste oder einem Tupel) aus.
* Die Funktion ``random.shuffle(liste)`` ordnet die Elemente einer Liste auf
  zufällige Weise neu an; dabei wird das Original verändert.

Beispielsweise kann also mittels ``random.randint(1,6)`` das Verhalten eines
gewöhnlichen sechsflächigen Würfels imitiert werden.

.. _timeit:

``timeit`` -- Laufzeitanalyse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mittels des Pakets `timeit
<https://docs.python.org/3/library/timeit.html>`__ und der
gleichnamigen Funktion aus diesem Paket kann einfach ermittelt werden, wieviel
Zeit eine Funktion für einen Aufruf benötigt:

.. code-block:: python

    import timeit

    timeit.timeit("x = 2 ** 2")
    # Ergebnis: 0.02761734207160771







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


