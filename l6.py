import numpy as np

# Hebbian learning function
def hebbian_learning(x1, x2, t, epochs=1):
    w1 = w2 = bias = 0
    for _ in range(epochs):
        for i in range(len(t)):
            y_pred = bias + w1 * x1[i] + w2 * x2[i]
            if y_pred != t[i]:
                w1 += x1[i] * t[i]
                w2 += x2[i] * t[i]
                bias += t[i]
    return w1, w2, bias
# Thresholding function
def threshold(y):
    return np.where(y < 0, -1, 1)
# Input vectors
x1 = np.array([1, 1, -1, -1])
x2 = np.array([1, -1, 1, -1])
# Target for AND gate: [1, -1, -1, -1]
# Target for OR gate: [1, 1, 1, -1]
t = np.array([1, -1, -1, -1])  # Change this to test OR gate
# Train
w1, w2, bias = hebbian_learning(x1, x2, t, epochs=2)
# Predict
y_pred = threshold(bias + w1 * x1 + w2 * x2)
print("Predictions:", y_pred)


def adaline_train(x1, x2, t, eta=0.1, max_epochs=3, error_threshold=2.0):
    w1 = w2 = b = 0.1
    iteration = 0
    print("Iter\tInput\t\tTarget\tYin\t\tError\t\tW1\t\tW2\t\tBias\t\tSqError")
    for epoch in range(max_epochs):
        total_error = 0
        for i in range(len(t)):
            y_in = b + w1 * x1[i] + w2 * x2[i]
            error = t[i] - y_in
            final_error = error ** 2
            total_error += final_error
            # Weight and bias update
            w1 += eta * error * x1[i]
            w2 += eta * error * x2[i]
            b += eta * error
            print(f"{iteration+1}\t{x1[i]}\t{x2[i]}\t{t[i]}\t{y_in:.4f}\t{error:.4f}\t{w1:.4f}\t{w2:.4f}\t{b:.4f}\t{final_error:.4f}")
            iteration += 1
        if total_error <= error_threshold:
            break
    print("\nFinal Weights and Bias:")
    print(f"W1 = {w1:.4f}, W2 = {w2:.4f}, Bias = {b:.4f}\n")
# Bipolar input
x1 = np.array([1, 1, -1, -1])
x2 = np.array([1, -1, 1, -1])
# Train for AND gate
print("Training Adaline for AND Gate:")
t_and = np.array([1, -1, -1, -1])
adaline_train(x1, x2, t_and)
# Train for OR gate
print("Training Adaline for OR Gate:")
t_or = np.array([1, 1, 1, -1])
adaline_train(x1, x2, t_or)

import numpy as np
import matplotlib.pyplot as plt

# Example data
x1 = np.array([1, 2, 3, 4])
x2 = np.array([1, 2, 3, 4])
y = np.array([0, 1, 0, 1])  # labels
x_test = [2.5, 2.5]         # test point
# Compute Euclidean distances in 2D
y_eucl = [((x1[i] - x_test[0])**2 + (x2[i] - x_test[1])**2)**0.5 for i in range(len(x1))]
# Combine indices and distances and sort
combined_data = list(zip(range(len(y)), y_eucl))
sorted_data = sorted(combined_data, key=lambda x: x[1])
# Number of neighbors
k = 3
nearest_indices = [i for i, _ in sorted_data[:k]]
# Plot all data points
plt.scatter(x1, x2, c=y, cmap='coolwarm', label='Data Points')
# Plot test point
plt.scatter(*x_test, c='green', marker='x', s=100, label='Test Point')
# Highlight nearest neighbors and draw lines
for i in nearest_indices:
    plt.scatter(x1[i], x2[i], c='red', s=100, edgecolors='black', label='Neighbor' if i == nearest_indices[0] else "")
    plt.plot([x_test[0], x1[i]], [x_test[1], x2[i]], c='black', linestyle='--')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('2D k-NN Visualization')
plt.legend()
plt.show()
# Print sorted distances
print("Index\tLabel\tDistance")
for idx, dist in sorted_data:
    print(f"{idx}\t{y[idx]}\t{dist:.4f}")
    
    
#competitve learning
c_x1 = [0.2, 0.6, 0.4, 0.9, 0.2]
c_x2 = [0.3, 0.5, 0.7, 0.6, 0.8]
x1, x2 = 0.3, 0.4
# Compute squared distances from input to cluster centers
d = [ (c_x1[i] - x1)**2 + (c_x2[i] - x2)**2 for i in range(len(c_x1)) ]
print("Distances:", d)
# Find index of closest cluster center
min_index = d.index(min(d))
print("Minimum value:", d[min_index])
print("Cluster of minimum value:", min_index + 1)
# Weight update of winner cluster 
eta = 0.3
c_x1[min_index] = c_x1[min_index] + eta *(x1 - c_x1[min_index])
c_x2[min_index] = c_x2[min_index] + eta *(x2 - c_x2[min_index])
# Find index of closest cluster center again
min_index = d.index(min(d))
print("Minimum value after update:", d[min_index])
print("Cluster of minimum value after update:", min_index + 1)



