import math
import os
import matplotlib.pyplot as plt
import numpy as np

# rad = float(input("Enter the radius of a circle: "))
# num_dim = int(input("Enter the number of dimensions of the sphere: "))
def calculate(num_dim, rad):
	return (((np.pi) ** (num_dim/2)) * (rad**num_dim)) / math.gamma(num_dim / 2 + 1)

dimensions = np.arange(0, 51)
# Create an array of radii from 1 to 2 in increments of 0.05
radii = np.arange(1, 2.05, 0.05)
"""
fig = plt.figure()
ax = plt.axes(projection='3d')
volumes = []
for dim in dimensions:
    for radius in radii:
        volume = calculate(dim, radius)
        volumes.append((dim, radius, volume))
        
volumes = np.array(volumes)

# Separate the data for plotting
dimensions, radii, volumes = volumes[:, 0], volumes[:, 1], volumes[:, 2]
ax.scatter(dimensions, radii, volumes, c=volumes, cmap='viridis', marker='o')

ax.set_xlabel('Dimensions')
ax.set_ylabel('Radii')
ax.set_zlabel('Volume')

# Set the title
ax.set_title('Volume of n-dimensional Spheres')
"""

# Create subplots for 4 rows and 5 columns (total 20 plots)
fig, axs = plt.subplots(3, 7, figsize=(10, 6))
fig.subplots_adjust(hspace=1.0, wspace=1.0)

# Flatten the axs array for easier indexing
axs = axs.flatten()


for i, radius in enumerate(radii):
    # Calculate volumes for the current radius
    volumes_fixed_radius = [calculate(dim, radius) for dim in dimensions]
    
    # Plot the volume vs. dimensions
    axs[i].plot(dimensions, volumes_fixed_radius)
    axs[i].set_title(f'Radius {radius:.2f}', fontsize=8)

fig.text(0.52, 0.01, 'Dimensions', ha='center', va='center', fontsize=10)
fig.text(0.015, 0.5, 'Volume', ha='center', va='center', rotation='vertical', fontsize=10)

plt.tight_layout()

plt.show()

