#Grade Tracker
grades = {
    "John": 85,
    "Sarah": 92,
    "Mike": 78,
    "Emma": 95
}

print("Students and Grades")

for name, grade in grades.items():
    print(f"{name}: {grade}")

average = sum(grades.values()) / len(grades)

highest = max(grades.values())

print(f"\nAverage Grade: {average}")
print(f"Highest Grade: {highest}")

for name, grade in grades.items():
    if grade == highest:
        print(f"Top Student: {name}")

