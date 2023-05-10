import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Erstellen der x-Werte für die erste Grafik mit weniger Stützstellen (2*np.pi/8 Schritte)
x1 = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
# Berechnen der sinus-Werte für die gegebenen x-Werte
y1 = np.sin(x1)
# Erstellen neuer x-Werte im Bereich [0, 2*pi] mit pi/50 Schritten für die Interpolation
x1new = np.arange(0, 2*np.pi, np.pi/50)
# Berechnen der kubischen Interpolationsfunktion (tck1) für die erste Grafik
tck1 = interpolate.splrep(x1, y1, s=0)
# Berechnen der interpolierten y-Werte (y1new) mit der kubischen Interpolationsfunktion
y1new = interpolate.splev(x1new, tck1, der=0)

# Plotten der originalen Datenpunkte, kubischen Interpolation und wahrer Sinusfunktion für die erste Grafik
plt.plot(x1, y1, 'o', x1new, y1new, 'r', x1new, np.sin(x1new), 'g', x1, y1, 'b--')
plt.legend(['Stützpunkte', 'Kubische Spline', 'Originalfunktion'])
plt.title('Approximation mit weniger Stützstellen')
# Anzeigen der ersten Grafik
plt.show()

# Erstellen der x-Werte für die zweite Grafik mit mehr Stützstellen (2*np.pi/16 Schritte)
x2 = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/16)
# Berechnen der sinus-Werte für die gegebenen x-Werte
y2 = np.sin(x2)
# Erstellen neuer x-Werte im Bereich [0, 2*pi] mit pi/50 Schritten für die Interpolation
x2new = np.arange(0, 2*np.pi, np.pi/50)
# Berechnen der kubischen Interpolationsfunktion (tck2) für die zweite Grafik
tck2 = interpolate.splrep(x2, y2, s=0)
# Berechnen der interpolierten y-Werte (y2new) mit der kubischen Interpolationsfunktion
y2new = interpolate.splev(x2new, tck2, der=0)

# Plotten der originalen Datenpunkte, kubischen Interpolation und wahrer Sinusfunktion für die zweite Grafik
plt.plot(x2, y2, 'o', x2new, y2new, 'r', x2new, np.sin(x2new), 'g', x2, y2, 'b--')
plt.legend(['Stützpunkte', 'Kubische Spline', 'Originalfunktion'])
plt.title('Approximation mit mehr Stützstellen')
# Anzeigen der zweiten Grafik
plt.show()
