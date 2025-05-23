import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x1 = 0.35
x2 = 0.9
w13 = 0.1
w14 = 0.4
w23 = 0.8
w24 = 0.4
w35 = 0.3
w45 = 0.9
eta=1
t = 0.5
learning_rate = 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def forward_pass(x1, x2, w13, w14, w23, w24, w35, w45):
    v3 = x1 * w13 + x2 * w23
    y3 = sigmoid(v3)
    v4 = x1 * w14 + x2 * w24
    y4 = sigmoid(v4)
    v5 = y3 * w35 + y4 * w45
    y5 = sigmoid(v5)
    return y3, y4, y5
def calculate_error(y5, t):
    error = t - y5
    return error
def calculate_local_gradients(y3, y4, y5, w35, w45, error):
    delta5 = y5 * (1 - y5) * error
    delta3 = y3 * (1 - y3) * (delta5 * w35)
    delta4 = y4 * (1 - y4) * (delta5 * w45)
    return delta3, delta4, delta5
def update_weights(x1, x2, delta3, delta4, delta5, learning_rate, w13, w14, w23, w24, w35, w45, alpha,y3,y4):#remove alpha if no momentum like strt from lr
    w35 = alpha * w35 + learning_rate * y3 * delta5
    w45 = alpha * w45 + learning_rate * y4 * delta5
    w13 = alpha * w13 + learning_rate * x1 * delta3
    w14 = alpha * w14 + learning_rate * x1 * delta4
    w23 = alpha * w23 + learning_rate * x2 * delta3
    w24 = alpha * w24 + learning_rate * x2 * delta4
    return w13, w14, w23, w24, w35, w45
errors = []
def train_one_epoch(x1, x2, w13, w14, w23, w24, w35, w45, t, eta, alpha):
    y3, y4, y5 = forward_pass(x1, x2, w13, w14, w23, w24, w35, w45)
    error = calculate_error(y5, t)
    delta3, delta4, delta5 = calculate_local_gradients(y3, y4, y5, w35, w45, error)
    w13, w14, w23, w24, w35, w45 = update_weights(x1, x2, delta3, delta4, delta5, eta, w13, w14, w23, w24, w35, w45, alpha,y3,y4)
    return error, w13, w14, w23, w24, w35, w45
alpha = 0.5
for epoch in range(10):
    error, w13, w14, w23, w24, w35, w45 = train_one_epoch(x1, x2, w13, w14, w23, w24, w35, w45, t, eta, alpha)
    errors.append(error)
plt.plot(range(1, 11), errors, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.grid()
plt.show()