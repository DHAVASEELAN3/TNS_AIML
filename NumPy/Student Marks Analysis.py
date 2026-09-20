import numpy as np

marks = np.array([85, 72, 90, 65, 78, 95, 60, 88, 74, 82])

print("Marks:", marks)

print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

print("Marks greater than 75:", marks[marks > 75])
