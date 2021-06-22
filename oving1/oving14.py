# Task1
# Read chapters (Done)

# Task2
# Watch movie (Done)

# Task 3

# 3.1
# Have working python

# 3.2

import matplotlib.pyplot as plt
import numpy as np

array100 = np.arange(1, 101)

sum100 = np.sum(array100)

print("Sum av tallene til 100: ", sum100)

# 3.3


w = 5
a = 2
time = np.linspace(0, 10, 100)
values = np.cos(w*time)*np.exp(-a*time)


plt.plot(time, values)
plt.title("Plot of f with w=5 and a=2")
plt.ylabel("Y-values")
plt.xlabel("X-Values")
plt.show()


# Task 6

# 6.3
t0 = 0
tf = 2
N = 100  # Antall punkter
c1 = 3
c2 = 0.8
t = np.linspace(t0, tf, N)
v = 0.5*c1*t**2-0.25*c2*t**4
plt.plot(t, v)
plt.ylabel("Fart (m/s)")
plt.xlabel("Tid (s)")
plt.show()


def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h


print("Areal: ", trapezoidal(lambda t: 0.5*c1*t**2-0.25*c2*t**4, 0, 2, N))
