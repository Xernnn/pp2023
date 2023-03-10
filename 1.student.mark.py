class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Class:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students in the class: "))
        for i in range(num_students):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth (DD/MM/YYYY): ")
            student = Student(id, name, dob)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses offered: "))
        for i in range(num_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(id, name)
            self.courses.append(course)

    def list_courses(self):
        print("Courses offered:")
        for course in self.courses:
            print(f"{course.id}: {course.name}")

    def list_students(self):
        print("Students enrolled:")
        for student in self.students:
            print(f"{student.id}: {student.name}")

