import numpy as np
import matplotlib.pyplot as plt
np.random.seed(9)
# Generate random data points
N = 100
X = np.random.rand(N, 2) * 5
# Assign class labels
y = np.sign(X[:, 1] - X[:, 0] + 0.5)
# Introduce outliers
outlier_ratio = 0.2
outlier_x = np.random.rand(int(N * outlier_ratio), 2) * 2 + 3
outlier_y = np.ones(int(N * outlier_ratio)) * -1
X = np.vstack((X, outlier_x))
y = np.concatenate((y, outlier_y))
# Plot the data points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Random Data Points')
plt.show()

# Learning rate and training parameters
eta = 0.1
epochs = 50
w = np.random.rand(2)
bias = 0
# Perceptron training loop
for epoch in range(epochs):
    error_count = 0
    for i in range(N):
        activation = np.dot(w, X[i]) + bias
        prediction = np.sign(activation)
        if prediction != y[i]:
            error_count += 1
            w += eta * y[i] * X[i]
            bias += eta * y[i]
    # Visualization every 10 epochs
    if epoch % 10 == 0:
        plt.figure(figsize=(5, 5))
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
        x_span = np.linspace(min(X[:, 0]) - 0.5, max(X[:, 0]) + 0.5)
        y_span = -(bias + w[0] * x_span) / w[1]
        plt.plot(x_span, y_span, color='red', label='Decision Boundary')
        plt.xlabel('X1')
        plt.ylabel('X2')
        plt.title(f'Epoch {epoch}, Errors: {error_count}')
        plt.legend()
        plt.show()