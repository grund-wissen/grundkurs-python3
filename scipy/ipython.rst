
``ipython`` -- ein komfortabler Python-Interpreter
==================================================

`Ipython <https://ipython.org/>`__ ist ein erweiterter Python-Interpreter zum
Entwickeln neuer Projekte. Er kann durch das gleichnamige Paket installiert
werden:

.. code-block:: bash

    sudo aptitude install ipython3 ipython3-qtconsole

Das zweite Paket ermöglicht es, Ipython als graphische Oberfläche zu starten.
Nach der Installation kann das Programm in einer Shell mittels ``ipython3`` oder
als graphische Oberfläche mittels ``ipython3 qtconsole`` aufgerufen werden.

Gibt man in Ipython einen Python-Ausdruck ein und drückt ``Enter``, so wird
dieser ausgewertet. Besteht der Ausdruck aus einem einzelnen Variablennamen, so
wird eine String-Version dieser Variablen ausgegeben.

.. _Navigationshilfen:

Navigationshilfen
-----------------

Ipython bietet gegenüber dem normalen Python-Interpreter neben einem
automatischen Syntax-Highlighting auch weitere

.. rubric:: Tab-Vervollständigung

Während man einen Python-Ausdruck oder einen Dateinamen schreibt, kann man
diesen durch Drücken der ``Tab``-Taste vervollständigen. Gibt es mehrere
Möglichkeiten zur Vervollständiung, so werden diese aufgelistet; bei Nutzung der
Qt-Konsole kann zwischen den einzelnen Möglichkeiten durch erneutes Drücken von
``Tab`` gewechselt und die Auswahl mit ``Enter`` bestätigt werden.

Gibt man einen Modulnamen ein, gefolgt von ``.``, so werden alle Funktionen des
Moduls aufgelistet. Funktionsnamen, die mit ``_`` oder ``__`` beginnen, werden
dabei als "privat" gewertet und ignoriert. Gibt man den einleitenden Unterstrich
ein, so lassen auch diese Funktionsnamen mit ``Tab`` vervollständigen.

.. rubric:: Weitere Tastenkürzel

In Ipython erleichtern folgende weitere Tastenkürzel das Arbeiten:

Navigation:

* ``Ctrl u`` Lösche die aktuelle Zeile
* ``Ctrl k`` Lösche vom Cursor bis zum Ende der aktuellen Zeile
* ``Ctrl a`` Gehe an den Anfang der aktuellen Zeile
* ``Ctrl e`` Gehe ans Ende der aktuellen Zeile

History:

* :math:`\uparrow`: History rückwärts durchsuchen
* :math:`\downarrow`: History vorwärts durchsuchen
* ``Ctrl`` :math:`\uparrow`: History rückwärts nach Aufruf durchsuchen, der
  genauso beginnt wie der aktuell eingegebene Text
* ``Ctrl`` :math:`\downarrow`: History vorwärts nach Aufruf durchsuchen, der
  genauso beginnt wie der aktuell eingegebene Text

..  * ``Ctrl r``: History rückwärts nach Aufrufen durchsuchen, die den
  ..  eingegebenen Text als Muster beinhalten

.. rubric:: Informationen zu Objekten

Gibt man vor oder nach einem Variablennamen ein ``?`` an, so werden
ausführliche Informationen zur jeweiligen Variable angezeigt. Setzt man das
Fragezeichen vor oder nach einen Funktions- oder Klassennamen, so wird auch der
Docstring der jeweiligen Funktion oder Klasse angezeigt. Schreibt man ``??``
anstelle von ``?``, so wird zusätzlich der Quellcode des jeweiligen Objekts
angezeigt.

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

    Available line magics:
    %alias  %alias_magic  %autocall  %autoindent  %automagic  %bookmark  %cd
    %colors  %config  %cpaste  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit
    %env  %gui  %hist  %history  %install_default_config  %install_ext
    %install_profiles  %killbgscripts  %load  %load_ext  %loadpy  %logoff
    %logon  %logstart  %logstate  %logstop  %lsmagic  %macro  %magic
    %matplotlib  %notebook  %page  %paste  %pastebin  %pdb  %pdef  %pdoc  %pfile
    %pinfo  %pinfo2  %popd  %pprint  %precision  %profile  %prun  %psearch
    %psource  %pushd  %pwd  %pycat  %pylab  %quickref  %recall  %rehashx
    %reload_ext  %rep  %rerun  %reset  %reset_selective  %run  %save  %sc
    %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who
    %who_ls  %whos  %xdel  %xmode

    Available cell magics:
    %%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html  %%javascript
    %%latex  %%perl  %%prun  %%pypy  %%python  %%python3  %%ruby  %%script  %%sh
    %%svg  %%sx  %%system  %%time  %%timeit  %%writefile

Ipython kennt -- ebenso wie der Standard-Python-Interpreter -- zwei Arten von
Anweisungen: Zum einen "simple" einzeilige Anweisungen, zum anderen
"zusammengesetzte" Anweisungen, die aus mehreren Zeilen bestehen. In Ipython
wird eine solche Block-Anweisung auch als "Zelle" bezeichnet.

Die ``line magic``-Funktionen beziehen sich auf eine einzelne, einzeilige
Anweisung; den ``cell magic``-Funktionen werden hingegen der jeweiligen
Anweisung weitere Zeilen angefügt. Beispielsweise kann mittels ``%% writefile
dateiname`` der unmittelbar folgenden Text (ohne Anführungszeichen!) in eine
Datei geschrieben werden, bis die Eingabe durch ein zweimaliges Drücken von
``Enter`` beendet wird.

.. code-block:: python

    In [5]: %%writefile test.txt
            Hallo
            Welt!

    Writing tmp.txt

Mittels ``%%writefile -a`` wird der folgende Text an die angegebene Datei
angehängt; eine Eingabe von leeren Zeilen oder von formattiertem Text ist so
allerdings nicht möglich, die unmittelbar folgende Texteingabe wird "as it is"
geschrieben.

.. TODO: Mittels der Funktion ``%automagic`` normale magic-Funktionen ohne %
.. aufrufbar machen

Im folgenden werden einige der ``magic``-Funktionen näher beschrieben.

.. rubric:: Magic-Funktionen automatisch erkennen

Durch eine Eingabe von ``%automagic`` im Ipython-Interpreter werden im Verlauf
der Sitzung die Namen der Magic-Funktionen in den globalen Namensrauf
aufgenommen. Im folgenden kann damit wahlweise ``pwd`` oder ``%pwd``
eingegeben werden, um den Namen des aktuellen Arbeitsverzeichnisses anzuzeigen;
das bzw. die ``%``-Zeichen können anschließend also weggelassen werden.

.. _Python-Skripte aufrufen:

.. rubric:: Python-Skripte aufrufen

Python-Skripte lassen sich folgendermaßen vom Ipython-Interpreter aus aufrufen:

.. code-block:: python

    %run path/script.py [arguments]

Der obige Aufruf entspricht dem üblichen Aufruf von ``python3 path/script.py``
in einer Shell. Benötigt das Skript gegebenenfalls weitere Argumente, so können
diese im Anschluss an die Pfadangabe des Skripts angegeben werden. Ist das
aufgerufene Skript fehlerhaft und/oder benötigt es zu lange zur Ausführung, so
kann es mit ``Ctrl c`` unterbrochen werden (KeyboardInterrupt).

Befindet man sich bereits im Pfad der Programmdatei oder wechselt mittels
``os.chdir(path)`` dorthin, so kann die Pfadangabe im obigen Aufruf weggelassen
werden.

Ein Vorteil der ``%run``-Anweisung liegt darin, dass hierbei alle im
aufgerufenen Skript definierten Variablen und Funktionen importiert und
anschließend in der interaktiven Sitzung genutzt werden können (als wären sie
direkt eingeben worden).

... to be continued ...

