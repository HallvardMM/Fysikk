import numpy as np
import matplotlib.pyplot as plt  # Used for plotting results


def step_Euler(y, h, f):
    next_y = y + h * f(y)
    return next_y


def full_Euler(h, f, y_0=0, start_t=0, end_t=10):
    N = int((end_t - start_t) / h)
    t_list = np.linspace(start_t, end_t, N + 1)
    y_list = np.zeros(N + 1)
    y_list[0] = y_0
    for i in range(0, N):
        y_list[i + 1] = step_Euler(y_list[i], h, f)
    return y_list, t_list


def g(v):
    speed = 9.81*(np.sin(30)-(0.42+0.13*v)*np.cos(30))
    return speed


y_0 = 0
h = 0.01
t_0 = 0
t_N = 10


y_list, t_list = full_Euler(h, g, y_0, t_0, t_N)
plt.plot(t_list, y_list, label="Numerical", linewidth=1)


# Making the plot look nice
plt.legend()
plt.title("Speed of brick")
plt.xlabel(r'$s$ [time]')
plt.ylabel(r'$m/s$ [speed]')
plt.show()
