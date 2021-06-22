import numpy as np
import matplotlib.pyplot as plt

e = 1.602 * 10**-19  # c
k = 8.988 * 10**9  # Nm^2C^-2

case = (2+1)**2/2**2


def F1(x):
    return k*-e*-e/(x**2)


def F2(x):
    return k*case*e*-e/(1+x)**2


def F3(x):
    return F1(x)+F2(x)


x = np.linspace(1, 10, 100)
p1 = plt.plot(x, F1(x), label="F1 (q2,q3)")
p2 = plt.plot(x, F2(x), label="F2 (q1, q3)")
p3 = plt.plot(x, F3(x), label="F3 (q1, q2, q3)")

plt.legend(loc="upper right")
plt.xlabel("x (m)")
plt.ylabel("F (N)")
plt.xlim([1, 10])
plt.show()
