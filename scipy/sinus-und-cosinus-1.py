# Module importieren
import numpy as np
import matplotlib.pyplot as plt

# Werte-Listen für eine Sinus- und Cosinus-Funktion erstellen:
x = np.linspace(-np.pi, np.pi, 500, endpoint=True)
cos_x = np.cos(x)
sin_x = np.sin(x)

# Eine neues Matplot-Figure-Objekt mit 8x6 Zoll und
# einer Auflösung von 100 dpi erstellen:
plt.figure(figsize=(8, 6), dpi=80)

# In diese Abbildung ein 1x1 großes Diagramm-Gitter erstellen;
# Als aktuelles Diagramm wird das erste dieses Gitters ausgewählt:
plt.subplot(111)

# Cosinus-Funktion mit blauner Farbe, durchgehender Linie und 1 Pixel
# Linienbreite plotten:
plt.plot(x, cos_x, color="blue", linewidth=1.0, linestyle="-")

# Sinus-Funktion mit grüner Farbe, durchgehender Linie und 1 Pixel
# Linienbreite plotten:
plt.plot(x, sin_x, color="green", linewidth=1.0, linestyle="-")

# Grenzen für die x-Achse festlegen:
plt.xlim(-4.0, 4.0)

# Grenzen für die y-Achse festlegen:
plt.ylim(-1.0, 1.0)

# "Ticks" (Bezugspunkte) für x-Achse festlegen:
plt.xticks(np.linspace(-4, 4, 9,endpoint=True))

# "Ticks" (Bezugspunkte) für y-Achse festlegen:
plt.yticks(np.linspace(-1, 1, 5,endpoint=True))

# Diagramm anzeigen:
plt.show()

