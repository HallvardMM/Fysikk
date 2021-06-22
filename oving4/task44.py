import numpy as np
import matplotlib.pyplot as plt

m1 = np.linspace(0, 100, 100)
l = 10
g = 9.81


def v2e(m1, m2):
    return (2**(3/2)*m1*(g*l)**0.5)/(m1+m2)


plt.plot(m1, v2e(m1, 0), 'r-', label="m2=0")
plt.plot(m1, v2e(m1, 20), 'g-', label="m2=20")
plt.plot(m1, v2e(m1, 40), 'b-', label="m2=40")
plt.plot(m1, v2e(m1, 60), 'ro', label="m2=60")
plt.plot(m1, v2e(m1, 80), 'go', label="m2=80")
plt.plot(m1, v2e(m1, 100), 'bo', label="m2=100")

plt.title("Speed of object 2 based on mass")
plt.legend()
plt.xlabel(r'$x$ [mass of object1 ]')
plt.ylabel(r'$y$ [Speed]')
plt.show()
