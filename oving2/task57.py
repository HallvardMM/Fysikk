import numpy as np
import matplotlib.pyplot as plt  

def f(x):
    return (x-1)/(x+1)

n = np.linspace(0, 1000, 1000)
xvalues = [f(x) for x in n]

plt.plot(n,f(n) )
plt.legend()
plt.title("a/gsin(theta)")
plt.xlabel(r'n')
plt.ylabel(r'a')
plt.show()