import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

X = np.array([2000, 2002, 2005, 2007, 2010], dtype=np.float64)
Y = np.array([6.5, 7.0, 7.4, 8.2, 9.0], dtype=np.float64)
X_normalized = (X - X.min()) / (X.max() - X.min())
Y_normalized = (Y - Y.min()) / (Y.max() - Y.min())
m, b = 0.1, 0.1
learning_rate = 0.1


def cost_function(X, Y, m, b):
    return np.mean((Y - (m * X + b))**2)


def gradients(X, Y, m, b):
    dm = -2 * np.mean(X * (Y - (m * X + b)))
    db = -2 * np.mean(Y - (m * X + b))
    return dm, db


def update(frame):
    global m, b
    dm, db = gradients(X_normalized, Y_normalized, m, b)
    m -= learning_rate * dm
    b -= learning_rate * db
    line.set_ydata(m * X_normalized + b)
    print(f"Iteracja {frame}: m={m}, b={b}, koszt={cost_function(X_normalized, Y_normalized, m, b)}")
    return line,


fig, ax = plt.subplots()
ax.scatter(X_normalized, Y_normalized, color='red')
line, = ax.plot(X_normalized, m * X_normalized + b, 'b-')


ax.set_xlim(0, 1)
ax.set_ylim(0, 1)


ani = FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True)

plt.show()
