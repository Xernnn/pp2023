class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob
        self._marks = {}

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def add_marks(self, course_id, marks):
        self._marks[course_id] = marks

    def get_marks(self):
        return self._marks

class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._students = {}

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def add_student(self, student):
        self._students[student.get_id()] = student

    def get_students(self):
        return self._students

class School:
    def __init__(self):
        self._students = {}
        self._courses = {}

    def add_student(self, id, name, dob):
        student = Student(id, name, dob)
        self._students[id] = student

    def add_course(self, id, name):
        course = Course(id, name)
        self._courses[id] = course

    def add_student_to_course(self, student_id, course_id):
        student = self._students.get(student_id)
        course = self._courses.get(course_id)
        if student and course:
            course.add_student(student)
        else:
            print("Invalid student or course ID")

    def add_marks(self, student_id, course_id, marks):
        student = self._students.get(student_id)
        if student:
            student.add_marks(course_id, marks)
        else:
            print("Invalid student ID")

    def list_courses(self):
        print("List of Courses:")
        for course_id, course in self._courses.items():
            print(f"ID: {course.get_id()}, Name: {course.get_name()}")

    def list_students(self):
        print("List of Students:")
        for student_id, student in self._students.items():
            print(f"ID: {student.get_id()}, Name: {student.get_name()}, DoB: {student.get_dob()}")

    def show_student_marks(self, student_id):
        student = self._students.get(student_id)
        if student:
            print(f"Marks for student {student.get_name()}:")
            for course_id, marks in student.get_marks().items():
                course = self._courses.get(course_id)
                if course:
                    print(f"Course: {course.get_name()}, Marks: {marks}")
        else:
            print("Invalid student ID")

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB: ")
            self.add_student(id, name, dob)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.add_course(id, name)

    def input_student_to_course(self):
        while True:
            student_id = input("Enter student ID to add to a course (or 'quit' to exit): ")
            if student_id == 'quit':
                break
            course_id = input("Enter course ID to add the student to: ")
            self.add_student_to_course(student_id, course_id)

    def input_marks(self):
        while True:
            student_id = input("Enter student ID to add marks for (or 'quit' to exit): ")
            if student_id == 'quit':
                break
            course_id = input("Enter course ID to add marks for: ")
            marks = int(input("Enter marks for the student: "))
            self.add_marks(student_id, course_id, marks)

    def run(self):
        self.input_students()
        self.input_courses()
        self.input_student_to_course()
        self.input_marks()
        self.list_courses()
        self.list_students()
        student_id = input("Enter student ID to show marks for: ")
        self.show_student_marks(student_id)

school = School()
school.run()