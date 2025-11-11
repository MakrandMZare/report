import numpy as np
import scipy.integrate as integrate

x = np.array([0.0, 0.125, 1.0, 2.0])
y = np.array([0.49671415, 0.1382643, 0.64768854, 1.52302986])

cum_simp = integrate.cumulative_simpson(y, x=x, initial=0)
print(f"Cumulative Simpson: {cum_simp}")
# Output: [ 0.          0.03856317 -0.00276498  1.05653714]

# Note: cum_simp[2] < 0 and cum_simp[2] < cum_simp[1], violating monotonicity