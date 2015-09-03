.. _Singleton:

Singleton
=========

Als Singleton bezeichnet man ein Objekt, das innerhalb eines laufenden Programms
nur in einer Ausprägung ("Instanz") existieren darf; beispielsweise ist bei
jedem Betriebsystem mit grafischer Oberfläche genau ein Window-Manager in
Betrieb. Zugleich muss das Singleton-Objekt unter Umständen für viele
Stellen zugriffsbereit sein.

Singletons stellen also eine Art von klar definierten "Access Points" dar, auf
die von mehreren Clienten aus zugegriffen werden kann. Ein solches Objekt könnte
zwar prinzipiell auch mittels einer globalen Variable initiiert werden, jedoch
könnten dabei immer noch mehrere Instanzen des Objekts existieren -- man hätte
dann zwar das gleiche, aber nicht das selbe Objekt. Zudem soll die Klasse des
Grundobjekts durch die Erstellung von Unterklassen erweiterbar sein.

Singleton-Klasse
----------------

In Python kann eine Singleton-Klasse folgendermaßen als Klasse implementiert
werden:

.. code-block:: python

    class Singleton(object):
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super().__new__(cls)
            return cls.instance

Wird ein solches Objekt initiiert, so wird es nur dann eine neue Instanz des
Objekts erzeugt, falls noch keine solche existiert; andernfalls gibt die
Initiierung die bereits existierende Instanz als Ergebnis zurück. Auf diese
Weise kann man von beliebiger Stelle aus auf das Singleton zugreifen, indem
man eine neue Instanz des Singletons erzeugt:

.. code-block:: python

    # Ein neues Singleton erzeugen:
    singleton_1 = Singleton()

    # Das existierende Singleton an anderer Stelle nutzen:
    singleton_2 = Singleton()


Jedes Objekt, das ein Singleton darstellen soll, kann damit der obigen
Implementierung als Unterklasse eines Singletons definiert werden:

.. code-block:: python

    class Any_Singleton_Object(Singleton):
        """
        A Class for a Singleton Object.
        """

        # Class methods and attributes..

Bei der Initiierung eines solchen Objekts wird aufgrund der geerbten
``__new__()``-Funktion nur dann ein neues Objekt (mit allen
"Standardeinstellungen") erstellt, falls ein solches noch nicht existiert.
Ansonsten wird dieses mit all seinen Methoden und Attributen genutzt.


Singleton-Module
----------------

Die Initiierung eines Objekts ist stets mit etwas Rechenaufwand verbunden. Soll
auf ein Singleton häufig und möglichst schnell zugegriffen werden und ist
keine Aufgliederung des Singletons in mehrere mögliche Unterklassen nötig, so
kann anstatt der oben beschriebenen Klasse auch ein Singleton-Modul erzeugt
werden. Dieses Modul, das den Namen des Singletons (in Kleinbuchstaben) als
Dateinamen (mit Endung ``.py``) trägt, bekommt "Methoden" als Funktionen und
"Attribute" als Variablen auf Modulebene zugewiesen -- d.h. in diesem Modul
werden keine Klassen angelegt.

Da Module nach erstmaligem Importieren durch ``import modulname`` stets nur in
Form einer Referenz genutzt werden, kann auf die gewünschten Singleton-Methoden
unmittelbar mittels ``modul.funktionsname()`` und die gewünschten Attribute
mittels ``modul.variable`` zugegriffen werden.


... to be continued :-) ...
