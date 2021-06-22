import numpy as np
import matplotlib.pyplot as plt  

t_novac = np.genfromtxt("tnonvacuum.txt")
x_novac = np.genfromtxt("xnonvacuum.txt")
t_vac = np.genfromtxt("tvacuum.txt")
x_vac = np.genfromtxt("xvacuum.txt")

plt.plot(t_novac,x_novac,label="position")
plt.title("Position/time no vacuum")
plt.xlabel(r'$t$ [time]')
plt.ylabel(r'$y$ [height]')
plt.show()

v_novac=np.diff(x_novac)/np.diff(t_novac)
v_novac = np.append(v_novac,v_novac[v_novac.size-1])

plt.plot(t_novac,v_novac,label="speed")
plt.title("Speed/time no vacuum")
plt.xlabel(r'$t$ [time]')
plt.ylabel(r'$y$ [Speed]')
plt.show()

plt.plot(t_vac,x_vac)
plt.title("Position/time vacuum")
plt.xlabel(r'$t$ [time]')
plt.ylabel(r'$y$ [height]')
plt.show()


v_vac=np.diff(x_vac)/np.diff(t_vac)
v_vac = np.append(v_vac,v_vac[v_vac.size-1])


plt.plot(t_vac,v_vac)
plt.title("Speed/time vacuum")
plt.xlabel(r'$t$ [time]')
plt.ylabel(r'$y$ [Speed]')
plt.show()