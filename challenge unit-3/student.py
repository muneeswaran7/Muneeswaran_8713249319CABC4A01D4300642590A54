def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Define a Student class for testing
class Student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Test the function with a list of student objects
students = [
    Student("Alice", "A001", 3.9),
    Student("Bob", "B002", 3.7),
    Student("Charlie", "C003", 3.5),
    Student("David", "D004", 4.0),
]

sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
