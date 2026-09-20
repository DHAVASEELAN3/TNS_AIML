import matplotlib.pyplot as plt

students = ["Arun", "Bala", "Chandru", "Divya", "Ezhil",
            "Farhan", "Gokul", "Hari", "Ishan", "Jaya"]

marks = [85, 72, 90, 65, 78, 95, 60, 35, 50, 88]

# Bar Chart
plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)

plt.show()


# Performance Categories
excellent = 0
good = 0
average = 0
needs_improvement = 0

for mark in marks:
    if mark >= 80:
        excellent += 1
    elif mark >= 60:
        good += 1
    elif mark >= 40:
        average += 1
    else:
        needs_improvement += 1

categories = ["Excellent", "Good", "Average", "Needs Improvement"]
count = [excellent, good, average, needs_improvement]

# Pie Chart
plt.pie(count, labels=categories, autopct="%1.1f%%")

plt.title("Student Performance Distribution")

plt.show()
