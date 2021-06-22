# Importing the necessary libraries
# NumPy is used to generate arrays and tp perform some mathematical operations
import numpy as np
import matplotlib.pyplot as plt  # Used for plotting results

# Updating figure params
# Note, this is not important for any of the code, this is just to set the appropiate figure and text sizes
newparams = {'figure.figsize': (15, 7), 'axes.grid': False,
             'lines.markersize': 10, 'lines.linewidth': 2,
             'font.size': 15, 'mathtext.fontset': 'stix',
             'font.family': 'STIXGeneral', 'figure.dpi': 200}
plt.rcParams.update(newparams)


def step_Euler(y, h, f):
    """This Python function performs a single step of Euler's method.

    Parameters:
            y: Numerical approximation of y at time t
            h: Step size
            f: RHS of our ODE (RHS = Right hand side). Can be any function that only has y as a variable.
        Returns:
            next_y: Numerical approximation of y at time t+h
    """
    next_y = y + h * f(y)
    return next_y


def full_Euler(h, f, y_0=1, start_t=0, end_t=1):
    """  A full numerical aproximation of an ODE in a set time interval. Performs consecutive Euler steps
    with step size h from start time until the end time. Also takes into account the initial values of the ODE

    Parameters:
            h: Step size
            f: RHS of our ODE
            y_0 : Initial condition for y at t = start_t
            start_t : The time at the initial condtion, t_0
            end_t : The end of the interval where the Euler method is perfomed, t_N
        Returns:
            y_list: Numerical approximation of y at times t_list
            t_list: Evenly spaced discrete list of time with spacing h. 
                    Starting time = start_t, and end time = end_t 
    """
    # Number of discretisation steps
    N = int((end_t - start_t) / h)
    # Following the notation in the theory, we have N+1 discrete time values linearly spaced
    t_list = np.linspace(start_t, end_t, N + 1)

    # Initialise array to store y-values
    y_list = np.zeros(N + 1)
    # Assign initial condition to first element
    y_list[0] = y_0

    # Assign the rest of the array using N Euler_steps
    for i in range(0, N):
        y_list[i + 1] = step_Euler(y_list[i], h, f)
    # With N + 1 time values, we are only able to calculate N values of y. Thus we do not return the last element of
    # our time list. We accomplish this by writing t_list[:-1]
    return y_list, t_list


def g(y):
    """Defines the right hand side of our differential equation. In our case of bacterial growth, g(y) = k*y

    Parameters:
            y: Numerical approximation of y at time t
        Returns:
            growth_rate: Current population size multiplied with a constant of proportionality. In this case this is 
            equal to ln(2)
    """
    growth_rate = np.log(2)*y
    return growth_rate

# Now we can find the the numerical results from Euler's method and compare them to the analytical solution


# Input parameters
y_0 = 1  # Initial population size, i.e. a single bacteria
h = 0.01  # Step size
t_0 = 0  # We define the time at our initial observation as 0
t_N = 10  # 10 days after our initial observation of a single bacteria


# Calculating results from Euler and plotting them
y_list, t_list = full_Euler(h, g, y_0, t_0, t_N)
plt.plot(t_list, y_list, label="Numerical", linewidth=1)

# Plotting the analytical solution derived earlier
plt.plot(t_list, np.power(2, t_list), label="Analytical", linewidth=1)

# Making the plot look nice
plt.legend()
plt.title("The population size of a bacterial colony as a function of time")
plt.xlabel(r'$t$ [days]')
plt.ylabel(r'$y$ [# bacteria]')
plt.show()

# Let's see how far off our numerical approximation is after 5 days.

# Extracting the last element of the analytical solution
last_analytical = np.power(2, t_list[-1])
# Extracting the last element of the numerical solution
last_numerical = y_list[-1]

print("After 10 days, our numerical approximation of bacterias is off by: %.2f" %
      (last_analytical - last_numerical))


def r(y):
    """Defines the right hand side of our new differential equation. In our case of 
    bacterial growth, h(y) = k*y*(1-y/m). In this case, we set k = 1, and m = 100.

    Parameters:
            y: Numerical approximation of y at time t
        Returns:
            growth_rate: The current growth rate for a population with population = y
    """
    k = 1
    m = 100
    growth_rate = k * y * (1 - y / m)
    return growth_rate


# Input parameters

y_0 = 1  # Initial population size
h = 0.01  # Step size
t_0 = 0  # We define the time at our initial observation as 0
t_N = 10  # 10 days after our initial observation of a single bacteria


# Calculating results from Euler and plotting them
y_list, t_list = full_Euler(h, r, y_0, t_0, t_N)
plt.plot(t_list, y_list)


# Making the plot look nice
plt.title("The population size of a bacterial colony as a function of time using the logistic growth model")
plt.xlabel(r'$t$ [days]')
plt.ylabel(r'$y$ [# bacteria]')
plt.show()
