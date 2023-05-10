import scipy.interpolate as interpolate
import matplotlib.pyplot as plt
import numpy as np

# Definieren der Funktion, die interpoliert werden soll (in diesem Fall die Sinusfunktion)
def f(x):
    return np.sin(x)

# Definition der Grenzen des Interpolationsbereichs und der Anzahl der Stützpunkte
a = 0
b = 2 * np.pi
n = 10

# Erstellen der Stützpunkte für die Interpolation
x_stuetzpunkte = np.linspace(a, b, n)
y_stuetzpunkte = f(x_stuetzpunkte)

# Erstellen der linearen Interpolationsfunktion und der kubischen Spline-Funktion
linear_interp = interpolate.interp1d(x_stuetzpunkte, y_stuetzpunkte, kind='linear')
spline = interpolate.CubicSpline(x_stuetzpunkte, y_stuetzpunkte)

# Erstellen der x-Werte für das Plotten der Funktionen
x_plot = np.linspace(a, b, 1000)

# Berechnen der y-Werte für die verschiedenen Funktionen (exakte Funktion, lineare Interpolation, Spline-Approximation)
y_plot = f(x_plot)
y_linear = linear_interp(x_plot)
y_spline = spline(x_plot)

# Plotten der verschiedenen Funktionen und Stützpunkte
plt.plot(x_plot, y_plot, label='Exakte Funktion')
plt.plot(x_stuetzpunkte, y_stuetzpunkte, 'o', label='Stützpunkte')
plt.plot(x_plot, y_linear, label='Lineare Interpolation')
plt.plot(x_plot, y_spline, label='Spline-Approximation')

# Hinzufügen der Legende, Beschriftung der Achsen und Titel des Plots
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vergleich von Linearer Interpolation und Spline-Approximation')

# Anzeigen des Plots
plt.show()
