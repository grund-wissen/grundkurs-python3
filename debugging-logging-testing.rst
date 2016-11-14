
Debugging, Logging und Testing
==============================

Im folgenden Abschnitt werden Methoden vorgestellt, die beim Auffinden, Beheben
und Vermeiden von Fehlern hilfreich sind.


.. _pdb:

``pdb`` -- Der Python-Debugger
------------------------------

Ein Debugger wird verwendet, um ein fehlerhaftes Programm Schritt für Schritt
ablaufen zu lassen, um den Fehler schnell ausfindig machen zu können; er kann
ebenso verwendet werden, um die Funktionsweise ein unbekanntes Programms
leichter nachvollziehen zu können, indem man sieht, welche Funktionen im Laufe
des Programms nacheinander aufgerufen werden.

Der Python-Debugger ``pdb`` kann in einer Shell folgendermaßen aufgerufen
werden:

.. code-block:: sh

    pdb3 scriptfile.py

Nach dem Aufruf erscheint der ``pdb``-Eingabeprompt ``(Pdb)``. Hier können unter
anderem folgende Anweisungen eingegeben werden:

* ``help`` (oder kurz: ``h``):

  Mit ``help`` wird eine Übersicht über die wichtigsten Funktionen von ``pdb``
  angezeigt.

* ``step`` (oder kurz: ``s``):

  Mit ``step`` wird die aktuelle Zeile ausgeführt; der Debugger hält allerdings
  bei der nächst möglichen Stelle an (beispielsweise einem neuen
  Funktionsaufruf).

* ``p`` und ``pp``:

  Mit ``p`` wird der angegebene Ausdruck ausgewertet und das Ergebnis angezeigt;
  beispielsweise gibt ``p variablenname`` den Wert der angegebenen Variablen zum
  aktuellen Zeitpunkt im Programm an. Mit ``pp`` wird das Ergebnis in "pretty
  print"-Form ausgegeben.

* ``return`` (oder kurz: ``r``):

  Mit ``return`` wird das Programm bis zum Ende der aktuellen Funktion weiter
  ausgeführt.

* ``break`` (oder kurz: ``b``):

  Wird ``break`` ohne weiteres Argument aufgerufen, gibt es alle aktuellen
  Haltepunkte ("Breakpoints") und ihre laufende Nummer aus. Diese können
  ebenfalls mittels ``break`` manuell gesetzt werden:

  - Wird ``break`` mit einer ganzzahligen Nummer als Argument aufgerufen, so
    wird ein Breakpoint an dieser Stelle im Quellcode des Programms gesetzt; das
    heißt, der Debugger hält an, wenn diese Stelle erreicht wird.
  - Wird ``break`` mit einem Funktionsnamen als Argument aufgerufen, so wird ein
    Breakpoint bei dieser Funktion gesetzt, das heißt, der Debugger hält jedes
    mal an, wenn diese Funktion aufgerufen wird.

* ``clear`` (oder kurz: ``cl``):

  Mit ``clear nummer`` kann der Breakpoint mit der angegebenen Nummer wieder
  gelöscht werden.

* ``continue`` (oder kurz: ``c``):

  Mit ``continue`` wird das Programm bis zum Ende weiter ausgeführt, außer ein
  mit ``break`` gesetzter Breakpoint wird erreicht.

* ``run`` beziehungsweise ``restart``:

  Mit ``run`` beziehungsweise ``restart`` wird das zu debuggende Programm von
  Neuem gestartet. Wurde das Programm seit dem letzten Aufruf von ``pdb``
  verändert, wird es neu geladen; Breakpoints bleiben dabei erhalten.

* ``exit`` beziehungsweise ``quit``:

  Mit ``exit`` oder ``quit`` wird der Debugger beendet.

.. Debugging mit Ipython

.. index:: Logdatei
.. _Logdatei:
.. _Arbeiten mit Logdateien:

``logging`` -- Arbeiten mit Logdateien
--------------------------------------

Logdateien können ebenso wie ein Debugger genutzt werden, um Fehler in einem
Programm zu finden. Hierzu nutzt man im Quellcode des Programms Anweisungen, die
große Ähnlichkeit mit simplen ``print()``-Anweisungen haben. Die Ausgabe wird
allerdings üblicherweise nicht auf dem Bildschirm, sondern mit einer
Standard-Formatierung in eine Logdatei geschrieben. [#]_

In Python kann ein Logging einfach mit Hilfe des ``logging``-Moduls umgesetzt
werden. Beispielsweise kann man ein Logging in einer interaktiven
Interpreter-Sitzung folgendermaßen aktivieren:

.. code-block:: python

    import logging

    # Basis-Einstellungen festlegen:
    logging.basicConfig(level=logging.INFO)

    # Logger zur aktuellen Sitzung erstellen:
    logger = logging.getLogger(__name__)

    # Logger-Nachricht erzeugen:
    logger.info("Los geht's!")
    # Ergebnis:INFO:__main__:Los geht's!

Über die Angabe des Log-Levels wird festgelegt, wie dringlich eine Nachricht
ist. Im ``logging``-Modul sind dabei folgende Werte festgelegt:

+----------+----+
| CRITICAL | 50 |
+----------+----+
| ERROR    | 40 |
+----------+----+
| WARNING  | 30 |
+----------+----+
| INFO     | 20 |
+----------+----+
| DEBUG    | 10 |
+----------+----+
| NOTSET   | 0  |
+----------+----+

Die einzelnen Stufen können mittels ``logger.info()``, ``logger.warning()``,
``logger.error()`` usw. unmittelbar genutzt werden. Ausgegeben werden derartige
Nachrichten immer dann, wenn ihr Dringlichkeitswert über dem in der
Basis-Einstellung festgelegten Level liegt.

Meist werden Logger nicht in interaktiven Interpreter-Sitzungen, sondern
innerhalb von Quellcode-Dateien in Verbindung mit einer Logdatei genutzt.
Hierfür kann die Basis-Konfiguration beispielsweise so aussehen:

.. code-block:: python

    import logging

    import modul1
    import modul2

    # Basis-Einstellungen festlegen:
    logging.basicConfig(filename='logdatei.log',
                        format='%(levelname)s: %(message)s',
                        level=logging.DEBUG)

    # Logger-Nachricht erzeugen:
    logger.info("Los geht's!")

In diesem Fall wurden bei der Festlegung der Basis-Einstellungen zusätzlich eine
Logdatei und eine Standardfomat angegeben. Wird das Programm aufgerufen, so wird
hierdurch in der angegebenen Logdatei folgender Eintrag erzeugt::

    INFO: Los geht's!

Wird die obige Konfiguration in der Basis-Datei eines Programms vorgenommen, das
als Ankerpunkt für weitere Module dient, so genügt innerhalb dieser Module
bereits die Anweisung ``import logging`` zu Beginn der jeweiligen Datei, um
innerhalb des Moduls ebenfalls mittels ``logger.info(nachricht)`` Einträge in
die Logdatei des Basis-Programms schreiben zu können.

Da mittels Lognachrichten auch, ebenso wie mit :ref:`print() <Formatierung von
Zeichenketten>`, Variablenwerte ausgegeben werden können, kann die Verwendung
von Logdateien in vielen Fällen sogar einen Debugger ersetzen.


.. index:: Doctest
.. _Doctest:

``doctest`` -- Testen mittels Docstrings
----------------------------------------

Zu Beginn eines jeden Funktionsblocks sollte mittels dreifachen Anführungszeichen
ein kurzer :ref:`Docstring <Docstring>` geschrieben werden, welcher eine kurze
Beschreibung der Funktion enthält. Ein solcher Docstring kann ebenfalls ein
kurzes Code-Beispiel enthalten, wie die Funktion angewendet wird und welches
Ergebnis die Funktion liefert.

.. code-block:: python

    def power(base, n):
        """
        Berechne die n-te Potenz des Basis-Werts.

        >>> power(5, 3)
        125

        :param base: Basiswert  (int oder float)
        :param n:    Exponent   (int oder float)
        :returns:    Potenzwert (int oder float)
        """
        return base ** n

.. TODO besseres Beispiel

Beim Schreiben von Doctests werden Zeilen, die normalerweise direkt im
Python-Interpreter eingegeben werden, mit ``>>>`` eingeleitet; in der
darauffolgenden Zeile wird dann eingegeben, welches Ergebnis beim Aufruf der
vorherigen Zeile erwartet wird. Stimmt beim Durchlaufen der Doctests ein
tatsächliches Ergebnis nicht mit dem erwarteten Ergebnis überein, so schlägt der
jeweilige Test fehl, und eine entsprechende Fehlermeldung wird angezeigt.

Das Schreiben von so gestalteten Docstrings macht einerseits Code
nachvollziehbarer; andererseits die integrierten Code-Beispiele auch ein Testen
der jeweiligen Funktionen. Dazu muss das Paket ``doctest`` importiert werden.
Bei einem Modul, das ausschließlich Hilfsfunktionen enthält (also üblicherweise
nur importiert, aber nicht ausgeführt wird, kann folgende Syntax verwendet
werden:

.. code-block:: python

    if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=1)

Werden diese Zeilen an das Ende des zu testenden Moduls geschrieben, so kann man
anschließend ``python3 modulname.py`` aufrufen, um die Tests zu aktivieren; wird
Das Modul hingegen nur importiert, so wird der Code-Abschnitt ignoriert.

Alternativ können Doctests auch direkt durch den Aufruf des Interpreters
aktiviert wrden:

.. code-block:: sh

    python3 -m doctest modulname.py -v

Hierbei wird mittels der Interpreter-Option ``-m`` das ``doctest``-Modul
geladen, zudem werden mittels der Option ``-v`` ("verbose") ausführliche
Ausgabe-Informationen angezeigt.

Doctests eignen sich nur für verhältnismäßig einfache Tests, in denen nur eine
geringe Anzahl von Tests je Funktion durchgeführt werden und auch keine
umfangreiche Vorbereitung der Einsatz-Umgebung notwendig ist; dies würde die
Docstrings allzu umfangreich und die Code-Dateien damit zu unübersichtlich
machen. Eine bessere Alternative bieten an dieser Stelle Unit-Tests.

.. index:: Unittest
.. _unittest:

``unittest`` -- Automatisiertes Testen
--------------------------------------

Beim Schreiben von Unit-Tests mit Hilfe des ``unittest``-Pakets wird zu jedem
Modul ``modulname.py`` ein entsprechendes Test-Modul ``test_modulname.py``, mit
dessen Hilfe welche die im Hauptmodul enthaltenen Funktionen getestet werden
können. Alle diese so genannten Unit Tests sollten voneinander unabhängig sein.

Da manche Funktionen oder Module im normalen Betrieb eine bestimmte Umgebung
benötigen, beispielsweise einen aktiven Webserver, eine Datenbank, oder eine
geöffnete Beispieldatei, können innerhalb der Test-Module mittels der Funktionen
``setup()`` und ``teardown()`` solche Umgebungen bereitgesetellt werden; diese
beiden Funktionen werden bei jedem Test aufgerufen und erzeugen beziehungsweise
bereinigen die benötigte Umgebung.

Ein Test-Funktionen einer Unitt-Test-Datei beginnen jeweils mit mit ``test_``,
gefolgt vom Namen der zu testenden Funktion. Um Klassen zu testen, werden in der
Unit-Test-Datei ebenfalls Klassen definiert, deren Namen sich aus der
Zeichenkette ``Test_`` und und den eigentlichen Klassennamen zusammensetzt.
Diese Klassen haben ``unittest.TestCase`` als Basisklasse.

Eine Unit-Test-Klasse kann somit etwa folgenden Aufbau haben:

.. code-block:: python

    import unittest
    from modulname import KlassenName

    class Test_KlassenName(unittest.TestCase):

        def setUp(self):
            pass

        def test_funktionsname1(self):
            ...

        def test_funktionsname2(self):
            ...

        ...

        def tearDown(self):
            pass


Die einzelnen Test-Funktionen enthalten -- neben möglichen
Variablen-Definitionen oder Funktionsaufrufen -- stets so genannte Assertions,
also "Behauptungen" oder "Hypothesen". Hierbei wird jeweils geprüft, ob das
tatsächliche Ergebnis einer ``assert``-Anweisung mit dem erwarteten Ergebnis
übereinstimmt. Ist dies der Fall, so gilt der Test als bestanden, andererseits
wird ein ``AssertionError`` ausgelöst.

In Python gibt es, je nach Art der Hypothese, mehrere mögliche
``assert``-Anweisungen:

* Mit ``assertEqual(funktion(), ergebnis)`` kann geprüft werden, ob der
  Rückgabewert der angegebenen Funktion mit dem erwarteten Ergebnis
  übereinstimmt.
* Mit ``assertAlmostEqual(funktion(), ergebnis)`` kann bei numerischen
  Auswertungen geprüft werden, ob der Rückgabewert der angegebenen Funktion bis
  auf Rundungs-Ungenauigkeiten mit dem erwarteten Ergebnis übereinstimmt.
* ...

Um Unit-Tests zu starten, kann die Test-Datei am Ende um folgende Zeilen ergänzt
werden:

.. code-block:: python

    if __name__ == '__main__':
        unittest.main()

Gibt man dann ``python3 test_modulname.py`` ein, so werden durch die Funktion
``unittest.main()`` alle in der Datei enthaltenen Tests durchlaufen. Als
Ergebnis wird dann angezeigt, wieviele Tests erfolgreich absolviert wurden und
an welcher Stelle gegebenenfalls Fehler aufgetreten sind.

.. _Test-Automatisierung mit nose:

.. rubric:: Test-Automatisierung mit ``nose``

Das Programm ``nose`` vereinfacht das Aufrufen von Unit-Tests, da es automatisch
alle Test-Funktionen aufruft, die es im aktuellen Verzeichnis mitsamt aller
Unterverzeichnisse findet; eine Test-Funktion muss dazu lediglich in ihrem
Funktionsnamen die Zeichenkette ``test`` enthalten.

Um Tests mittels ``nose`` zu finden und zu aktivieren, genügt es in einer Shell in
das Test-Verzeichnis zu wechseln und folgende Zeile einzugeben:

.. code-block:: sh

    nosetest3

Bei Verwendung von ``nose`` erübrigt sich also das Schreiben von Test-Suits.
Wird ``nosetests3 --pdb`` aufgerufen, so wird automatisch der Python-Debugger
``pdb`` gestartet, falls ein Fehler auftritt.

.. fixtures
.. pdb bei fehlern
.. coverage


.. tox und py.test


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Gegenüber einfachen ``print()``-Anweisungen, die ebenfalls beispielsweise
    zur Ausgabe von Variablenwerten zu einem bestimmten Zeitpunkt genutzt werden
    können, haben Logger als Vorteil, nach dem 'Debuggen' zwingend wieder aus
    dem Code entfernt werden zu müssen; zudem stehen für Logger verschiedene
    Dringlichkeits-Stufen zur Verfügung, so dass die Ausgabe der
    Logging-Nachrichten nur dann erfolgt, wenn die jeweilige Stufe (mittels
    einer Einstellung) aktiviert wird.


