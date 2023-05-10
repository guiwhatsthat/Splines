# Importieren der benötigten Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Funktion zum Plotten der kubischen Interpolation
def plot_cubic_interpolation(s_value):
    # Erstellen von x-Werten im Bereich [0, 2*pi] mit 2*pi/8 Schritten
    x = np.arange(0, 2 * np.pi + np.pi / 4, 2 * np.pi / 8)
    # Berechnen der sinus-Werte für die gegebenen x-Werte
    y = np.sin(x)
    
    # Erstellen neuer x-Werte im Bereich [0, 2*pi] mit pi/50 Schritten
    xnew = np.arange(0, 2 * np.pi, np.pi / 50)
    
    # Berechnen der kubischen Interpolationsfunktion (tck) mit Glättungsparameter s
    tck = interpolate.splrep(x, y, s=s_value)
    
    # Berechnen der interpolierten y-Werte (ynew) mit der kubischen Interpolationsfunktion
    ynew = interpolate.splev(xnew, tck, der=0)
    
    # Plotten der originalen Datenpunkte, kubischen Interpolation und wahrer Sinusfunktion
    plt.plot(x, y, 'o', xnew, ynew, 'r', xnew, np.sin(xnew), 'g', x, y, 'b--')
    
    # Hinzufügen der Legende und Titel
    plt.legend(['Linear', 'Cubic', 'True'])
    plt.title(f'Cubic Interpolation with s={s_value}')
    
    # Anzeigen des Plots
    plt.show()

# Ausführen der plot_cubic_interpolation-Funktion mit verschiedenen Glättungsparametern
plot_cubic_interpolation(0)
plot_cubic_interpolation(2)
