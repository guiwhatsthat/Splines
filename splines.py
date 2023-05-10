import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Gegebene Punkte
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 2, 3, 1])

# Kubischer Spline erstellen
cs = CubicSpline(x, y)

# Feinere x-Werte für die Visualisierung
x_fine = np.linspace(0, 5, 100)

# Spline-Kurve berechnen
y_fine = cs(x_fine)

# Visualisierung
plt.plot(x, y, 'o', label='Stützstellen')
plt.plot(x_fine, y_fine, label='Kubischer Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()