
Ziffernsumme
------------

.. only:: html

    .. sidebar:: Hinweis

        Das Original dieser Maxima-Beispielaufgabe kann im Original `hier
        <http://www.lungau-academy.at/wxmax1001/D1001_F_MO_PU_Ziffernsumme.wxmx>`_
        heruntergeladen werden. Die wxmx-Datei kann mit `WxMaxima
        <http://wiki.ubuntuusers.de/Maxima>`_ geöffnet werden.

Bei dieser Aufgabe handelt es sich um eine Knobelaufgabe bzw. um eine einfache
Übungsaufgabe für lineare Gleichungssysteme.

*Aufgabe:*

Die Aufgabe besteht darin, eine dreistellige Zahl zu finden, die folgende
Bedingungen erfüllt:

1. Die Ziffernsumme einer dreistelligen Zahl ist gleich :math:`18`.

2. Die Hunderterstelle ist um :math:`6` größer als das :math:`2`-fache der
   Zehnerstelle.

3. Die Einerstelle ist um :math:`6` größer als das :math:`3`-fache der
   Zehnerstelle.


*Lösung:*

Definiert man die Variablen :math:`h` als die Hunderterziffer, :math:`z` als die
Zehnerziffer und :math:`e` als die Einerziffer, so ist die Ziffernsumme gleich
:math:`z + h + e`. Aus der Aufgabenstellung lassen sich damit folgende drei
Gleichungen aufstellen:

1. Die Ziffernsumme einer dreistelligen Zahl ist :math:`18`:

   .. math::

       z + h + e = 18

2. Die Hunderterstelle ist um :math:`6` größer als das :math:`2`-fache der
   Zehnerstelle.

   .. math::

       h - 6 = 2 \cdot z

3. Die Einerstelle ist um :math:`6` größer als das :math:`3`-fache der
   Zehnerstelle.

   .. math::

       e - 6 = 3 \cdot z

Dieses Gleichungsystem kann mittels :ref:`Sympy <Sympy>` gelöst werden. Der
Code dazu lautet beispielsweise:

.. code-block:: python

    import sympy as sy

    # Sympy-Variablen initiieren:
    h, z, e = sy.S( 'h z e'.split() )

    # Gleichungssystem formulieren:
    equations = [
        sy.Eq( z + h + e , 18  ),
        sy.Eq( h - 6     , 2*z ),
        sy.Eq( e - 6     , 3*z ),
    ]

    # Gleichungssystem lösen:
    sy.solve(equations)

    # Ergebnis: {h: 8, z: 1, e: 9}

Die Hunderterziffer ist gleich :math:`8`, die Zehnerziffer gleich :math:`1` und
die Einerziffer gleich :math:`9`. Die gesuchte Zahl lautet somit :math:`819`.


