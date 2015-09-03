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

Eine neue Klasse wird in Python mit dem Schlüssenwort ``class``, gefolgt vom
Klassennamen und einem Doppelpunkt eingeleitet. Alle darauf folgenden
Definitionen von Eigenschaften und Funktionen, die zur Klasse gehören, werden
um eine Tabulatorweite (üblicherweise 4 Leerzeichen) eingerückt.

.. rubric:: Definition und Initialisierung eigener Klassen

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

Im obigen Beispiel wurde zunächst die Klasse ``AlarmClock`` definiert und als
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

.. index:: __del__()

Möchte man eine konkrete Instanz wieder löschen, so ist dies mittels
``del(name_der_instanz)`` möglich, im obigen Fall also mit
``del(my_alarm_clock)``. Sollen bei der Löschung einer Instanz weitere Aufgaben
abgearbeitet werden, so können diese in einer optionalen Funktion ``__del__()``
innerhalb der Klasse festgelegt werden.

..
    ``__str()__`` als weitere besondere Funktion, liefert Zeichenkette mit
    Objekteigenschaften in gewuenschter Form ``__gt()__``, ``__eq()__``,
    ``__lt()__`` als Vergleichsoperatoren, um beispielsweise ein einzelnes
    Instanz-Attribut vergleichen; ebenso ``__le()__`` fuer < und ``__ne()__``
    fuer !=.
    ``__sub()__`` wird aufgerufen, wenn instanz1 - instanz2 eingegeben wird.
    Ebenso + __add()__, * __mul()__, ** __pow()__, / __truediv()__, //
    __floordiv()__, % __mod()__


