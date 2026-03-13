# Internship Task 7: Dictionaries & JSON Handling (Compact Output Version)

import json

# 1. Dictionary of student details
students = {
    "S101": {"name": "Amit", "age": 20, "grades": [88, 92, 79]},
    "S102": {"name": "Riya", "age": 21, "grades": [90, 85, 95]},
    "S103": {"name": "Sara", "age": 19, "grades": [78, 82, 88]}
}

# 2. Original records
print("Original Records:")
for sid, info in students.items():
    print(f"{sid}: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")

# 3. Update & delete
students["S102"]["age"] = 22
del students["S103"]

print("\nAfter Update/Delete:")
for sid, info in students.items():
    print(f"{sid}: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")

# 4. Loop through dictionary (compact)
print("\nLooping Records:")
for sid, info in students.items():
    print(f"{sid} -> Name: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")

# 5. Convert dictionary to JSON string
students_json = json.dumps(students, indent=2)
print("\nJSON Format:")
print(students_json)

# 6. Save JSON to file
with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

# 7. Load JSON back
with open("students.json", "r") as f:
    loaded_students = json.load(f)

print("\nLoaded from JSON:")
for sid, info in loaded_students.items():
    print(f"{sid}: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")