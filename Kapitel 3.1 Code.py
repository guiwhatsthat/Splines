import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Beispielkurve: Sinusfunktion
def exact_function(x):
    return np.sin(x)

# Berechnung des mittleren quadratischen Fehlers (MSE)
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

# Berechnung der maximalen Abweichung
def max_deviation(y_true, y_pred):
    return np.max(np.abs(y_true - y_pred))

# Anzahl der Stützstellen variieren
num_support_points = [5, 10, 20, 50]

# Ergebnisse speichern
results = []

for num_points in num_support_points:
    # Stützstellen erstellen
    x_support = np.linspace(0, 2 * np.pi, num_points)
    y_support = exact_function(x_support)

    # Kubische Splines erstellen
    cs = CubicSpline(x_support, y_support)

    # Feinere x-Werte für die Auswertung
    x_fine = np.linspace(0, 2 * np.pi, 1000)
    y_exact = exact_function(x_fine)
    y_approx = cs(x_fine)

    # Qualität der Approximation berechnen
    mse_value = mse(y_exact, y_approx)
    max_dev = max_deviation(y_exact, y_approx)

    results.append((num_points, mse_value, max_dev))

    # Grafik erstellen
    plt.figure()
    plt.plot(x_fine, y_exact, label="Exakte Kurve")
    plt.plot(x_fine, y_approx, label="Approximation")
    plt.plot(x_support, y_support, 'ko', label="Stützpunkte")
    plt.legend()
    plt.title(f"Approximation mit {num_points} Stützpunkten")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

# Ergebnisse in einer Tabelle ausgeben
print("Anzahl der Stützpunkte | MSE | Maximale Abweichung")
for result in results:
    print(f"{result[0]:>20} | {result[1]:.5f} | {result[2]:.5f}")
