.. _Fehler, Ausnahmen, Debugging und Tests:

Fehler, Ausnahmen, Debugging und Tests
======================================

Fehler gehören für Programmierer zum Alltag: Komplexe Computerprogramme laufen
nur selten fehlerfrei, schon gar nicht in der Entwicklungsphase. Die möglichen
auftretenden Fehler lassen sich allgemein in drei Arten unterteilen:

* **Syntax-Fehler** bewirken, dass ein Programm aufgrund eines
  "Grammatik-Fehlers" vom Computer nicht in ausführbaren Maschinencode übersetzt
  werden kann. Derartige Fehler können aus unvollständigen Klammerpaaren,
  fehlenden Doppelpunkt-Zeichen am Ende einer ``if``-Bedingung, ungültige Zeichen
  oder ähnlichem bestehen.

  Enthält ein Programm Syntax-Fehler, so werden diese beim Versuch eines
  Programmaufrufs angezeigt, und das Programm startet nicht.

  Die zwei geläufigsten Syntax-Checker für Python-Code sind `pylint
  <http://pylint.org>`_ und `pyflakes <https://pypi.python.org/pypi/pyflakes>`_;
  zudem gibt es einen "Style"-Checker namens `pep8
  <https://pypi.python.org/pypi/pep8>`_, der prüft, ob die offiziellen
  Empfehlung für das Aussehen von Python-Code eingehalten werden (beispielsweise
  keine Zeilen mit mehr als 80 Zeichen auftreten). Diese zusätzlichen Werkzeuge
  können folgendermaßen installiert werden:

  .. code-block:: sh

      pip3 install pylint
      pip3 install pyflakes
      pip3 install pep8

  Gibt man nach der Installation ``pylint skriptname.py`` ein, so werden
  einerseits darin möglicherweise enthaltene Syntax-Fehler aufgelistet,
  andererseits werden Empfehlungen zur Verbesserung der Code-Syntax gegeben --
  unter anderem wird darauf hingewiesen, wenn eine Funktionsdefinition keinen
  Docstring enthält.

  Gibt man ``pep8 skriptname.py`` ein, so werden ebenfalls
  Verbesserungsvorschläge angezeigt, wie der enthaltene Python-Code in einer
  besser lesbaren Form geschrieben werden kann.

.. PEP8 Syntax-Konvention für gut lesbaren Code...
.. ``pip3 install pep8``
.. ``pep8 scriptname.py``

* **Laufzeit-Fehler** treten auf, wenn ein Programm versucht, eine ungültige
  Operation durchzuführen, beispielsweise eine Division durch Null oder ein
  Öffnen einer nicht vorhandenen Datei. Laufzeit-Fehler treten also erst auf,
  wenn das Programm (in der Regel ohne Fehlermeldung) bereits läuft.

  Laufzeit-Fehler können in Python allgemein mittels :ref:`try-except
  <try>`-Konstrukten abgefangen werden.

* **Logische Fehler** treten auf, wenn ein Programm zwar (anscheinend)
  fehlerfrei funktioniert, jedoch andere Ergebnisse liefert als erwartet. Bei
  solchen Fehlern liegt das Problem also an einem Denkfehler des Programmierers.

  Logische Fehler sind oft schwer zu finden; am besten hilft hierbei ein
  Debugger, mit dem man den Programmablauf Schritt für Schritt nachvollziehen
  kann (siehe Abschnitt :ref:`pdb -- der Python-Debugger <pdb>`).

Tritt in einem Python-Programm ein Fehler auf, der nicht von einer
entsprechenden Routine abgefangen wird, so wird das Progarmm beendet und ein so
genannter "Traceback" angezeigt. Bei dieser Art von Fehlermeldung, die man von unten
nach oben lesen sollte, wird als logische Aufruf-Struktur angezeigt, welche
Funktion beziehungsweise Stelle im Programm den Fehler verursacht hat; für diese
Stelle wird explizit der Dateiname und die Zeilennummer angegeben.

.. index:: Ausnahme, try, except
.. _try:
.. _except:
.. _finally:
.. _try, except und finally:

``try``, ``except`` und ``finally`` -- Fehlerbehandlung
-------------------------------------------------------

Mit dem Schlüsselwort ``try`` wird eine Ausnahmebehandlung eingeleitet: Läuft
der ``try``-Block nicht fehlerfrei durch, so kann der Fehler mittels einer
``except``-Anweisung abgefangen werden; in diesem Fall werden alle Anweisungen
des jeweiligen ``except``-Blocks ausgeführt.

.. Beispiel

Zusätzlich zu ``try`` und ``except`` kann man optional auch einen
``finally``-Block angeben; Code, der innerhalb von diesem Block steht, wird auf
alle Fälle am Ende der Ausnahmebehandlung ausgeführt, egal ob der ``try``-Block
fehlerfrei ausgeführt wurde oder eine Exceptions aufgetreten ist.

.. _with:

.. rubric:: Das ``with``-Statement

Ausnahmebehandlungen sind insbesondere wichtig, wenn Dateien eingelesen oder
geschrieben werden sollen. Tritt nämlich bei der Bearbeitung ein Fehler auf, so
muss das ``file``-Objekt trotzdem wieder geschlossen werden. Mit einer
"klassischen" ``try``- und ``finally``-Schreibweise sieht dies etwa wie folgt
aus:

.. code-block:: python

    # Datei-Objekt erzeugen:
    myfile = open("filename.txt", "r")

    try:
        # Datei einlesen und Inhalt auf dem Bildschirm ausgeben:
        content = myfile.read()
        print(content)
    finally:
        # Dateiobjekt schließen:
        f.close()

Diese verhältnismäßig häufig vorkommende Routine kann kürzer und eleganter
auch mittels eines ``with``-Statements geschrieben werden:

.. code-block:: python

    with open("filename.txt", "r") as myfile:
        content = myfile.read()
        print(content)

Hierbei versucht Python ebenfalls, den ``with``-Block ebenso wie einen
``try``-Block auszuführen. Die Methode ist allerdings wesentlich
"objekt-orientierter": Durch die im ``with``-Statement angegebene Anweisung wird
eine Instanz eines Objekts erzeugt, in dem obigen Beispiel ein ``file``-Objekt;
innerhalb des ``with``-Blocks kann auf dieses Objekt mittels des hinter dem
Schlüsselwort ``as`` angegebenen Bezeichners zugegriffen werden.

In der Klasse des durch das ``with``-Statement erzeugten Objekts sollten die
beiden Methoden ``__enter__()`` und ``__exit()__`` definiert sein, welche
Anweisungen enthalten, die unmittelbar zu Beginn beziehungsweise am Ende des
``with``-Blocks aufgerufen werden. Beispielsweise besitzen ``file``-Objekte eine
``__exit__()``-Methode, in denen die jeweilige Datei wieder geschlossen wird.

.. TODO weiterer Anwendungsfall: Log-Datei mit ``__enter__()`` öffnen.

.. index:: raise
.. _raise:

.. rubric:: ``raise`` -- Fehler selbst auslösen

Mit dem Schlüsselwort ``raise`` kann eine Ausnahme an der jeweiligen Stelle im
Code selbst ausgelöst werden. Dies ist unter anderem nützlich, um bei der
Interpretation einer Benutzereingabe fehlerhafte Eingaben frühzeitig abzufangen.

Wird von einem Benutzer beispielsweise anstelle einer Zahl ein Buchstabe
eingegeben, so kann dies beim Aufruf der weiterverarbeitenden Funktion mit
großer Wahrscheinlichkeit zu Fehlern führen. Da der Fehler jedoch bei der
Eingabe entstanden ist, sollte auch an dieser Stelle die entsprechende
Fehlermeldung (ein ``ValueError``) ausgelöst werden.

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

.. index:: Unittests
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

