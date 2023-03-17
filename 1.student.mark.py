class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        print(f"List of students enrolled in {self.name}:")
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, DoB: {student.dob}")

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, student):
        self.students[student.id] = student

    def add_course(self, course):
        self.courses[course.id] = course

    def add_student_to_course(self, student_id, course_id):
        student = self.students.get(student_id)
        course = self.courses.get(course_id)
        if student and course:
            course.add_student(student)
        else:
            print("Invalid student or course ID")

    def add_marks(self, student_id, course_id, marks):
        student = self.students.get(student_id)
        if student:
            student.add_marks(course_id, marks)
        else:
            print("Invalid student ID")

    def list_students(self):
        print("List of Students:")
        for student_id, student in self.students.items():
            print(f"ID: {student.id}, Name: {student.name}, DoB: {student.dob}")

    def list_courses(self):
        print("List of Courses:")
        for course_id, course in self.courses.items():
            print(f"ID: {course.id}, Name: {course.name}")

    def show_student_marks(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"Marks for student {student.name}:")
            for course_id, marks in student.marks.items():
                course = self.courses.get(course_id)
                if course:
                    print(f"Course: {course.name}, Marks: {marks}")
        else:
            print("Invalid student ID")

school = School()

# Input number of students
num_students = int(input("Enter number of students: "))

# Input student information
for i in range(num_students):
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student DoB: ")
    student = Student(id, name, dob)
    school.add_student(student)

# Input number of courses
num_courses = int(input("Enter number of courses: "))

# Input course information
for i in range(num_courses):
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    course = Course(id, name)
    school.add_course(course)

# Add students to courses
while True:
    student_id = input("Enter student ID to add to a course (or 'quit' to exit): ")
    if student_id == 'quit':
        break
    course_id = input("Enter course ID to add the student to: ")
    school.add_student_to_course(student_id, course_id)

# Add marks for students in courses
while True:
    student_id = input("Enter student ID to add marks for (or 'quit' to exit): ")
    if student_id == 'quit':
        break
    course_id = input("Enter course ID to add marks for: ")
    marks = int(input("Enter marks for the student: "))
    school.add_marks(student_id, course_id, marks)

# Listing the functions
school.list_courses()
school.list_students()
student_id = input("Enter student ID to show marks for: ")
school.show_student_marks(student_id)