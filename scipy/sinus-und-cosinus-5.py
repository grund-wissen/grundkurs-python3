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

# Auf der x-Achse fünf Bezugspunkte (als Vielfache von pi) festlegen
# und mittels LaTeX-Symbolen beschriften:
plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
            [ r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$']
    )

# Auch Ticks für die y-Achse anpassen:
plt.yticks( [-1.0, -0.5, 0, 0.5, 1],
            [ r'$-1$', r'$-1/2$', r'', r'$+1/2$', r'$+1$']
    )

# Das Achsen-Objekt des Diagramms in einer Variablen ablegen:
ax = plt.gca()

# Die obere und rechte Achse unsichtbar machen:
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Die linke Diagrammachse auf den Bezugspunkt '0' der x-Achse legen:
ax.spines['left'].set_position(('data',0))

# Die untere Diagrammachse auf den Bezugspunkt '0' der y-Achse legen:
ax.spines['bottom'].set_position(('data',0))

# Ausrichtung der Achsen-Beschriftung festlegen:
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Achse-Beschriftungen durch weiß-transparenten Hintergrund hervorheben:
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))


# Diagramm anzeigen:
plt.show()

