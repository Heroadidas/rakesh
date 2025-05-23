# eq = x*y + 4*y - 3*x**2 - y - y**2
import numdifftools as nd
import numpy as np
import matplotlib.pyplot as plt

x = [-2,-2]
def fun(x):
    return 2*x[0]*x[1] - x[0]**2 - 2*x[1]**2 + 2*x[0]
def fun2(x):
    return 2*x[0]*x[1] + x[1]**2 + 6*x[0] + 2*x[1]
grad2 = nd.Gradient(fun)([2,-2])
def gradient_descent(epoch, input):
    eta = 0.1
    history = [[input[0], input[1]]]
    for i in range(epoch):
        grad = nd.Gradient(fun2)(input)
        input[0] = input[0] - eta * grad[0]
        input[1] = input[1] - eta * grad[1]
        history.append([input[0], input[1]])
    return history

history = gradient_descent(10, [2, -2])
x_history = [point[0] for point in history]
y_history = [point[1] for point in history]
plt.plot(x_history, y_history)
plt.xlabel("x[0]")
plt.ylabel("x[1]")
plt.title("Gradient Descent Trajectory")
plt.show()

def gradient_Ascent(epoch, input):
    eta = 0.1
    history = [[input[0], input[1]]]
    for i in range(epoch):
        grad = nd.Gradient(fun2)(input)
        input[0] = input[0] + eta * grad[0]
        input[1] = input[1] + eta * grad[1]
        history.append([input[0], input[1]])
    return history

history = gradient_descent(10, [2, -2])
x_history = [point[0] for point in history]
y_history = [point[1] for point in history]
plt.plot(x_history, y_history)
plt.xlabel("x[0]")
plt.ylabel("x[1]")
plt.title("Gradient Ascent Trajectory")
plt.show()


def fun(x):
    return x[0]*x[1] + 4*x[1] - 3*x[0]**2  - x[1]**2
def newton_method(fun, x0, max_iter=100, tol=1e-6):
    x = x0
    x_history = [x0]
    for i in range(max_iter):
        grad = nd.Gradient(fun)(x)
        hess = nd.Hessian(fun)(x)
        try:
            hess_inv = np.linalg.inv(hess)
        except np.linalg.LinAlgError:
            print(f"Hessian is singular at iteration {i}")
            return x, x_history
        x_new = x - np.dot(hess_inv, grad)
        x_history.append(x_new)
        if np.linalg.norm(x_new - x) < tol:
            return x_new, x_history
        x = x_new
    print("Maximum iterations reached without convergence")
    return x, x_history
x0 = [1, 1]  # Initial guess
optimal_x, x_history = newton_method(fun, x0)
print(optimal_x)
# Visualization
x_values = [point[0] for point in x_history]
y_values = [point[1] for point in x_history]
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, marker='o')
plt.scatter(x_values[0], y_values[0], color='r', label='Initial Point')
plt.scatter(x_values[-1], y_values[-1], color='g', label='Optimal Point')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Newton's Method Optimization for x*y + 4*y - 3*x**2 - y**2")
plt.legend()
plt.show()
