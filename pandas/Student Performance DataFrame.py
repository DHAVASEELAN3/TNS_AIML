import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Chandru", "Divya", "Ezhil", "Farhan", "Gokul", "Hari"],
    "Department": ["CSE", "ECE", "CSE", "IT", "EEE", "CSE", "IT", "ECE"],
    "Marks": [85, 72, 90, 65, 78, 95, 60, 82],
    "Attendance": [90, 85, 95, 75, 88, 92, 70, 80]
}

df = pd.DataFrame(data)

print("First 5 students:")
print(df.head())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nStudents who scored more than 75:")
print(df[df["Marks"] > 75])

print("\nStudents whose attendance is below 80%:")
print(df[df["Attendance"] < 80])

print("\nStudents sorted by marks:")
print(df.sort_values("Marks"))
