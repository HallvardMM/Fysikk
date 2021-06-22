import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 360, 360)


def function(theta):
    return 0.5*(1+np.cos(np.deg2rad(theta)))


plt.plot(theta, function(theta), 'r-', label="kf/ki ")

plt.title("kf/ki in relation to theta")
plt.legend()
plt.xlabel(r'$x$ theta')
plt.ylabel(r'$y$ kf/ki')
plt.show()
