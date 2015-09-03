.. index:: Modul
.. _Module:

Module und Pakete
=================

Module
------

Module bestehen, ebenso wie Python-Skript, aus Quellcode-Dateien mit der Endung
``.py``. Prinzipiell kann somit jedes Python-Skript als eigenständiges
Python-Modul angesehen werden, es existieren allerdings auch Module, die nur nur
aus Hilfsfunktionen bestehen.

In der Praxis werden Module allerdings in erster Linie verwendet, um den
Quellcode eines umfangreicheren Software-Projekts leichter zu organisieren und
übersichtlich zu halten. Eine grobe Regel besagt, dass ein Modul nur so
umfangreich sein sollte, dass sich seine Inhalte und sein Verwendungszweck mit
ein bis zwei Sätzen zusammenfassen lassen sollten.

Jedes Modul stellt einen eigenen Namensraum für Variablen dar, so dass
gleichnamige Funktionen, die in unterschiedlichen Modulen definiert sind, keine
Konflikte verursachen.

.. index:: import()

Modulnamen werden in Python allgemein in Kleinbuchstaben geschrieben. Um in das
aktuelle Programm ein externes Modul, also eine andere ``.py``-Datei, zu
integrieren, ist folgende Syntax üblich:

.. code-block:: python

    import modulname

    # Beispiel:

    import antigravity
    import this

Das zu importierende Modul muss sich hierbei im Python-Pfad befinden, also
entweder global installiert oder im aktuellen Verzeichnis enthalten sein.
Andernfalls ist eine Anpassung der Variablen ``sys.path`` nötig.

.. TODO Beispiel

.. _Verwendung von Modulen:

.. rubric:: Verwendung von Modulen

Nach dem Importieren eines Moduls können die im Modul definierten :ref:`Klassen
<Klassen und Objektorientierung>`, :ref:`Funktionen <Funktionen>` und
:ref:`Variablen <Variablen>` mit folgender Syntax aufgerufen werden:

.. code-block:: python

    modulname.Klassenname
    modulname.variablenname
    modulname.funktionsname()

Um bei längeren Modulnamen Schreibarbeit sparen zu können, ist beim
Importieren eines Moduls auch eine abkürzende Syntax möglich:

.. code-block:: python

    import modulname as myname

    # Beispiel:

    import math as m

Anschließend kann das Kürzel als Synonym für den Modulnamen verwendet werden,
beispielsweise ``m.pi`` anstelle von ``math.pi``.

Eine weitere Vereinfachung ist möglich, wenn man nur einzelne Klassen oder
Funktionen eines Moduls importieren möchte. Hierfür ist folgende Syntax
möglich:

.. code-block:: python

    from modulname import Klassenname   # oder
    from modulname import funktionsname

Dabei können auch mehrere Klassen- oder Funktionsnamen jeweils durch ein Komma
getrennt angegeben werden. Die so importieren Klassen bzw. Funktionen können
dann direkt aufgerufen werden, als wären sie in der aktuellen Datei definiert.

..
    .. rubric:: Wechselseitiges Importieren vermeiden

    Zwei Python-Dateien ``a.py`` und ``b.py`` können sich nicht gegenseitig
    importieren -- dies würde zu einer Endlosschleife führen:

    .. code-block:: python

    ..  # FEHLER-BEISPIEL!!

    ..  # Modul a.py:

    ..  import b

    ..  # Modul b.py

    ..  import a

    Der Python-Interpreter quittiert in diesem Fall unmittelbar mit einer
    Fehlermeldung. Um diesen Fehler zu umgehen, hilft nur eine Möglichkeit: Der
    Code, der von beiden Modulen zugleich benötigt wird, muss in eine weitere
    Datei ``c.py`` ausgelagert werden; diese kann dann mittels ``import c`` von
    den beiden Modulen ``a`` und ``b`` importiert werden.

.. _Hilfe zu Modulen:

.. rubric:: Hilfe zu Modulen

Mittels ``help(modulname)`` kann wiederum eine Hilfeseite zu dem jeweiligen
Modul eingeblendet werden, in der üblicherweise eine Beschreibung des Moduls
angezeigt wird und eine Auflistung der im Modul definierten Funktionen. Bei den
Standard-Modulen wird zudem ein Link zur entsprechenden Seite der offiziellen
Python-Dokumentation https://docs.python.org/3/ angegeben.


.. index:: __name__, __main__

.. rubric:: Die ``__name__``-Variable

Jedes Modul bekommt, wenn es importiert wird, automatisch eine
``__name__``-Variable zugewiesen, die den Namen des Moduls angibt. Wird
allerdings eine Python-Datei unmittelbar als Skript mit dem Interpreter
aufgerufen, so bekommt dieses "Modul" als ``__name__``-Variable den Wert
``__main__`` zugewiesen.

Wenn Python-Module importiert werden, dann werden sie einmalig vom Interpreter
ausgeführt, das heißt alle darin aufgelisteten Definitionen und Funktionsaufrufe
werden zum Zeitpunkt des Importierens (einmalig) aufgerufen. Möchte man einige
Funktionen in einer Python-Datei nur dann ausführen, wenn die Datei als Skript
aufgerufen wird, nicht jedoch, wenn sie als Modul in ein anderes Programm
eingebunden wird, so kann man dies mittels folgender Anweisung erreichen:

.. code-block:: python

    if __name__ == __main__:

        # execute this only if the current file is interpreted directly

Dies ist insbesondere für Mini-Programme nützlich, die wahlweise als
selbstständiges Programm aufgerufen, oder in ein anderes Programm eingebettet
werden können.

.. _Module erneut laden:

.. rubric:: Module erneut laden

Ist ein Modul einmal importiert, so wird jede weitere ``import``-Anweisung des
gleichen Moduls vom Python-Interpreter ignoriert. Dies ist in den meisten
Fällen von Vorteil, denn auch wenn beispielsweise mehrere Module eines
Programms das Modul ``sys`` importieren, so wird dieses nur einmal geladen.

Schreibt man allerdings selbst aktiv an einem Programmteil und möchte die
Änderungen in einer laufenden Interpreter-Sitzung (z.B. Ipython) übernehmen,
so müsste der Interpreter nach jeder Änderung geschlossen und neu gestartet
werden. Abhilfe schafft in diesem Fall die im Modul ``imp`` definierte Funktion
``reload()``, die ein erneutes Laden eines Moduls ermöglicht:

.. code-block:: python

    import imp
    import modulname

    # Modul neu laden:
    imp.reload(modulname)

Dies funktioniert auch, wenn ein Modul mit einer Abkürzung importiert wurde,
beispielsweise ``import modulname as m``; in diesem Fall kann das Modul mittels
``imp.reload(m)`` neu geladen werden.


.. _Pakete:

Pakete
------

Mehrere zusammengehoerende Module können in Python weiter in so genannten
Paketen zusammengefasst werden. Ein Paket besteht dabei aus einem einzelnen
Ordner, der mehrere Module (``.py``-Dateien) sowie stets eine Date
``__init__.py`` enthält. Diese Datei, die auch leer sein darf, enthält Code, der
einmalig beim Laden des Paketes ausgeführt wird.

Ein Programm kann somit in mehrere Teilpakete untergliedert werden, die wiederum
mittels der ``import``-Anweisung wie Module geladen werden können. Enthält
beispielsweise ein Paket ``pac`` die Module ``a`` und ``b``, so können diese
mittels ``import pac`` geladen und mittels ``pac.a`` beziehungsweise ``pac.b``
benutzt werden; zur Trennung des Paket- und des Modulnamens wird also wiederum
ein Punkt verwendet. Ebenso kann mittels ``import pac.a`` nur das Modul ``a``
aus dem Paket ``pac`` geladen werden.

Die ``import``-Syntax für Pakete lautet somit allgemein:

.. code-block:: python

    # Alle Module eines Pakets importieren:
    import paket

    # Oder: Einzelne Module eines Pakets importieren:
    import paket.modulname

    # Alternativ:
    from paket import modulname

Wird ein Modul mittels ``from paket import modulname`` importiert, so kann es
ohne Angabe des Paketnamens benutzt werden; beispielsweise können darin
definierte Funktionen mittels ``modulname.funktionsname()`` aufgerufen werden.
Eine weitere Verschachtelung von Paketen in Unterpakete ist ebenfalls möglich.


.. _Relative und absolute Pfadangaben:

.. rubric:: Relative und absolute Pfadangaben

Um Module aus der gleichen Verzeichnisebene zu importieren, wird in Python
folgende Syntax verwendet:

.. code-block:: python

    # Modul aus dem gleichen Verzeichnis importieren
    from . import modulname

Mit ``.`` wird dabei der aktuelle Ordner bezeichnet. Ebenso kann ein Modul
mittels ``from .. import modulname`` aus dem übergeordneten Verzeichnis und
mittels ``from ... import modulname`` aus dem nochmals übergeordneten
Verzeichnis importiert werden.


