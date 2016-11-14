.. index:: Ipython (IDE)
.. _ipython:
.. _ipython -- eine Python-Entwicklungsumgebung:

``ipython`` -- eine Python-Entwicklungsumgebung
===============================================

`Ipython <https://ipython.org/>`__ ist ein Interpreter-Frontend, das vielerlei
nützliche Features zum interaktiven Entwickeln von Python-Projekten bietet. Er
kann durch das gleichnamige Paket installiert werden:

.. code-block:: bash

    sudo aptitude install ipython3 ipython3-qtconsole ipython3-notebook

Die beiden letzten Pakete ermöglichen es, Ipython mit einer graphischen
Oberfläche oder als Anwendung in einem Webbrowser zu starten. Nach der
Installation kann das Programm in einer Shell mittels ``ipython3`` oder als
graphische Oberfläche mittels ``ipython3 qtconsole`` aufgerufen werden.

Gibt man in Ipython einen Python-Ausdruck ein und drückt ``Enter``, so wird
dieser ausgewertet. Besteht der Ausdruck beispielsweise aus einem einzelnen
Variablennamen, so wird eine String-Version dieser Variablen ausgegeben.


.. _Navigationshilfen:

Navigationshilfen
-----------------

Ipython bietet gegenüber dem normalen Python-Interpreter für ein interaktives
Arbeiten am Quellcode nicht nur ein Syntax-Highlighting, sondern auch folgende
Funktionen:


.. _Tab-Vervollständigung:

.. rubric:: Tab-Vervollständigung

Während man einen Python-Ausdruck oder einen Dateinamen schreibt, kann man
diesen durch Drücken der ``Tab``-Taste vervollständigen. Gibt es mehrere
Möglichkeiten zur Vervollständigung, so werden diese aufgelistet; bei Nutzung der
Qt-Konsole kann zwischen den einzelnen Möglichkeiten durch erneutes Drücken von
``Tab`` gewechselt und die Auswahl mit ``Enter`` bestätigt werden.

Gibt man einen Modulnamen ein, gefolgt von ``.``, so werden durch Drücken von
``Tab`` alle Funktionen des Moduls aufgelistet; Attributs- und Funktionsnamen,
die mit ``_`` oder ``__`` beginnen, werden allerdings als "privat" gewertet und
ignoriert. Gibt man zusätzlich den einleitenden Unterstrich ein, so lassen auch
diese Attributs- beziehungsweise Funktionsnamen mit ``Tab`` auflisten und
vervollständigen.


.. _Weitere Tastenkürzel:

.. rubric:: Weitere Tastenkürzel

In Ipython erleichtern folgende weitere Tastenkürzel das Arbeiten:

Navigation:

* ``Ctrl u`` Lösche die aktuelle Zeile
* ``Ctrl k`` Lösche vom Cursor bis zum Ende der aktuellen Zeile
* ``Ctrl a`` Gehe an den Anfang der aktuellen Zeile
* ``Ctrl e`` Gehe ans Ende der aktuellen Zeile

Code-History:

* :math:`\uparrow`: History rückwärts durchsuchen
* :math:`\downarrow`: History vorwärts durchsuchen
* ``Ctrl`` :math:`\uparrow`: History rückwärts nach Aufruf durchsuchen, der
  genauso beginnt wie der aktuell eingegebene Text
* ``Ctrl`` :math:`\downarrow`: History vorwärts nach Aufruf durchsuchen, der
  genauso beginnt wie der aktuell eingegebene Text
* ``Ctrl r``: History rückwärts nach Aufrufen durchsuchen, die den eingegebenen
  Text als Muster beinhalten

Die letzten drei eingegeben Code-Zeilen können in Ipython zudem über die
Variablen ``_``, ``\__`` und ``\___`` referiert werden.

Startet man Ipython mittels ``ipython3`` als Shell-Anwendung, so kann (abhängig
von den Einstellungen des jeweiligen Shell-Interpreters) nur begrenzt weit
"zurück scrollen". Ruft man in Ipython Funktionen auf, die eigentlich sehr lange
Ausgaben auf dem Bildschirm erzeugen würden, so kann man diese unterdrücken,
indem man an die Anweisung ein ``;`` anhängt. Dies hat keine Auswirkung auf die
Anweisung selbst, hilft aber dabei, die Interpreter-Sitzung übersichtlich zu
halten.


.. _Informationen zu Objekten:

.. rubric:: Informationen zu Objekten

Gibt man vor oder nach einem Variablennamen ein ``?`` an, so werden
ausführliche Informationen zur jeweiligen Variable angezeigt. Setzt man das
Fragezeichen vor oder nach einen Funktions- oder Klassennamen, so wird auch der
Docstring der jeweiligen Funktion oder Klasse angezeigt:

::

    print?

.. code-block:: python

    # Ergebnis:
    # Type:        builtin_function_or_method
    # String form: <built-in function print>
    # Namespace:   Python builtin
    # Docstring:
    # print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    # Prints the values to a stream, or to sys.stdout by default.
    # Optional keyword arguments:
    # file:  a file-like object (stream); defaults to the current sys.stdout.
    # sep:   string inserted between values, default a space.
    # end:   string appended after the last value, default a newline.
    # flush: whether to forcibly flush the stream.

Schreibt man ``??`` anstelle von ``?``, so wird zusätzlich der Quellcode des
jeweiligen Objekts angezeigt.

.. todo docstring popup-fenster in qtconsole

.. _magic-Funktionen:
.. _magic:

``magic``-Funktionen
--------------------

In Ipython ist es möglich, einige zusätzliche Funktionen aufzurufen; diese nur
in Ipython-Sitzungen definierten Funktionen werden als ``magic``-Funktionen
bezeichnet und mit ``%`` bzw. ``%%`` eingeleitet. Mittels ``%lsmagic`` werden
beispielsweise alle derartigen Funktionen aufgelistet:

.. code-block:: python

    %lsmagic

.. code-block:: python

    # Ergebnis:

    # Available line magics:
    # %alias  %alias_magic  %autocall  %autoindent  %automagic  %bookmark  %cd
    # %colors  %config  %cpaste  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit
    # %env  %gui  %hist  %history  %install_default_config  %install_ext
    # %install_profiles  %killbgscripts  %load  %load_ext  %loadpy  %logoff
    # %logon  %logstart  %logstate  %logstop  %lsmagic  %macro  %magic
    # %matplotlib  %notebook  %page  %paste  %pastebin  %pdb  %pdef  %pdoc  %pfile
    # %pinfo  %pinfo2  %popd  %pprint  %precision  %profile  %prun  %psearch
    # %psource  %pushd  %pwd  %pycat  %pylab  %quickref  %recall  %rehashx
    # %reload_ext  %rep  %rerun  %reset  %reset_selective  %run  %save  %sc
    # %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who
    # %who_ls  %whos  %xdel  %xmode

    # Available cell magics:
    # %%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html  %%javascript
    # %%latex  %%perl  %%prun  %%pypy  %%python  %%python3  %%ruby  %%script  %%sh
    # %%svg  %%sx  %%system  %%time  %%timeit  %%writefile

Im folgenden werden einige der ``magic``-Funktionen kurz vorgestellt.


.. _Magic-Funktionen automatisch erkennen:

.. rubric:: Magic-Funktionen automatisch erkennen

Durch eine Eingabe von ``%automagic`` im Ipython-Interpreter werden im Verlauf
der Sitzung die Namen der Magic-Funktionen in den globalen Namensraum
aufgenommen. Im folgenden kann damit wahlweise ``pwd`` oder ``%pwd``

eingegeben werden, um den Namen des aktuellen Arbeitsverzeichnisses anzuzeigen;
das beziehungsweise die ``%``-Zeichen können anschließend also weggelassen werden.


.. _Zeilen und Zellen:

.. rubric:: Zeilen und Zellen

Ipython kennt -- ebenso wie der Standard-Python-Interpreter -- zwei Arten von
Anweisungen: Zum einen "simple" einzeilige Anweisungen, zum anderen
"zusammengesetzte" Anweisungen, die aus mehreren Zeilen bestehen. In Ipython
wird eine solche Block-Anweisung, die stets mit einer leeren Zeile endet, auch
als "Zelle" bezeichnet.

Die ``line magic``-Funktionen beziehen sich auf eine einzelne, einzeilige
Anweisung; den ``cell magic``-Funktionen werden hingegen der jeweiligen
Anweisung weitere Zeilen angefügt. Beispielsweise kann mittels ``%% writefile
dateiname`` der unmittelbar folgenden Text (ohne Anführungszeichen!) in eine
Datei geschrieben werden, bis die Eingabe durch ein zweimaliges Drücken von
``Enter`` beendet wird.

::

    %%writefile test.txt
    Hallo
    Welt!


.. code-block:: python

    #Ergebnis: Writing tmp.txt

Mittels ``%%writefile -a`` wird der folgende Text an die angegebene Datei
angehängt; eine Eingabe von leeren Zeilen oder von formatiertem Text ist so
allerdings nicht möglich, die unmittelbar folgende Texteingabe wird "as it is"
geschrieben.

.. _cpaste:
.. _Code via Copy-und-Paste einfügen:

.. rubric:: Code via Copy-und-Paste einfügen

Versucht man einen ganzen Code-Block per Copy-und-Paste einzufügen, so kann es
zu einer Fehlermeldung kommen, wenn der Block leere Zeilen enthält: Ipython
sieht an dieser Stelle die Eingabe der "Zelle" als beendet an und beginnt die
nächste (die dann meist eine falsche Einrückung aufweist).

Um dieses Problem zu umgehen, kann man die Magic-Funktion ``%cpaste`` aufrufen:
Anschließend wird der gesamte (beispielsweise mittels ``Paste``) eingefügte Text
als eine einzige Eingabe-Zelle interpretiert -- bis ``Ctrl d`` gedrückt wird,
oder eine Textzeile eingegeben wird, die lediglich die Zeichenkette ``--``
enthält.

Auf diese Weise kann man beispielsweise :ref:`Vim <gwl:Vim>` mit dem Plugin
:ref:`Vicle <gwl:Vicle>` als Editor verwenden und von dort aus Code an einen
Ipython-Shell-Interpreter senden.

.. _Python-Skripte aufrufen:

.. rubric:: Python-Skripte aufrufen

Python-Skripte lassen sich folgendermaßen vom Ipython-Interpreter aus aufrufen:

.. code-block:: python

    %run path/script.py [arguments]

Befindet man sich bereits im Pfad der Programmdatei oder wechselt mittels
``os.chdir(path)`` dorthin, so kann die Pfadangabe im obigen Aufruf weggelassen
werden.

Der obige Aufruf entspricht dem üblichen Aufruf von ``python3 path/script.py``
in einer Shell. Benötigt das Skript gegebenenfalls weitere Argumente, so können
diese im Anschluss an die Pfadangabe des Skripts angegeben werden. Ist das
aufgerufene Skript fehlerhaft und/oder benötigt es zu lange zur Ausführung, so
kann es mit ``Ctrl c`` unterbrochen werden (KeyboardInterrupt).

Ein Vorteil der ``%run``-Anweisung liegt darin, dass alle im aufgerufenen Skript
definierten Variablen und Funktionen importiert und anschließend in der
interaktiven Sitzung genutzt werden können (als wären sie direkt eingeben
worden). Ein weiterer Vorteil liegt darin, dass beim Aufruf von ``run``
zusätzliche Optionen angegeben werden können:

* Mit ``%run -t`` ("timer") wird die Laufzeit des Python-Skript in Kurzform
  dargestellt.

  Der Timer listet auf, wie viel Zeit beim Ausführen des Skripts für
  System-Aufrufe, wie viel auf benutzerspezifische Rechenschritte und wie viel
  Gesamt benötigt wurde.

* Mit ``%run -t`` ("profiler") wird die Laufzeit der einzelnen im Python-Skript
  aufgerufenen Anweisungen detailliert dargestellt.

  Der Profiler listet dabei auf, wie häufig eine Funktion aufgerufen wurde und
  wie viel Zeit dabei je Ausführung beziehungsweise insgesamt benötigt wurde.

* Mit ``%run -d`` ("debugger") wird das Programm im Python-Debugger ``pdb``
  gestartet.

  Der Debugger durchläuft das Programm Anweisung für Anweisung und hält dabei an
  vorgegebenen Breakpoints oder bei nicht abgefangenen Exceptions; man kann sich
  dann beispielsweise die Werte von Variablen anzeigen lassen, die für den
  auftretenden Fehler verantwortlich sein können.

.. _Debugging:

.. rubric:: Debugging

Anstelle ein Python-Skript mittels ``%run -d script.py`` von Anfang an im
Debugger zu starten, kann man in Ipython mittels ``%debug`` einen allgemeinen
Debug-Modus aktivieren. In diesem Fall wird der Debugger automatisch gestartet,
wenn eine nicht abgefangene Exception auftritt.


.. _Interaktion mit der Shell:

.. rubric:: Interaktion mit der Shell

Im Ipython-Interpreter lassen sich Shell-Anweisungen ausführen, indem man diesen
ein ``!`` voranstellt; beispielsweise listet ``!ls`` den Inhalt des aktuellen
Verzeichnisses auf. Gibt man ``files = !ls`` ein, so wird die Ausgabe der
Shell-Anweisung ``ls`` als Liste in der Python-Variablen ``files`` gespeichert.

Umgekehrt kann man den Inhalt von Python-Variablen an die Shell-Anweisung
übergeben, indem man der Variablen ein ``$``-Zeichen voranstellt. Man könnte
also ``!echo "$files`` eingeben, um die in der Variablen ``files`` gespeicherten
Inhalte mittels :ref:`echo <gwl:echo>` auszugeben.


.. _Konfigurationen:

Konfigurationen
---------------

Eigene Konfigurationen lassen sich in Ipython mittels so genannter "Profile"
festlegen. Auf diese Weise kann beispielsweise festgelegt werden, welche
Module beim Start von Ipython automatisch geladen oder welche Variablen
standardmäßig definiert werden sollen; die Ipython-Profile ermöglichen darüber
hinaus weitere Möglichkeiten, das Aussehen und Verhalten des Interpreters zu
steuern.

Ein neues Profil kann folgendermaßen erstellt werden:

.. code-block:: sh

    # Profil "default" erstellen:
    ipython3 profile create

    # Profil "profilname" erstellen:
    ipython3 profile create profilname

Hierdurch wird das Profil mit dem angegebenen Namen im Verzeichnis
``~/.ipython`` neu angelegt; lässt man den Profilnamen weg, so wird das Profil
automatisch ``default`` genannt. Bei künftigen Sitzungen wird, sofern vorhanden,
das Profil ``default`` automatisch geladen, außer man wählt startet Ipython
explizit mit dem angegebenen Profilnamen:

.. code-block:: sh

    # Ipython mit "default"-Profil starten:
    ipython3

    # Ipython mit "profilname"-Profil starten:
    ipython3 --profile=profilname

Durch das Erstellen eines Profils wird im Verzeichnis
``~/.ipython/profile_default`` (oder einem entsprechenden Profilnamen) 
automatisch ein Satz Konfigurationsdateien erstellt. Die wichtigsten
Konfigurationsdateien sind:

* ``ipython_qtconsole_config.py``: Diese Datei wird aufgerufen, wenn Ipython
  mittels ``ipython3 qtconsole``, also mit graphischer QT-Console gestartet
  wird.
* ``ipython_notebook_config.py``: Diese Datei wird aufgerufen, wenn Ipython
  mittels ``ipython3 notebook``, also als Webanwendung gestartet wird.
* ``ipython_config.py``: Diese Datei wird *immer* aufgerufen, wenn Ipython mit
  dem angegebenen Profil gestartet wird.

Alle Konfigurationen enthalten sämtliche Einstellungsoptionen mitsamt der
zugehörigen Beschreibungen in Kommentarform; um eine Einstellung vorzunehmen, muss
also nur das Kommentarzeichen am Anfange der jeweiligen Zeile entfernt und der
Konfig-Variable der gewünschte Wert zugewiesen werden.

Abgesehen von vielen zusätzlichen Kommentaren kann eine Konfigurationsdatei
somit beispielsweise folgendermaßen aussehen:

.. code-block:: python

    # sample ipython_config.py
    # Configuration file for ipython.

    c = get_config()

    # lines of code to run at IPython startup.
    c.InteractiveShellApp.exec_lines = [
        'import math as m',
        'import sympy as sy',
        ]

    # Autoindent IPython code entered interactively.
    c.InteractiveShell.autoindent = True

    # Enable magic commands to be called without the leading %.
    c.TerminalInteractiveShell.automagic = True

    c.TerminalInteractiveShell.history_length = 10000


Die einzelnen Optionen können bei Bedarf auch innerhalb einer laufenden Sitzung
geändert werden; hierzu muss man lediglich eine Anweisung der Form ``%config
InteractiveShell.autoindent = True`` eingeben.


.. todo DEMO-Funktion https://ipython.org/ipython-doc/2/interactive/reference.html#interactive-demos
.. todo EMBEDDING Ipython https://ipython.org/ipython-doc/2/interactive/reference.html
.. todo Ipythen Kernel -> Debugging

Weitere Infos zu Ipython gibt es in der offiziellen `Dokumentation (en.)
<https://ipython.org/ipython-doc/2/index.html>`__.


