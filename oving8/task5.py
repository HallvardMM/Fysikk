import numpy as np
import matplotlib.pyplot as plt

e0 = 8.85 * 10**-12  # m^3*kg^-1*s^4*A^2
R1 = 3*10**-3  # m
Q1 = -2*10**-9  # C
R2 = 5*10**-3  # m
Q2 = 10*10**-9  # C
a = 1*10**-2  # m


def V1(x):
    return 1/(4*np.pi*e0)*Q1/np.sqrt(x**2+R1**2)


def V2(x):
    return V1(x) + 1/(4*np.pi*e0)*Q2/np.sqrt((x-a)**2+R2**2)


x = np.linspace(0.0001, 0.1, 1000)
p1 = plt.plot(x, V1(x), label="V1")
p2 = plt.plot(x, V2(x), label="V2")
plt.legend(loc="upper right")
plt.xlabel("x")
plt.ylabel("V")
plt.show()
