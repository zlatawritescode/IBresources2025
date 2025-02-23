import numpy as np
import matplotlib.pyplot as plt

# Given data, insure proper sig fig treatment, and 5 levels, replace the values
x_values = np.array([8.29, 8.57, 8.86, 9.13, 9.39])  # x variable
y_values = np.array([93.14, 95.31, 96.17, 99.59, 107.57])  # y variable
y_errors = np.array([0.45, 0.54, 0.60, 0.94, 0.38])  # Vertical error bars

# Define the equations for the lines
x_fit = np.linspace(min(x_values) - 0.5, max(x_values) + 0.5, 100)  # Extended range for better visualization
best_fit = 13.1 * x_fit - 15.439
max_line = 14 * x_fit - 23.53
min_line = 12.36 * x_fit - 8.8744

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the data points with error bars, change colours to fit preferences
plt.errorbar(x_values, y_values, yerr=y_errors, fmt='o', color='black', ecolor='gray', capsize=5, label="Experimental Data")

# Plot the lines,  change colours to fit preferences
plt.plot(x_fit, best_fit, 'k-', label="Best-Fit Line: $y = 13.1x - 15.439$")
plt.plot(x_fit, max_line, 'r--', label="Max Slope: $y = 14x - 23.53$")
plt.plot(x_fit, min_line, 'b--', label="Min Slope: $y = 12.36x - 8.8744$")

# Labels and title
plt.xlabel("X (units)", fontsize=12)
plt.ylabel("Y (units)", fontsize=12)
plt.title("Relationship Between X and Y", fontsize=14)

# Grid and legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10)

# Show the plot
plt.show()
