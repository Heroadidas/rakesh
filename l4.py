import numpy as np
X1 = [1, 1, -1, -1]
print(X1)
X2 = [1, -1, 1, -1]
print(X2)
y=[1,-1,-1,-1]
print(y)
# Tanh Function
def tanh_function(z):
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))
# Define weights
W1 = 10
W2 = 11
# Predict values
y_pred = [0, 0, 0, 0]
for i in range(4):
    y_pred[i] = (X1[i] * W1) + (X2[i] * W2)
print(y_pred)

def Sigmoid(x):
    return 1 / (1 + np.exp(-x))
def relu(x):
    return max(0, x)
for i in y_pred:
    print(tanh_function(i))
for i in y_pred:
    print(Sigmoid(i))
for i in y_pred:
    print(relu(i))
    
    

# Define input values
X1 = [0, 0, 1, 1]
print(X1)
X2 = [0, 1, 0, 1]
print(X2)
y = [0, 1, 1, 0]
print(y)
# Define weights
w1 = 0
w2 = 1
w3 = 1
w4 = 0
w5 = 1
w6 = -1
# Initialize prediction arrays
y_pred = [0, 0, 0, 0]
z1 = [0, 0, 0, 0]
z2 = [0, 0, 0, 0]
# Forward propagation
for i in range(4):
   z1[i] = (X1[i]*w1) + (X2[i]*w3)
   z2[i] = (X2[i]*w4) + (X1[i]*w2)
   if((z1[i]*w5) + (z2[i]*w6) < 0):
       y_pred[i] = 1
   else:
       y_pred[i] = (z1[i]*w5)+(z2[i]*w6)
# Print results
print(z1)
print(z2)
print(y_pred)
def test(y, y_pred):
    flag = "Correct"
    index = -1
    for i in range(4):
        if y[i] != y_pred[i]:
            flag = "Incorrect"
            index = i
            break
    return flag, index
# Test the model
print(test(y,y_pred))