from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
from scipy import interpolate



#3.1 Sinusfunkmtion mit wenig Punkten
#Dieses Code-Snippet plottet die Stützpunkten einer Cosinus Funktion
#Das INtervall der Funktion ist [0, 5]
#Anzahl der Stützpunkten 6
x=np.linspace(0,5, num=6)
y=np.sin(x)
plt.plot(x,y,'o--')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Stützpunkte
x = np.linspace(0, 5, num=6)
y = np.sin(x)

# Kubische Splines erzeugen
cs = CubicSpline(x, y)

# Feinere x-Werte für die Visualisierung der Splines
x_fine = np.linspace(0, 5, num=300)

# Abschnitte mit unterschiedlichen Farben darstellen
colors = ['r', 'g', 'b', 'm', 'c']
for i in range(len(x) - 1):
    x_segment = x_fine[(x_fine >= x[i]) & (x_fine <= x[i+1])]
    plt.plot(x_segment, cs(x_segment), c=colors[i % len(colors)])

# Stützpunkte hinzufügen
plt.scatter(x, y, c='k', marker='o', zorder=5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Kubische Splines')
plt.show()
