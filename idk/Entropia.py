import numpy as np

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Input values
x = np.array([0.6, 0.1])
target = 1

# Initial weights
w_ih = np.array([[0.1, 0.2], [-0.2, 0.3], [0.0, -0.4]])  # Weights from input to hidden layer
w_ho = np.array([-0.4, 0.1])  # Weights from hidden to output layer
bias_h = np.array([0.1, 0.2])  # Bias for hidden layer
bias_o = 0.5  # Bias for output layer

# Learning rate
alpha = 0.1

# Forward propagation
h_input = np.dot(w_ih.T, x) + bias_h
h_output = sigmoid(h_input)

o_input = np.dot(w_ho, h_output) + bias_o
o_output = sigmoid(o_input)

# Calculate error
error = target - o_output

# Backward propagation
delta_o = error * sigmoid_derivative(o_output)
delta_h = delta_o * w_ho * sigmoid_derivative(h_output)

# Update weights
w_ho += alpha * delta_o * h_output
w_ih += alpha * np.outer(x, delta_h).T

# Update biases
bias_o += alpha * delta_o
bias_h += alpha * delta_h

print("Updated weights from input to hidden:", w_ih)
print("Updated weights from hidden to output:", w_ho)
print("Updated biases for hidden layer:", bias_h)
print("Updated bias for output layer:", bias_o)