class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the list of students based on their CGPA in descending order
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Test the function with a list of student objects
students = [
  Student("Alice", "S001", 3.8),
  Student("Bob", "S002", 3.6),
  Student("Charlie", "S003", 3.9),
  Student("David", "S004", 3.7),
]

sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
