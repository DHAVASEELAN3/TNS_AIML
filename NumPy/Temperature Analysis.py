import numpy as np

temperature = np.array([28, 31, 29, 33, 35, 30, 32])

print("Temperature:", temperature)

print("Average Temperature:", np.mean(temperature))
print("Highest Temperature:", np.max(temperature))
print("Lowest Temperature:", np.min(temperature))

print("Temperatures above 30°C:", temperature[temperature > 30])

updated_temperature = temperature + 2

print("Updated Temperature:", updated_temperature)
