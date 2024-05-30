import numpy as np
import matplotlib.pyplot as plt

# Generate universe variables
x = np.arange(0, 11, 0.1)

# Triangular membership function
def triangular(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

tri = triangular(x, 2, 5, 10)
plt.figure()
plt.plot(x, tri, 'b', linewidth=1.5, label='Triangular')
plt.title('Triangular membership function')
plt.legend()
plt.show()

# Gaussian membership function
def gaussian(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

gauss = gaussian(x, 5, 2)
plt.figure()
plt.plot(x, gauss, 'g', linewidth=1.5, label='Gaussian')
plt.title('Gaussian membership function')
plt.legend()
plt.show()

# Trapezoid membership function
def trapezoid(x, a, b, c, d):
    return np.maximum(np.minimum((x - a) / (b - a), 1, (d - x) / (d - c)), 0)

trap = trapezoid(x, 2, 4, 6, 8)
plt.figure()
plt.plot(x, trap, 'r', linewidth=1.5, label='Trapezoid')
plt.title('Trapezoid membership function')
plt.legend()
plt.show()