students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91
}

print("Current student grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

new_student = input("\nEnter a new student name: ")
new_grade = float(input("Enter the grade: "))
students[new_student] = new_grade

update_student = input("\nEnter a student name to update: ")

if update_student in students:
    updated_grade = float(input("Enter the updated grade: "))
    students[update_student] = updated_grade
    print(f"{update_student}'s grade updated successfully.")
else:
    print(f"{update_student} was not found in the dictionary.")

print("\nAll student grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")
