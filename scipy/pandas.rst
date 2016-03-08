.. index:: Pandas
.. _Pandas:

``pandas`` -- eine Bibliothek für tabellarische Daten
=====================================================

Pandas ist eine Python-Bibliothek, die vorrangig zum Auswerten und Bearbeiten
tabellarischer Daten gedacht ist. Dafür sind in Pandas drei Arten von Objekten
definiert:

* Eine ``Series`` entspricht in vielerlei Hinsicht einer "eindimensionalen"
  Liste, beispielsweise einer Zeitreihe, einer Liste, einem Dict, oder einem
  :ref:`Numpy <numpy>` -Array.

* Ein ``Dataframe`` besteht aus einer "zweidimensionalen" Tabelle. Die einzelnen
  Reihen beziehungsweise Spalten dieser Tabelle können wie ``Series``-Objekte
  bearbeitet werden.

* Ein ``Panel`` besteht aus einer "dreidimensionalen" Tabelle. Die einzelnen
  Ebenen dieser Tabelle bestehen wiederum aus ``Dataframe``-Objekten.

In den folgenden Abschnitten sollen die ``Series``- und die
``Dataframe``-Objekte als grundlegende und am häufigsten verwendeten
Pandas-Objekte kurz vorgestellt werden.

.. index:: Series()
.. _Arbeiten mit Series-Objekten:
.. _Series:

Arbeiten mit ``Series``-Objekten
--------------------------------

Ein neues Series-Objekt kann mittels der gleichnamigen Funktion
beispielsweise aus einer gewöhnlichen Liste generiert werden:

.. code-block:: python

    import pandas as p

    s = p.Series( [5,10,15,20,25] )

    s
    # Ergebnis:
    # 0     5
    # 1    10
    # 2    15
    # 3    20
    # 4    25
    # dtype: int64

Das Series-Objekt erhält automatisch einen Index, so dass beispielsweise mittels
``s[0]`` auf das erste Element, mit ``s[1]`` auf das zweite Element, usw.
zugegriffen werden kann. Neben diesen numerischen Indizes, die auch bei
gewöhnlichen Listen verwendet werden, können explizit auch andere Indizes
vergeben werden:

.. code-block:: python

    s.index =  ['a','b','c','d','e']

    s
    # Ergebnis:
    # a     5
    # b    10
    # c    15
    # d    20
    # e    25
    # dtype: int64

Nun können die einzelnen Elemente zwar immer noch mit ``s[0]``, ``s[1]``, usw.,
aber zusätzlich auch mittels ``s['a']``, ``s['b']`` usw. ausgewählt werden. [#]_
Wird bei der Generierung eines Series-Objekts ein :ref:`Dict <dict>` angegeben,
so werden automatisch die Schlüssel als Indizes und die Werte als eigentliche
Listenelemente gespeichert.

Sollen mehrere Elemente ausgewählt werden,so können die entsprechenden Indizes
wahlweise als Liste oder als so genannter "Slice" angegeben werden:

.. code-block:: python

    # Zweites und drittes Element auswählen:

    s[ [1,2] ]
    # Ergebnis:
    # b    10
    # c    15

    # Gleiche Auswahl mittels Slicing:

    s[1:3]
    # Ergebnis:
    # b    10
    # c    15

Bei Slicings wird, ebenso wie bei :ref:`range() <range()>`-Angaben, die obere
Grenze nicht in den Auswahlbereich mit eingeschlossen. Die Auswahl mittels
Slicing hat bei Series-Objekten also die gleiche Syntax wie die :ref:`Auswahl
von Listenobjekten <Indizierung von Listen und Tupeln>`.

.. index:: Zeitreihe, date_range()
.. _Zeitreihen:

.. rubric:: Zeitreihen

Zeitangaben in Series-Objekten können mittels der Pandas-Funktion
``date_range()`` generiert werden:

.. code-block:: python

    dates = p.date_range('2000-01-01', '2000-01-07')

    dates
    # <class 'pandas.tseries.index.DatetimeIndex'>
    # [2000-01-01, ..., 2000-01-07]
    # Length: 7, Freq: D, Timezone: None

Als Start- und Endpunkt werden allgemein Datumsangaben mit einer gleichen Syntax
wie im ``datetime``-Modul verwendet. Zusätzlich kann angegeben werden, in
welchen Zeitschritten die Zeitreihe erstellt werden soll:

.. code-block:: python

    weekly = p.date_range('2000-01-01', '2000-02-01', freq="W")

    weekly
    # Ergebnis:
    # <class 'pandas.tseries.index.DatetimeIndex'>
    # [2000-01-02, ..., 2000-01-30]
    # Length: 5, Freq: W-SUN, Timezone: None


    hourly = p.date_range('2000-01-01 8:00', '2000-01-01 18:00', freq="H")

    hourly
    # Ergebnis:
    # <class 'pandas.tseries.index.DatetimeIndex'>
    # [2000-01-01 08:00:00, ..., 2000-01-01 18:00:00]
    # Length: 11, Freq: H, Timezone: None

Die Elemente der Zeitreihe können explizit mittels ``list(zeitreihe``,
beispielsweise ``list(dates)``, ausgegeben werden; in Series-Objekten werden
Zeitreihen häufig als Index-Listen verwendet.

.. _Arbeiten mit Dataframe-Objekten:
.. _Dataframe:

Arbeiten mit ``Dataframe``-Objekten
-----------------------------------

.. index:: Dataframe()

Ein neues Dataframe-Objekt kann mittels der Funktion ``DataFrame()``
beispielsweise aus einer gewöhnlichen Liste generiert werden:

.. code-block:: python

    import pandas as p

    df = p.DataFrame( [5,10,15,20,25] )

    df
    # Ergebnis:
    #     0
    # 0   5
    # 1  10
    # 2  15
    # 3  20
    # 4  25
    #
    # [5 rows x 1 columns]

Als Unterschied zu einem Series-Objekt werden bei einem Dataframe sowohl die
Zeilen als auch die Spalten mit einem Index versehen.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Die Index-Liste kann auch bereits bei der Erzeugung eines neuen
    Series-Objekts mittels ``Series(datenliste, index=indexliste)`` angegeben
    werden.


