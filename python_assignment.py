#!/usr/bin/env python3
"""Python & Bash assignment: grade checker, student dictionary, and file handling."""

def grade_checker():
    print("\n=== Grade Checker ===")
    try:
        score = float(input("Enter score (0-100): "))
        if score < 0 or score > 100:
            print("Please enter a score between 0 and 100.")
        elif score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
    except ValueError:
        print("Invalid input. Please enter a number.")

def student_grades():
    print("\n=== Student Grades ===")
    students = {"Aarav": "A", "Diya": "B", "Rahul": "C"}
    print("Initial student records:", students)
    action = input("Choose action (add/update/show): ").strip().lower()

    if action == "add":
        name = input("Enter student name: ").strip()
        grade = input("Enter grade: ").strip().upper()
        if name in students:
            print("Student already exists. Choose update instead.")
        else:
            students[name] = grade
            print(f"Added {name} with grade {grade}.")
    elif action == "update":
        name = input("Enter student name to update: ").strip()
        if name in students:
            grade = input("Enter new grade: ").strip().upper()
            students[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print("Student not found.")
    elif action == "show":
        print("All student grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    else:
        print("Invalid action. Please choose add, update, or show.")

    print("Current student dictionary:", students)

def write_to_file():
    print("\n=== Write to a File ===")
    content = "Python file handling practice.\nThis text was written using open() and write().\n"
    with open("student_notes.txt", "w", encoding="utf-8") as file:
        file.write(content)
    print("Content successfully written to student_notes.txt")
    print("Written content:")
    print(content, end="")

def read_from_file():
    print("\n=== Read from a File ===")
    with open("student_notes.txt", "r", encoding="utf-8") as file:
        content = file.read()
    print("File content:")
    print(content, end="")

def main():
    grade_checker()
    student_grades()
    write_to_file()
    read_from_file()

if __name__ == "__main__":
    main()
