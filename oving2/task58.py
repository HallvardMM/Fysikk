# Importing the necessary libraries
# NumPy is used to generate arrays and tp perform some mathematical operations
import numpy as np
import matplotlib.pyplot as plt  # Used for plotting results

def step_Euler(y, h, f):
    next_y = y + h * f(y)
    return next_y


def full_Euler(h, f, y_0=1, start_t=0, end_t=1):
    N = int((end_t - start_t) / h)
    t_list = np.linspace(start_t, end_t, N + 1)
    y_list = np.zeros(N + 1)
    y_list[0] = y_0
    for i in range(0, N):
        y_list[i + 1] = step_Euler(y_list[i], h, f)
    return y_list, t_list

# Input parameters
v_0 = 1.5  
h = 0.01  
t_0 = 0  
t_N = 10 

def v(vel):
    value = -3*vel**2
    return value

y_list, t_list = full_Euler(h, v, v_0, t_0, t_N)
plt.plot(t_list, y_list, label="Numerical", linewidth=1)

# Making the plot look nice
plt.legend()
plt.title("Euler for a=-kv^2")
plt.xlabel(r'$t$ [time]')
plt.ylabel(r'$y$ [velocity]')
plt.show()