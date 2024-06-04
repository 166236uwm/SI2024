
import numpy as np

# Perceptron Learning Algorithm for AND NOT Function
# Initialize parameters
w = np.array([0.5, 0.5, 0.5])  # Weights (including bias)
learning_rate = 0.5
epochs = 10

# Training data for x1 AND NOT x2
training_data = [
    (np.array([1, 0, 0]), 0),  # (x1, x2, bias), target
    (np.array([1, 0, 1]), 1),
    (np.array([1, 1, 0]), 0),
    (np.array([1, 1, 1]), 0)
]

# Activation function
def step_function(x):
    return 1 if x >= 0 else 0

# Training the perceptron
for epoch in range(epochs):
    for inputs, target in training_data:
        weighted_sum = np.dot(inputs, w)
        output = step_function(weighted_sum)
        error = target - output
        w += learning_rate * error * inputs

print(f"Trained Weights: {w}")
