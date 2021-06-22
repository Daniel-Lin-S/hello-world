coeff = [3, 2, 5, 1, 0.5, 4, 3, 7, 2]

import matplotlib.pyplot as plt
import numpy as np

def plot_fourier(coefficients):
    x = np.arange(-10, 10, 0.1)
    y = coefficients[0]
    for n in range(1, len(coefficients)):
        y += coefficients[n] * np.sin(n * x)
    plt.title('Fourier approximation')
    plt.plot(x,y)
    plt.show()

plot_fourier(coeff)
