import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0, 10, 100)  # Create 100 evenly spaced points from 0 to 10
y = np.sin(x) + np.random.normal(0, 0.1, 100)  # Add normally distributed noise to sine

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x) with noise', color='blue', linestyle='--')
plt.title('Line Plot Example')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

x = np.random.rand(100) * 10
y = np.random.rand(100) * 5 + 2 * x
sizes = np.random.rand(100) * 100
colors = np.random.rand(100)

# Perform linear regression to fit the data
coefficients = np.polyfit(x, y, 1)
poly_function = np.poly1d(coefficients)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, label='data points')
plt.plot(x, poly_function(x), color='red', label='regression line')
plt.title('Scatter Plot with Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Sizes')
plt.legend()
plt.grid(True)
plt.show()

categories = ['A', 'B', 'C', 'D']
values = np.random.randint(1, 50, size=len(categories))

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='green', alpha=0.7)
plt.title('Bar Plot Example')
plt.xlabel('Category')
plt.ylabel('Values')
plt.grid(axis='y')
plt.show()

epochs = np.arange(1, 11)
train_loss = np.random.rand(10) * 0.5 + np.linspace(0.5, 0.1, 10)  # Random training loss
val_loss = np.random.rand(10) * 0.5 + np.linspace(0.4, 0.05, 10)  # Random validation loss

plt.figure(figsize=(8, 6))
plt.plot(epochs, train_loss, label='Training Loss', color='blue', marker='o')
plt.plot(epochs, val_loss, label='Validation Loss', color='orange', marker='s')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

from sklearn.metrics import confusion_matrix
import seaborn as sns

# Generate example true labels and predicted labels
true_labels = np.random.randint(0, 3, size=100)
predicted_labels = np.random.randint(0, 3, size=100)

cm = confusion_matrix(true_labels, predicted_labels)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

activations = np.random.randn(1000)

plt.figure(figsize=(8, 6))
plt.hist(activations, bins=30, color='green', alpha=0.7)
plt.title('Activation Histogram')
plt.xlabel('Activation Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()