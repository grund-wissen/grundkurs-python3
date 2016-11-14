.. _Fehler und Ausnahmen:

Fehler und Ausnahmen
====================

Fehler gehören für Programmierer zum Alltag: Komplexe Computerprogramme laufen
nur selten fehlerfrei, schon gar nicht in der Entwicklungsphase. Die möglichen
auftretenden Fehler lassen sich allgemein in drei Arten unterteilen:

.. _Arten von Programm-Fehlern:

Arten von Programm-Fehlern
--------------------------

* **Syntax-Fehler** bewirken, dass ein Programm aufgrund eines
  "Grammatik-Fehlers" vom Computer nicht in ausführbaren Maschinencode übersetzt
  werden kann. Derartige Fehler können aus unvollständigen Klammerpaaren,
  fehlenden Doppelpunkt-Zeichen am Ende einer ``if``-Bedingung, ungültige Zeichen
  oder ähnlichem bestehen.

  Enthält ein Programm Syntax-Fehler, so werden diese beim Versuch eines
  Programmaufrufs angezeigt, und das Programm startet nicht.

  Die zwei geläufigsten Syntax-Checker für Python-Code sind `pylint
  <https://pylint.org>`_ und `pyflakes <https://pypi.python.org/pypi/pyflakes>`_;
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

Optional kann neben einer ``try`` und einer beziehungsweise mehreren
``except``-Anweisungen auch eine ``else``-Anweisung angegeben werden, die genau
dann ausgeführt wird, wenn die ``try``-Anweisung *keinen* Fehler ausgelöst hat:

.. code-block:: python

    try:
        # Diese Anweisung kann einen FileNotFoundError auslösen:
        file = open('/tmp/any_file.txt')

    except FileNotFoundError:
        print("Datei nicht gefunden!")

    except IOError:
        print("Datei nicht lesbar!")

    else:
        # Datei einlesen, wenn kein Fehler augetreten ist:
        data = file.read()

    finally:
        # Diese Anweisung in jedem Fall ausführen:
	    file.close()

Zusätzlich zu ``try`` und ``except`` kann man optional auch einen
``finally``-Block angeben; Code, der innerhalb von diesem Block steht, wird auf
alle Fälle am Ende der Ausnahmebehandlung ausgeführt, egal ob der ``try``-Block
fehlerfrei ausgeführt wurde oder eine Exception aufgetreten ist.

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

