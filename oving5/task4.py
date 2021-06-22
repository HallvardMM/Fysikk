import numpy as np
import matplotlib.pyplot as plt  # Used for plotting results

m = 0.01  # kg
k = 0.1  # N/m
F0 = 5  # usikker på om man skulle finne f0 eller bare velge
OMEGA = np.sqrt(k/m)
WD = np.linspace(0.1, 10, 1000)


def b(k, Q, w):
    return k/(Q*w)


def A(wd, q):
    b_value = b(k, q, wd)
    return F0*wd*b_value/np.sqrt(m**2*(OMEGA**2-wd**2)**2+b_value**2*wd**2)


fig = plt.figure()
l1, l2, l3, l4 = plt.plot(WD, A(WD, 1), 'b-', WD, A(WD, 3), 'r-',
                          WD, A(WD, 10), 'g-', WD, A(WD, 20), 'c-')
fig.legend((l1, l2, l3, l4), ('1', '3', '10', '20'), 'upper left')
plt.scatter([OMEGA], [0])
plt.annotate('omega', (OMEGA, 0))
plt.xlabel('W_{d}')
plt.show()
