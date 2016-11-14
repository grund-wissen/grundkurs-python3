# Module importieren
import numpy as np
import matplotlib.pyplot as plt

# Werte-Listen für eine Sinus- und Cosinus-Funktion erstellen:
x = np.linspace(-np.pi, np.pi, 500, endpoint=True)
cos_x = np.cos(x)
sin_x = np.sin(x)

# Größe des Plots anpassen:
plt.figure(figsize=(10,6), dpi=80)

# In diese Abbildung ein 1x1 großes Diagramm-Gitter erstellen;
# Als aktuelles Diagramm wird das erste dieses Gitters ausgewählt:
plt.subplot(111)

# Cosinus-Funktion mit blauner Farbe,
# Sinus-Funktion mit roter Farbe plotten:
plt.plot(x, cos_x, color='blue', linewidth=2.5, linestyle='-')
plt.plot(x, sin_x, color='red',  linewidth=2.5, linestyle='-')

# Wertebereiche der Achsen anpassen:
plt.xlim(x.min()*1.1, x.max()*1.1)
plt.ylim(cos_x.min()*1.1, cos_x.max()*1.1)

# "Ticks" (Bezugspunkte) für x-Achse festlegen:
plt.xticks(np.linspace(-4, 4, 9,endpoint=True))

# "Ticks" (Bezugspunkte) für y-Achse festlegen:
plt.yticks(np.linspace(-1, 1, 5,endpoint=True))

# Diagramm anzeigen:
plt.show()

