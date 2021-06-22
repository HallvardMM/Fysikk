import numpy as np
import matplotlib.pyplot as plt  

fildata = np.genfromtxt("cupdata.txt",skip_header=2,delimiter=",")


print(fildata[:,0])

plt.plot(fildata[:,0],fildata[:,2])
plt.legend()
plt.title("Cupcape position per time")
plt.xlabel(r'$t$ [time]')
plt.ylabel(r'$y$ [height]')
plt.show()