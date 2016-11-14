.. index:: Klasse, Attribut, Methode
.. _Klassen und Objektorientierung:

Klassen und Objektorientierung
==============================

Um Quellcode besser zu strukturieren, werden bei der objektorientierten
Programmierung so genannte Klassen erzeugt, die jeweils bestimmte Eigenschaften
("Attribute") und  Funktionen ("Methoden") besitzen. Klassen werden in Python
allgemein durch einzelne Zeichenketten mit großen Anfangsbuchstaben
gekennzeichnet.

.. index:: class

Eine neue Klasse wird in Python mit dem Schlüsselwort ``class``, gefolgt vom
Klassennamen und einem Doppelpunkt eingeleitet. Alle darauf folgenden
Definitionen von Eigenschaften und Funktionen, die zur Klasse gehören, werden
um eine Tabulatorweite (üblicherweise 4 Leerzeichen) eingerückt.

.. _Definition und Initialisierung eigener Klassen:

Definition und Initialisierung eigener Klassen
----------------------------------------------

Ebenso wichtig wie der Begriff einer Klasse ist der Begriff der Instanz einer
Klasse. Während beispielsweise die Klasse "Wecker" einen Objekttyp eines meist
unhöflich Lärm erzeugenden Gerätes darstellt, so ist ein einzelner neben einem
Bett stehender Wecker ein konkreter Vertreter dieser Klasse. Eine solche Instanz
hat, zumindest in der Programmierung, stets alle in der Klasse definierten
Eigenschaften und Funktionen, allerdings mit möglicher unterschiedlicher
Ausprägung (beispielsweise Farbe oder Klingelton).

In Python könnte die Implementierung einer Beispielklasse etwa so aussehen:

.. code-block:: python

    class AlarmClock():
        """
        Just a simple Class example.
        """

        def __init__(self, color, sound):
            """
            Initialize a new alarm clock.

            Arguments:

            * color (string): Color of the alarm clock.
            * sound (string): Ringing sound of the clock.
            """
            self.color = color
            self.sound = sound

        def show_color(self):
            return self.color

        def ring(self):
            return self.sound + "!!!"

Im obigen Beispiel wurde zunächst die Klasse ``AlarmClock`` definiert und als.
erstes mit einem :ref:`Docstring <Docstring>` versehen, der eine kurze
Beschreibung der Klasse liefert.

.. index:: __init__()

In der Funktion ``__init__()`` wird anschließend festgelegt, wie eine neue
Instanz der Klasse erzeugt wird. Die angegebenen Argumente werden dabei als
Eigenschaften der Instanz, die in Python mit ``self`` bezeichnet wird,
gespeichert. Nach der Initialisierung stehen im obigen Beispiel dem neuen Objekt
dann die beiden weiteren angegebenen Funktionen ``show_color()`` und ``ring()``
bereit, die als Ausgabe der jeweiligen Objektvariablen dienen.

Die Methode ``__init__()`` wird automatisch aufgerufen, wenn man den Namen der
Klasse als Funktion aufruft. Eine neue Instanz einer Klasse lässt sich im
Fall des obigen Beispiels also folgendermaßen erzeugen:

.. code-block:: python

    # Initialisierung:
    my_alarm_clock = AlarmClock("green", "Ring Ring Ring")


    # Objekttyp testen:

    type(my_alarm_clock)
    # Ergebnis: __main__.AlarmClock


    # Funktionen testen:

    my_alarm_clock.show_color()
    # Ergebnis: 'green'

    my_alarm_clock.ring()
    # Ergebnis: 'Ring Ring Ring!!!'

.. index:: __type__()

Mittels ``type(objektname)`` kann allgemein angezeigt werden, zu welcher Klasse
ein beliebiges Python-Objekt gehört; ebenso kann mit ``isinstance(objektname,
klassenname)`` geprüft werden, ob ein Objekt eine Instanz der angegebenen Klasse
ist.

.. index:: Garbage Collector, __del__()

Möchte man eine konkrete Instanz wieder löschen, so ist dies allgemein mittels
``del(name_der_instanz)`` möglich, im obigen Fall also mittels
``del(my_alarm_clock)``. Genau genommen wird die Instanz allerdings nur dann
gelöscht, wenn die letzte Referenz auf die Instanz gelöscht wird. Sind
beispielsweise mittels ``alarm_clock_1 = alarm_clock_2 = AlarmClock("blue",
"Ring!")`` zwei Referenzen auf die gleiche Instanz erzeugt worden, so wird
mittels ``del(alarm_clock_1)`` nur die erste Referenz gelöscht; die Instanz
selbst bleibt weiter bestehen, da die Variable ``alarm_clock_2`` immer noch
darauf verweist. Beim Löschen der letzten Referenz auf wird automatisch Pythons
"Garbage Collector" aktiv und übernimmt die Aufräumarbeiten, indem die
entsprechende ``__del__()``-Methode aufgerufen wird; ebenso wird der benötigte
Platz im Arbeitsspeicher dadurch automatisch wieder freigegeben.

Sollen bei der Löschung einer Instanz weitere Aufgaben abgearbeitet werden, so
können diese in einer optionalen Funktion ``__del__()`` innerhalb der Klasse
festgelegt werden.

.. index:: Member
.. _Allgemeine Eigenschaften von Klassen:

Allgemeine Eigenschaften von Klassen
------------------------------------

Klassen dienen allgemein dazu, die Attribute und Methoden (kurz: "Member")
einzelner Objekte festzulegen. Bei der Festlegung der Attribute und Methoden
wird jeweils das Schlüsselwort ``self`` genutzt, das auf die jeweilige Instanz
einer Klasse verweist.

Attribute eines Objekts werden mittels ``self.attributname = wert`` festgelegt;
dies erfolgt üblicherweise bereits bei der Initialisierung. Anschließend kann
auf die so definierten Attribute innerhalb der Klasse mittels
``self.attributname`` und außerhalb mittels ``instanzname.attributname``
zugegriffen werden.

Methoden eines Objekts werden ebenso wie Funktionen definiert, mit der einzigen
Besonderheit, dass als erstes Argument stets ``self`` angegeben wird. Innerhalb
der Klasse können so definierte Methoden mittels ``self.methodenname()`` und
außerhalb mittels ``instanzname.methodenname()`` aufgerufen werden.

.. _Geschützte und private Attribute und Methoden:

.. rubric:: Geschützte und private Attribute und Methoden

In manchen Fällen möchte man vermeiden, dass die Attribute eines Objekts durch
andere Objekte manipuliert werden können; ebenso sind manche Methoden nur für
den "internen" Gebrauch innerhalb einer Klasse geeignet. In Python gibt es für
diesen Zweck sowohl geschützte ("protected") als auch private ("private")
Attribute und Methoden:

* Geschützte Member (Attribute und Methoden) werden durch einen einfach
  Unterstrich vor dem jeweiligen Namen gekennzeichnet. Auf derartige Attribute
  oder Methoden kann weiterhin von einer anderen Stelle aus sowohl lesend als
  auch schreibend zugegriffen werden; es ist vielmehr eine Konvention zwischen
  Python-Entwicklern, dass auf derartige Member nicht direkt zugegriffen werden
  sollte.

* Private Member werden durch einen doppelten Unterstrich vor dem jeweiligen
  Namen gekennzeichnet. Auf derartige Attribute kann außerhalb der Klasse weder
  lesend noch schreibend zugegriffen werden.

Attribute sollten beispielsweise dann als geschützt oder privat gekennzeichnet
werden, wenn sie nur bestimmte Werte annehmen sollen. In diesem Fall werden
zusätzlich so genannte "Getter" und "Setter"-Methoden definiert, deren Aufgabe
es ist, nach einer Prüfung auf Korrektheit den Wert des entsprechenden Attributs
auszugeben oder ihm einen neuen Wert zuzuweisen.

.. Geschützte Methoden und Attribute bleiben bei ``from modulname import *``
.. unberücksichtigt!

.. index:: Property
.. _Property:

Setter- und Getter-Methoden werden bevorzugt als so genannte "Properties"
definiert; dazu wird folgende Syntax verwendet:

.. code-block:: python

    class MyClass:

    def __init__(self):
        self._myattr = None

    def get_myattr(self):
        return self._myattr

    def set_myattr(self, value):
        # todo: check if value is valid

        self._myattr = value

    self.myattr = property(get_myattr, set_myattr)

.. todo Verwendung eines Decorators!

Mittels der ``property()``-Funktion wird die Setter- und Getter-Methode eines
geschützten oder privaten Attributs dem gleichen, nicht-geschützten
Attributnamen zugewiesen. Von außerhalb der Klasse ist dieses gezielte Handling
also nicht sichtbar, das entsprechende Attribut erscheint von außen also wie ein
gewöhnliches Attribut. Dieses Prinzip der Kapselung von Aufgaben ist typisch für
objektorientierte Programmierung: Wichtig ist es, die Aufgabe eines Objekts klar
zu definieren sowie seine "Schnittstellen", also seine von außerhalb
zugänglichen Attribute und Methoden, festzulegen. Solange das Objekt als
einzelner Baustein seine Aufgabe damit erfüllt, braucht man sich als Entwickler
um die Interna dieses Bausteins nicht weiter Gedanken zu machen.

.. index:: Statisches Attribut, Statische Methode
.. _Statische Member:

.. rubric:: Statische Member

Neben Attributen und Methoden, die jede einzelne Instanz einer Klasse an sich
bereitstellt, können innerhalb einer Klasse auch Attribute und/oder Methoden
definiert werden, die für alle Instanzen der Klasse gleichermaßen gelten.
Derartige Klassenmember werden "statisch" genannt.

Statische Attribute lassen sich erzeugen, indem innerhalb der Klasse
(üblicherweise gleich zu Beginn des Klassen-Blocks) die gewünschten Attribute
wie normale Variablen gesetzt werden, also ohne vorangestelltes ``self`` und
außerhalb einer Methoden-Definition. Der Zugriff auf statische Attribute kann
dann (sowohl lesend als auch schreibend) wahlweise mittels
``Klassenname.attributname`` oder mittels ``Instanzname.attributname`` erfolgen:

.. code-block:: python

    # Definition eines statischen Attributs:

    class MyClass:

        myattr = 42

        pass

    # Zugriff auf ein statisches Attribut:

    MyClass.myattr
    # Ergebnis: 42

    MyClass().myattr
    # Ergebnis: 42

.. index:: staticmethod(), Statische Methode
.. _Statische Methode:

Statische Methoden werden ebenso wie gewöhnliche Methoden definiert, außer dass
bei der Definition das ``self`` als erstes Argument weggelassen wird;
stattdessen wird die Methode anschließend mittels der Funktion
``staticmethod()`` zur statische Methode deklariert:

.. code-block:: python

    # Definition einer statischen Methode:

    class MyClass:

        def mymethod():
            print("Hello!")

        mymethod = staticmethod(mymethod)

    # Aufruf einer statischen Methode:

    MyClass.mymethod()
    # Ergebnis: Hello!

    MyClass().mymethod()
    # Ergebnis: Hello!

Statische Attribute und Methoden können auch dann genutzt werden, wenn (noch)
keine Instanz der Klasse existiert.

.. todo Verwendung eines Decorators!

.. todo Klassenmethoden

.. index:: Magic Member, Operator-Überladung
.. _Magic Member:

.. rubric:: "Magic" Member

Als "Magic Member" werden private Attribute und Funktionen von Klassen
bezeichnet, die es beispielsweise ermöglichen, einzelne Instanzen der Klassen
mittels Operatoren miteinander in Relation zu setzen oder Builtin-Funktionen auf
die einzelnen Instanzen anzuwenden. Die Bezeichnung "magisch" stammt daher, dass
diese Methoden und Attribute selten direkt mit ihrem Namen angesprochen werden,
aber dafür oft implizit genutzt werden -- wie beispielsweise die ``__init__()``
oder ``__del__()``-Funktionen als Konstruktor- und Destruktor-Methoden einzelner
Instanzen. Beispielsweise wird anstelle ``MyClass.__init__()`` wird
üblicherweise ``MyClass()`` geschrieben, um eine neue Instanz einer Klasse zu
erzeugen; bei letzterer Variante wird die ``__init__()``-Funktion vom
Python-Interpreter implizit aufgerufen.

Folgende Member sind für die Repräsentation von Objekten vorgesehen:

.. index:: __str__()

* Mittels der Methode ``__str()__`` wird eine für Menschen gut lesbare
  Zeichenkette definiert, die beim Aufruf von ``str(MyClass)`` als
  Objektbeschreibung ausgegeben werden soll.

.. index:: __repr__()

* Die Methode ``__repr()`` wird so definiert, dass sie Python-Code als Ergebnis
  zurückgibt, bei dessen Ausführung eine neue Instanz der jeweiligen Klasse
  erzeugt wird.

* Die Methode ``__call__()`` bewirkt, sofern sie definiert ist, dass eine
  Instanz einer Klasse -- ebenso wie eine Funktion -- aufgerufen werden kann.

Folgende Member sind für den Zugriff auf Attribute vorgesehen:

.. index:: __dict__

* Mit dem Attribut ``__dict__`` wird als :ref:`dict <dict>` aufgelistet, welche
  Attribute und zugehörigen Werte die jeweilige Instanz der Klasse aktuell
  beinhaltet.

.. index:: __slots__

* Durch das (statische) Attribut ``__slots__`` kann mittels einer Liste
  festgelegt werden, welche Attributnamen die Instanzen einer Klasse haben.
  Wird versucht, mittels ``del(instanzname.attributname)`` ein Attribut einer
  Instanz zu löschen, dessen Name in der ``__slots__``-Liste enthalten ist, so
  schlägt das Löschen mit einem ``AttributeError`` fehl. Umgekehrt wird auch
  dann ein ``AttributeError`` ausgelöst, wenn man versucht, ein neues Attribut
  für die Instanz festzulegen, dessen Name nicht in der ``__slots__``-Liste
  enthalten ist.

.. index:: __getattr__() und __getattribute__()

* Mit der Methode ``__getattr__()`` wird definiert, wie sich die Klasse zu
  verhalten hat, wenn ein angegebenes Attribut abgefragt wird, aber nicht
  existiert. Wahlweise kann ein Standard-Wert zurückgegeben werden,
  üblicherweise wird jedoch ein ``AttributeError`` ausgelöst.

  | Mit der Methode ``__getattribute__()`` wird das angegebene Attribut
    ausgegeben, sofern es existiert. Andernfalls kann -- wie bei ``__getattr__()``
    -- wahlweise ein Standard-Wert zurückgegeben oder ein ``AttributeError``
    ausgelöst werden. Wenn die ``__getattribute()__`` definiert ist, wird die
    ``__getattr__()``-Methode nicht aufgerufen, außer sie wird innerhalb von
    ``__getattribute()__`` explizit aufgerufen.
  | Zu beachten ist außerdem, dass innerhalb von ``__getattribute()__`` nur
    mittels ``klassenname.__getattribute__(self, attributname)`` auf ein Attribut
    zugegriffen werden darf, nicht mittels ``self.attributname``; im letzteren
    Fall würde ansonsten eine Endlos-Schleife erzeugt.

.. index:: __setattr__()

* | Mit der Methode ``__setattr__()`` wird eine Routine angegeben, die
    aufgerufen wird, wenn ein Attribut neu erstellt oder verändert wird. Dafür
    wird zunächst der Name des Attributs und als zweites Argument der zuzuweisende
    Wert angegeben. Insbesondere kann mit dieser Methode kontrolliert werden, dass
    keine unerwünschten Attribute vergeben werden können.
  | Bei der Verwendung von ``__setattr__()`` ist zu beachten, dass die
    Wertzuweisung mittels ``self.__dict__['attributname'] = wert`` erfolgen
    muss, da ansonsten eine Endlos-Schleife erzeugt würde.

.. index:: __delattr__()

* Mit ``__delattr__()`` wird als Methode festgelegt, wie sich eine Instanz beim
  Aufruf von ``del(instanzname.attributname)`` verhalten soll.


Folgende Member sind für den Vergleich zweier Objekte vorgesehen:

.. index:: __eq__(), __ne__()

* Mit den Methoden ``__eq__()`` ("equal") und ``__ne__()`` ("not equal") kann
  festgelegt werden, nach welchen Kriterien zwei Instanzen verglichen werden
  sollen, wenn ``instanz_1 == instanz_2`` beziehungsweise ``instanz_1 !=
  instanz_2`` aufgerufen wird. Diese Operator-Kurzschreibweise wird intern in
  ``instanz_1.__eq__(instanz_2)`` übersetzt, es wird also die Equal-Methode des
  ersten Objekts aufgerufen.

.. index:: __gt__(), __ge__(), __lt__(), __le__()

* Mit den Methoden ``__gt__()`` ("greater than") und ``__ge__()`` ("greater
  equal") kann festgelegt werden, nach welchen Kriterien sich zwei Instanzen
  verglichen werden sollen, wenn ``instanz_1 > instanz_2`` beziehungsweise
  ``instanz_1 >= instanz_2`` aufgerufen wird. Entsprechend kann mit ``__lt__()``
  ("less than") und ``__le__()`` ("less equal") kann festgelegt werden, nach
  welchen Kriterien sich zwei Objekte verglichen werden, wenn ``instanz_1 <
  instanz_2`` beziehungsweise ``instanz_1 <= instanz_2`` aufgerufen wird.

.. index:: __hash__()

* Mit der Methode ``__hash__()`` wird ein zu der angegebenen Instanz gehörender
  Hash-Wert ausgegeben, der die Instanz als Objekt eindeutig identifiziert.

Folgendes Member ist für logische Operationen vorgesehen:

.. index:: __bool__()

* Mit der Methode ``__bool__()`` wird festgelegt, in welchen Fällen eine Instanz
  den Wahrheitswert ``True`` oder den Wahrheitswert ``False`` zurückgeben soll,
  wenn ``bool(instanz)`` aufgerufen wird; dies erfolgt beispielsweise implizit
  bei :ref:`if <if>`-Bedingungen.

.. ``__and__()``
.. ``__or__()``
.. ``__xor__()``

Folgende Member sind für numerische Operationen vorgesehen:

* Mit den Methoden ``__int__()``, ``__oct__()``, ``__hex__()``, ``__float__()``,
  ``__long__()`` und ``__complex__()`` kann festgelegt werden, wie das Objekt
  durch einen Aufruf von ``int(instanz)``, ``oct(instanz)`` usw. in den
  jeweiligen numerischen Datentyp umzuwandeln ist.

* Mit den Methoden ``__pos__()`` und ``__neg__()`` kann festgelegt werden,
  welche Ergebnisse die unären Operatoren ``+instanz`` beziehungsweise
  ``-instanz`` liefern sollen; zusätzlich kann mit der Methode ``__abs__()``
  (Absolut-Betrag) festgelegt werden, welches Ergebnis ein Aufruf von
  ``abs(instanz)`` liefern soll. Ebenso wird durch die Methoden ``__round__()``
  (Rundung) bestimmt, welches Ergebnis beim Aufruf von ``round(instanz)`` bzw.
  ``round(instanz, num)`` zu erwarten ist.

* Mit den Methoden ``__add__()``, ``__sub__()``, ``__mul__()`` und
  ``__truediv__()`` wird festgelegt, welches Ergebnis sich bei der Verknüpfung zweier
  Instanzen mit den vier Grundrechenarten ergeben soll, also ``instanz_1 +
  instanz_2``, ``instanz_1 - instanz_2``, usw. Zusätzlich wird durch die Methode
  ``__pow__()`` (Potenzrechnung) festgelegt, welches Ergebnis ``instanz_1 **
  instanz__2`` liefern soll.

* Mit der Methode ``__floordiv__()`` wird die Bedeutung von ``instanz_1 //
  instanz_2``  festgelegt; bei normalen Zahlen wird damit derjenige ``int``-Wert
  bezeichnet, der kleiner oder gleich dem Ergebnis der Division ist
  (beispielsweise ergibt ``5 // 3`` den Wert ``1``, und ``-5 // 3`` den Wert
  ``-2``). Zudem wird durch die Methode ``__mod__()`` (Modulo-Rechnung) die
  Bedeutung von ``instanz_1 % instanz_2`` festgelegt, was bei normalen Zahlen
  dem ganzzahligen Divisionsrest entspricht.

.. ``__lshift__()``
.. ``__rshift__()``

Folgende Member sind für Wertzuweisungen vorgesehen:

* Mit den Methoden ``__iadd__()``, ``__isub__()``, ``__imul__()`` und
  ``__itruediv__()`` wird festgelegt, welches Ergebnis sich bei der kombinierten
  Wertzuweisung zweier Instanzen mit den vier Grundrechenarten ergeben soll,
  also ``instanz_1 += instanz_2``, ``instanz_1 -= instanz_2``, usw. Zusätzlich
  wird durch die Methode ``__ipow__()`` (Potenzrechnung) festgelegt, welches
  Ergebnis ``instanz_1 **= instanz__2`` liefern soll.

* Mit der Methode ``__ifloordiv__()`` wird die Bedeutung von ``instanz_1 //=
  instanz_2``  festgelegt; bei normalen Zahlen wird ``instanz_1`` dabei
  derjenige Wert zugewiesen, der sich bei der Auswertung von ``instanz_1 //
  instanz_2`` ergibt. In gleicher Weise wird durch die Methode ``__imod__()``
  (Modulo-Rechnung) die Bedeutung von ``instanz_1 %= instanz_2`` festgelegt;
  hierbei erhält ``instanz_1`` als Wert das Ergebnis von ``instanz_1 %
  instanz_2``.

.. ``__ilshift__()``
.. ``__irshift__()``

Folgende Member sind für Container, Slicings und Iteratoren vorgesehen:

* Die Methode ``__len__()`` wird aufgerufen, wenn mittels ``len(instanz)`` die
  Länge eines Containers geprüft werden soll.

* Die Methode ``__contains__()`` wird aufgerufen, wenn mittels ``element in
  instanz`` geprüft wird, ob das als Argument angegebene Element im Container
  enthalten ist.

* Die Methode ``__getitem__()`` wird aufgerufen, wenn mittels ``instanz[key]``
  der zu dem als Argument angegebenen Schlüssel gehörende Wert abgerufen werden
  soll.

* Die Methode ``__setitem__()`` wird aufgerufen, wenn mittels ``instanz[key] =
  value`` dem als erstes Argument angegebenen Schlüssel der als zweites Argument
  angegebene Wert zugewiesen werden soll 

* Die Methode ``__delitem__()`` wird aufgerufen, wenn mittels ``del
  instanz[element]`` das als Argument angegebene Element aus dem Contaniner
  gelöscht werden soll.

.. TODO
.. * Die Methode ``__iter__()`` 
.. ``__reversed__()``

Folgende Member sind für die Verwendung des Objekts innerhalb von :ref:`with
<with>`-Konstrukten vorgesehen:

* Mit der Methode ``__enter__()`` werden Anweisungen definiert, die einmalig
  ausgeführt werden sollen, wenn eine Instanz der Klasse in eine :ref:`with
  <with>`-Umgebung geladen wird.
* Mit der Methode ``__exit__()`` werden Anweisungen definiert, die einmalig
  ausgeführt werden sollen, wenn eine :ref:`with <with>`-Umgebung um eine
  Instanz der Klasse wieder verlassen wird.

Mit Hilfe der "Magic Members" können also neue Klassen von Objekten definiert
werden, deren Verhalten dem von bestehenden Klassen (Zahlen, Listen, usw.)
ähnelt. Wird einem Operator, beispielsweise dem Plus-Operators ``+``, mittels
der Funktion ``__add__()`` eine neue, auf den Objekttyp passendere Bedeutung
zugewiesen, so spricht man auch von "Operator-Überladung".

Objekte zeichnen sich also weniger durch ihre Bezeichnung, sondern vielmehr
durch ihre Eigenschaften und Methoden aus. Dieses Konzept wird bisweilen auch
als "Duck Typing" bezeichnet:

.. epigraph::

    "Wenn ich einen Vogel sehe, der wie eine Ente läuft, wie eine Ente schwimmt
    und wie eine Ente schnattert, dann nenne ich diesen Vogel eine Ente."

    -- `James Riley <https://de.wikipedia.org/wiki/Duck_Typing>`_

Kann eine Funktion umgekehrt auf verschiedene Objekt-Typen angewendet werden, so
nennt man sie polymorph. Beispielsweise kann die Builtin-Funktion ``sum()`` auf
beliebige listen-artige Objekttypen angewendet werden, sofern für diese eine
``__add__()``-Funktion definiert ist. Durch Polymorphismus als Spracheigenschaft
wird einmal geschriebener Code oftmals auch an einer anderen Stelle verwendbar.


.. index:: Vererbung
.. _Vererbung:

Vererbung
---------

Mit dem Begriff "Vererbung" wird ein in der Objekt-orientierten Programmierung
sehr wichtiges Konzept bezeichnet, das es ermöglicht, bei der Definition von
fein spezifizierten Objekte auf allgemeinere Basis-Klassen zurückzugreifen; die
Basis-Klasse "vererbt" dabei ihre Attribute und Methoden an die abgeleitete
Sub-Klasse, wobei in dieser weitere Eigenschaften hinzukommen oder die geerbten
Eigenschaften angepasst werden können. Aus mathematischer Sicht ist die
Basis-Klasse eine echte Teilmenge der daraus abgeleiteten Klasse, da diese alle
Eigenschaften der ursprünglichen Klasse (und gegebenenfalls noch weitere)
enthält.

Um die Eigenschaften einer Basis-Klasse in einer neuen Klasse zu übernehmen,
muss diese bei der Klassendefinition in runden Klammern angegeben werden:

.. code-block:: python

    class SubClass(MyClass):

        pass

Bis auf diese Besonderheit werden alle Attribute und Methoden in einer
abgeleiteten Klasse ebenso definiert wie in einer Klasse, die keine Basis-Klasse
aufweist.

.. todo Basis-Klasse object, super()

In Python ist es prinzipiell möglich, dass eine Klasse auch mehrere
Basis-Klassen aufweist; in diesem Fall werden die einzelnen Klassennamen bei der
Definition der neuen Klasse durch Kommata getrennt angegeben. Die links stehende Klasse
hat dabei beim Vererben der Eigenschaften die höchste Priorität, gleichnamige
Attribute oder Methoden werden durch die weiteren Basis-Klassen also nicht
überschrieben, sondern nur ergänzt. Da durch Mehrfach-Vererbungen allerdings
keine eindeutige Baumstruktur mehr vorliegt, also nicht mehr auf den ersten
Blick erkennbar ist, aus welcher Klasse die abgeleiteten Attribute und Methoden
ursprünglich stammen, sollte Mehrfach-Vererbung nur in Ausnahmefällen und mit
Vorsicht eingesetzt werden.

.. index:: Dekorator
.. _Dekoratoren:
.. _Dekorator:

Dekoratoren
-----------

Dekoratoren werden in Python als Kurzschreibweise verwendet, um bestimmte,
innerhalb einer Klasse definierte Methoden mit zusätzlichen Methoden zu
"umhüllen".

Der wohl typischste Dekorator 

.. _Generatoren und Iteratoren:
.. _Generator:
.. _Iterator:

Generatoren und Iteratoren
--------------------------

Generatoren sind Objekte, die über eine ``__next__()``-Funktion verfügen, also
bei jedem Aufruf von ``next(generator_object)`` einen neuen Rückgabewert
liefern. Man kann sich einen Generator also vorstellen wie eine Funktion, die
mit jedem Aufruf das nächste Element einer Liste zurückgibt. Kann der Generator
keinen weiteren Rückgabewert liefern, wird ein ``StopIteration``-Error
ausgelöst.

Der Vorteil von Generatoren gegenüber Listen liegt darin, dass auch bei sehr
großen Datenmengen kein großer Speicherbedarf nötig ist, da immer nur das
jeweils aktuell zurückgegebene Objekt im Speicher existiert. Beispielsweise
handelt es sich auch bei :ref:`File <File>`-Objekten um Generatoren, die beim
Aufruf von ``next(fileobject)`` jeweils die nächste Zeile der geöffneten
ausgeben. Auf diese Weise kann der Inhalt einer (beliebig) großen Datei
beispielsweise mittels einer ``for``-Schleife abgearbeitet werden, ohne dass der
Inhalt der Datei auf einmal eingelesen und als Liste gespeichert werden muss.

Generatoren werden mit einer Syntax erzeugt, die der von :ref:`List
Comprehensions <List-Comprehension>` sehr ähnlich ist; es wird lediglich runde
Klammern anstelle der eckigen Klammern zur Begrenzung des Ausdrucks verwendet:

.. code-block:: python

    # List Comprehension:

    mylist = [i**2 for i in range(1,10)]

    mylist
    # Ergebnis: [1, 4, 9, 16, 25, 36, 49, 64, 81]

    # Generator:

    mygen  = (i**2 for i in range(1,10))

    next(mygen)
    # Ergebnis: 1

    next(mygen)
    # Ergebnis: 4

    # ...

Generatoren können auch verschachtelt auftreten; bestehende Generatoren können
also zur Konstruktion neuer Generatoren verwendet werden:

.. code-block:: python

    # Neuen Generator mittels eines existierenden erzeugen:

    mygen2 = (i**2 for i in mygen)

    next(mygen2)
    # Ergebnis: 81

    next(mygen2)
    # Ergebnis: 256

Python kann diese Art von verschachtelten Generatoren sehr schnell auswerten, so
dass Generatoren allgemein sehr gut für die Auswertung großer Datenströme
geeignet sind. Zu beachten ist lediglich, dass der Generator bei jedem Aufruf --
ähnlich wie eine Funktion -- einen Rückgabewert liefert, der von sich aus nicht 
im Speicher verbleibt, sondern entweder unmittelbar weiter verarbeitet oder
manuell gespeichert werden muss.




