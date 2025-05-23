import numpy as np
import matplotlib.pyplot as plt
# Define data for AND, OR, and XOR gates
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])
X_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_or = np.array([0, 1, 1, 1])
X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])
# Function to plot data points and decision boundaries
def plot_data_and_boundary(X, y, gate_type):
    plt.figure(figsize=(8, 6))
    # Plot data points for Class 0 and Class 1
    plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='blue', label='Class 0')
    plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='red', label='Class 1')
    # Plot decision boundaries based on gate type
    if gate_type == 'AND':
        plt.plot([-0.5, 1.5], [1.9, -0.4], color='green', linestyle='--', label='Decision Boundary')
    elif gate_type == 'OR':
        plt.plot([-0.5, 1.5], [0.5, -0.5], color='green', linestyle='--', label='Decision Boundary')
    elif gate_type == 'XOR':
        plt.plot([-0.5, 1.5], [1.9, -0.4], color='green', linestyle='--', label='Boundary 1')
        plt.plot([-0.5, 1.5], [0.5, -0.5], color='purple', linestyle='--', label='Boundary 2')
    # Customize plot
    plt.title(f'{gate_type} Gate')
    plt.xlabel('Input 1')
    plt.ylabel('Input 2')
    plt.legend()
    plt.grid(True)
    plt.show()
#  AND Gate
plot_data_and_boundary(X_and, y_and, gate_type='AND')
# Plot example: OR Gate
plot_data_and_boundary(X_or, y_or, gate_type='OR')
# Plot example: XOR Gate
plot_data_and_boundary(X_xor, y_xor, gate_type='XOR')