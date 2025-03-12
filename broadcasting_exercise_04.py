import numpy as np

# Generate temperatures (3 cities, 12 months, 2 years)
temps = np.random.randint(15, 35, (3, 12, 2))

# Convert to Fahrenheit
temps_fahrenheit = temps * 9/5 + 32

print("Temperatures in Fahrenheit:\n", temps_fahrenheit)
