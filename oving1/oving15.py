import matplotlib.pyplot as plt
import numpy as np


# Task 8
t = np.linspace(start=0, stop=4, num=40)
pt = 2*t**2
pp = 8*t-8
pp = np.hstack((np.zeros(10), pp[10:]))

plt.plot(t, pt, t, pp)

plt.ylabel("Posisjon fra origo(m)")
plt.xlabel("Tid (s)")
plt.show()


# Task 9

# 9.1
t0 = 0
t120 = 120
v0 = 30

t = np.linspace(t120, 960, 840)
b = v0*t120**2/t**2

a = np.ones(120)*30

t = np.linspace(0, 960, 960)
c = np.hstack((a, b))

plt.plot(t, c)
plt.ylabel("Fart (m/s)")
plt.xlabel("Tid (s)")
plt.show()


# 9.2

a = np.ones(t120)*0
t = np.linspace(t120, 960, 840)
b = -2*v0*t120**2/t**3

t = np.linspace(0, 960, 960)
c = np.hstack((a, b))

plt.plot(t, c)
plt.ylabel("Fart (m/s)")
plt.xlabel("Tid (s)")
plt.show()


# 9.3

t0 = 0
t120 = 120
v0 = 30

t = np.linspace(t120, 960, 840)
b = v0*t120**2/t**2

a = np.ones(120)*30

t = np.linspace(0, 960, 960)
c = np.hstack((a, b))


def integration(arrayC):
    temp = 0
    integration = []
    for i in range(len(arrayC)):
        integration.append(temp+arrayC[i])
        temp += arrayC[i]
    return integration


plt.plot(t, integration(c))
plt.ylabel("Posisjon (m)")
plt.xlabel("Tid (s)")
plt.show()
