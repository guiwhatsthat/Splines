import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import LSQUnivariateSpline

x = np.linspace(0, 2 * np.pi, 10)
y = np.sin(x)
xnew = np.linspace(0, 2 * np.pi, 100)

# Gewichte für die Datenpunkte definieren
weights = np.ones_like(x)
weights[[0, -1]] = 10  # Erhöhung der Gewichte für die Randpunkte

# Gewichteter Spline mit 3 Knotenpunkten
knots = np.linspace(x[1], x[-2], 3)
spl = LSQUnivariateSpline(x, y, knots, w=weights)

ynew = spl(xnew)

plt.plot(x, y, 'o', label='Datenpunkte')
plt.plot(xnew, ynew, '-', label='Gewichteter Spline')
plt.legend(loc='best')
plt.show()