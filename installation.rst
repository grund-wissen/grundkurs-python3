.. index:: Installation
.. _Installation:

Installation
============

.. _Installation von Python3:

Installation von Python3
------------------------

Bei neuen Linux-Versionen ist Python in den Versionen 2.7 und 3.4 bereits
vorinstalliert. Auf älteren Systemen kann es hingegen notwendig sein, die
aktuelle (und sehr empfehlenswerte) Version 3 von Python nachträglich zu
installieren. Hierzu sollten folgende Pakete mittels ``apt`` installiert
werden:

.. code-block:: sh

    sudo aptitude install python3 python3-doc python3-setuptools pip3

Das zuletzt genannte Paket erlaubt es, zusätzliche Erweiterungen (sofern diese
nicht auch über ``apt`` installierbar sind) mittels folgender Syntax zu
installieren:

.. code-block:: sh

    sudo easy_install3 paketname

Dabei werden automatisch alle bekannten Python-Repositories durchsucht und die
aktuelle Version installiert. Mit der Option ``-U`` ("update") wird eine
eventuell bereits vorhandene, nicht mehr aktuelle Version eines Pakets durch die
neueste Version ersetzt. Beispielsweise kann so mittels ``easy_install3 -U
Sphinx`` die neueste Version des Python-Dokumentationssystems :ref:`Sphinx
<gwl:Sphinx>` installiert werden. Alternativ kann auch in den gewöhnlichen
Linux-Paketquellen mittels ``apt`` nach einem entsprechenden Python-Paket
gesucht beziehungsweise dieses installiert werden.

Eine Alternative zu ``easy-install`` ist ``pip3``:

.. code-block:: sh

    sudo pip3 install paketname

Bei Verwendung von ``pip3`` können die Namen der zu installierenden Module auch,
in eine Textdatei geschrieben werden, wobei jede Zeile genau einen Modulnamen
enthält. Heißt die Textdatei beispielsweise ``requirements.txt``, so können
mittels ``pip3 install -r requirements.txt`` alle benötigten Module auf einmal
installiert werden.



.. _Installation von Ipython3:

Installation von Ipython3
-------------------------

Anstelle des "normalen" Python-Interpreters, der sich durch Aufruf von
``python3`` ohne weitere Argumente starten lässt, sollte bevorzugt ``ipython3``
verwendet werden. Neben einer automatischen Vervollständigung von Modul-,
Klassen- und Funktionsnamen bei Drücken der ``Tab``-Taste bietet Ipython eine
interaktive Syntax-Hilfe und weitere hilfreiche Funktionen.

Folgende Pakete sollten für Ipython3 installiert werden:

.. code-block:: sh

    sudo aptitude install ipython3 ipython3-qtconsole ipython3-notebook python3-tk

Ipython kann als Shell-Version anschließend mittels ``ipython3``, die graphische
Oberfläche mittels ``ipython3 qtconsole`` gestartet werden.

.. index:: virtualenv
.. _Virtuelle Umgebungen:

Virtuelle Umgebungen
--------------------

Python ermöglicht es mittels einer so genannten virtuellen Umgebung, die
Entwicklung eines Python-Programms gezielt auf eine bestimmte Python-Version und
eine bestimmte Auswahl an installierten Paketen abzustimmen.

Zunächst muss hierzu das Paket ``virtualenv`` installiert werden:

.. code-block:: sh

    sudo aptitude install python virtualenv

Anschließend kann im Basis-Verzeichnis eines Projekts folgendermaßen eine neue
virtuelle Arbeitsumgebung erstellt werden:

.. code-block:: sh

    # Virtuelle Umgebung im Unterverzeichnis "env" erstellen:
    virtualenv -p python3 env

Diese Umgebung kann dann aus dem Projektverzeichnis heraus folgendermaßen
aktiviert werden:

.. code-block:: sh

    # Virtuelle Umgebung aktivieren:
    source env/bin/activate

Alle Paket-Installationen, die bei einer aktiven virtuellen Umgebung vorgenommen
werden, haben nur Auswirkung auf diese Umgebung; zunächst ist überhaupt kein
Zusatzpaket installiert. Mittels ``pip3 install paketname`` können wie gewohnt
Pakete installiert werden: 

.. code-block:: sh

    # Python-Paket in der virtuellen Umgebung installieren:
    pip3 install Sphinx

Gegebenenfalls muss, beispielsweise bei der lokalen Installation von
:ref:`Sphinx <gwl:Sphinx>`, anschließend ``hash -r`` eingegeben werden, damit
der "Suchpfad" aktualisiert und die Python-Programme beim Aufruf auch lokal
gefunden werden.

.. Es ist empfehlenswert, ebenfalls im Basisverzeichnis des Projekts eine Datei
.. ``requirements.txt`` mit den benötigten Modulen (ein Eintrag je Zeile) zu
.. erstellen und diese dann mittels ``pip3 install -r requirements`` zu
.. installieren. Auf diese Weise wird schnell deutlich, welche Pakete ein Benutzer
.. für die Verwendung des Programms installieren muss.

Durch Eingabe von ``deactivate`` in dem Shell-Fenster wird die virtuelle
Umgebung wieder beendet:

.. code-block:: sh

    # Virtuelle Umgebung beenden:
    deactivate



