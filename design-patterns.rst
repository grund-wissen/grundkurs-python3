.. _Design Patterns:

Design Patterns
===============

An dieser Stelle sollen einige hilfreiche Entwurfsmuster ("Design Patterns") und
ihre Implementierungen in Python 3 vorgestellt werden.


Erzeugungsmuster
----------------

Als Erzeugungsmuster ("creational patterns") werden Entwurfsprinzipien
bezeichnet, die für das Erstellen neuer Objekte hilfreich sein können.

Factory
^^^^^^^

Als "Factories" werden Hilfsobjekte bezeichnet, deren Aufgabe es ist, die
Erzeugung eines Objekts von seiner Verwendung zu trennen. Man unterscheidet im
Allgemeinen zwischen zwei verschiedenen Möglichkeiten, dieses Prinzip zu
implementieren:

* Bei einer "Factory Method" wird ein neues Objekt durch den Aufruf einer
  Funktion erzeugt und von dieser als Ergebnis zurückgegeben. Die erzeugende
  Funktion erstellt das neue Objekt dabei in Abhängigkeit vom Kontext.
  Beispielsweise kann nach diesem Prinzip eine Funktion ``read_file()`` ein
  Datei-Reader-Objekt in Abhängigkeit vom Dateityp bzw. der Datei-Endung des
  angegebenen Pfads generieren:

  .. code-block:: python
  
      # Factory-Method-Beispiel

      class CSV_Reader():

          def __init__(self, path):
              pass

      def file_reader(path):

          # Todo: Check if file exists

          if path.endswith(".csv"):
              return CSV_READER(path)
          else:
              return None

      csv_reader = file_reader('test.csv')

  Soll durch eine Factory Method eine direkte Instanzierung einer Klasse
  verhindert werden, so kann die Definition dieser Klasse auch innerhalb der
  Funktionsdefinition erfolgen.

  Die generierende Funktion kann selbstverständlich auch als eine Methode einer
  "Factory Class" implementiert werden. Eine solche Klasse kann wiederum mehrere
  verschiedene Factory Methods beinhalten und somit die Generierung von mehreren
  Objekten bündeln. (Eine echte Firma erzeugt auch meist mehr als ein Produkt.)

* Bei Verwendung einer "Abstract Factory" werden über eine weitere
  Generalisierungs-Ebene die Factory-Methoden einer konkreten Factory-Klasse
  kontextbezogen aufgerufen. Durch Verwendung dieses Patterns könnte
  beispielsweise in einem Strategie-Spiel ein "Gebäude" je nach
  Entwicklungsstufe andere "Gegenstände" erzeugen.

Factories erzeugen nach ihrem Grundprinzip fertige Objekte "aus einem Guss".
Soll ein ein Objekt allerdings aus einzelnen Teilen erzeugt werden, so empfiehlt
sich die Verwendung des folgenden "Builder"-Patterns.

.. _Builder:

Builder
^^^^^^^

Das "Builder"-Pattern kann verwendet werden, wenn ein Objekt schrittweise aus
einzelnen Komponenten zusammengestellt werden muss. Die einzelnen Komponenten
werden dabei durch Factory-Methoden einer (oder mehrerer) "Builder"-Klassen
erzeugt. Die Builder-Methoden werden wiederum von einem "Director"-Objekt in der
gewünschten Reihenfolge aufgerufen. Das gewünschte Objekt als Ganzes wird also
über den Direktor in Auftrag gegeben, der die Anfrage an den passenden Builder
weiter reicht. Ist das Objekt erstellt, kann der Director es wiederum beim
Builder abholen und als Ergebnis zurückgeben. Während die einzelnen Builder
wiederum "Factories" darstellen, ist der Director ein steuerndes Element, das
kontextbezogen den relevanten Builder auswählt und gewissermaßen "nach Rezept"
nacheinander dessen Methoden aktiviert.

.. TODO: Beispiel

.. _Prototype:

Prototype
^^^^^^^^^

Mittels eines "Prototyps" kann ein neues Objekt erstellt werden, indem ein
bestehendes Objekt als Startpunkt verwendet wird. Um einen Prototypen zu
erzeugen, muss also zunächst eine exakte Kopie eines bestehenden Objekts erzeugt
werden.

In Python ist dies einfach mittels der Funktion ``deepcopy()`` aus dem Paket
``copy``

.. _Singleton:

Singleton
^^^^^^^^^

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

.. rubric:: Singleton-Klasse

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

.. _Singleton-Module:

.. rubric:: Singleton-Module

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

.. _Strukturmuster:

Strukturmuster
--------------

Als Strukturmuster ("structural patterns") werden Entwurfsprinzipien bezeichnet,
die für das Zusammenwirken mehrerer Objekte im Programm nützlich sein können.


Adapter
^^^^^^^



Model-View-Controller
^^^^^^^^^^^^^^^^^^^^^

.. _Verhaltensmuster:

Verhaltensmuster
----------------



