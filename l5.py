import matplotlib.pyplot as plt
# Effect of Weight on Network
weight = 1
bias = 1
def plot_weight_effect(weight, bias):
    x = range(-10, 11)
    y = [weight * i + bias for i in x]
    legend_label = f"weight = {weight}, bias = {bias}"
    plt.plot(x, y, label=legend_label)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_position('zero')

    plt.title("Weight and Bias Visualization")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_weight_effect(1, 1)
plot_weight_effect(3, 1)
plot_weight_effect(-2, 1)
plot_weight_effect(1, 5)
plot_weight_effect(1, -2)