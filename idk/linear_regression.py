import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set the backend to TkAgg
plt.switch_backend('TkAgg')

# Given data
x = np.array([0, 2, 5, 7, 10])
y = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

# Initial parameters
m = 0
b = 0
learning_rate = 0.01
iterations = 1000

# Number of data points
n = float(len(x))

# Gradient Descent
for i in range(iterations):
    y_pred = m * x + b
    D_m = (-2/n) * sum(x * (y - y_pred))  # Derivative wrt m
    D_b = (-2/n) * sum(y - y_pred)        # Derivative wrt b
    m = m - learning_rate * D_m
    b = b - learning_rate * D_b

print(f"Linear Regression Model: y = {m:.3f}x + {b:.3f}")

# Predicting the year when percentage exceeds 12%
threshold_percentage = 12
year_when_exceeds = (threshold_percentage - b) / m
predicted_year = 2000 + year_when_exceeds  # Adjust for normalization

print(f"The percentage of unemployed exceeds 12% in the year: {predicted_year:.0f}")

# Visualization using Matplotlib
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(6, 10)
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    global m, b
    y_pred = m * x + b
    D_m = (-2/n) * sum(x * (y - y_pred))
    D_b = (-2/n) * sum(y - y_pred)
    m = m - learning_rate * D_m
    b = b - learning_rate * D_b
    line.set_data(x, m * x + b)
    return line,

ani = FuncAnimation(fig, update, frames=np.arange(0, 1000), init_func=init, blit=True)

plt.scatter(x, y)
plt.title('Linear Regression using Gradient Descent')
plt.xlabel('Years since 2000')
plt.ylabel('Percentage Unemployed')
plt.show()