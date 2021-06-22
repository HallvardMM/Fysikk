import numpy as np
import matplotlib.pyplot as plt

# Trimming av data før fall
t_novac = np.genfromtxt("tnonvacuum.txt")[400:]
x_novac = np.genfromtxt("xnonvacuum.txt")[400:]
# Trimming av data før fall og lik lengde
t_vac = np.genfromtxt("tvacuum.txt")[600:741]
x_vac = np.genfromtxt("xvacuum.txt")[600:741]

# find smallest number
min_t_novac = min(t_novac)
min_t_vac = min(t_vac)

# Starte på t=0
t_vac = [time - min_t_vac for time in t_vac]
t_novac = [time - min_t_novac for time in t_novac]


def andregrad(time, pvalues):
    returnarray = []
    for i in range(len(time)):
        returnarray.append(pvalues[0]*time[i]**2+pvalues[1]*time[i]+pvalues[2])
    return returnarray


v_novac = np.diff(x_novac)/np.diff(t_novac)
v_novac = np.append(v_novac, v_novac[v_novac.size-1])
p_novac = np.polyfit(t_novac, v_novac, 2)
print(p_novac)

v_vac = np.diff(x_vac)/np.diff(t_vac)
v_vac = np.append(v_vac, v_vac[v_vac.size-1])
p_vac = np.polyfit(t_vac, v_vac, 2)
print(p_vac)  # Verdier for 5bii)


plt.plot(t_vac, andregrad(t_vac, p_vac), 'g-', label="approx")
plt.plot(t_vac, v_vac, 'r-', label="values")
plt.plot(t_vac, np.multiply(t_vac, 9.81), 'b-', label="g*t")
plt.title("vacuum")
plt.legend()
plt.xlabel(r'$t$ [time]')
plt.ylabel(r'$y$ [Speed]')
plt.show()
