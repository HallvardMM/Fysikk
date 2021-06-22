import numpy as np
import matplotlib.pyplot as plt  # Used for plotting results

m = 0.01  # kg
k = 0.1  # N/m
b = 0.001  # Ns/m
A = 0.019  # Amplitude
theta = -1.007  # rads
omega = np.sqrt(k/m)
P = 2*np.pi/omega
dt = P/2000
print(1/dt)
T = 4*P
N_t = int(round(T/dt))
print(N_t)
t = np.linspace(0, N_t*dt, N_t+1)


u = np.zeros(N_t+1)
v = np.zeros(N_t+1)

# Initial condition
X_0 = 0.01
u[0] = X_0
v[0] = 0.05

# Step equations forward in time
for n in range(N_t):
    u[n+1] = u[n] + dt*v[n]
    v[n+1] = v[n]*(1-(dt*(b/m))) - dt*omega**2*u[n]

fig = plt.figure()
l1 = plt.plot(t, u, 'b-')
fig.legend((l1), ('numerical'), 'upper left')
plt.xlabel('t')
plt.show()
