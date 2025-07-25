import numpy as np
import matplotlib.pyplot as plt

print("Radioactive Decay Simulator v1.0")

# User Input
N0 = float(input("Initial number of atoms:\n")) # Initial number of atoms
half_life = float(input("Half-life:\n")) # Half-life (In days or years)
dt = 0.01 # Step size

# Derived Parameters
decay_const = np.log(2) / half_life
T_max = 10 * half_life

# Data Arrays
N_vals = [N0]
t_vals = [0]

while True:
	dN = -decay_const * N_vals[-1] * dt
	
	N_new = N_vals[-1] + dN
	t_new = t_vals[-1] + dt
	
	if t_new > T_max:
		break # Stop when the current time crosses total time
	
	t_vals.append(t_new)
	N_vals.append(N_new)

# Plot Customization
plt.title("Radioactive Decay")
plt.xlabel("Time")
plt.ylabel("Number of Atoms")
plt.grid(True)

# Results
plt.plot(t_vals, N_vals)
plt.show()