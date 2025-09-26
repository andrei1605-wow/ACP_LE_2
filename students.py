class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else set()

    def __str__(self):
        return (f"ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}, "
                f"Grades: {self.grades}, Courses: {list(self.courses)}")

    def calculate_gpa(self):
        grade_to_gpa = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        total_points = 0
        count = 0
        for course, grade in self.grades.items():
            grade = grade.upper()
            if grade in grade_to_gpa:
                total_points += grade_to_gpa[grade]
                count += 1
        if count == 0:
            return "No grades available to calculate GPA"
        return round(total_points / count, 2)


class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        student = Student(student_id, student_name, email, grades, courses)
        self.students.append(student)
        return "Student added successfully"

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.student_id == student_id:
                if email is not None:
                    student.email = email
                if grades is not None:
                    student.grades.update(grades)
                if courses is not None:
                    student.courses.update(courses)
                return "Student updated successfully"
        return "Student not found"

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return "Student deleted successfully"
        return "Student not found"

    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.student_id == student_id:
                student.courses.add(course)
                return "Course enrolled successfully"
        return "Student not found"

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return str(student)
        return "Student not found"

    def search_by_name(self, name):
        name = name.lower()
        matches = [str(student) for student in self.students if name in student.student_name.lower()]
        return matches if matches else "No students found with that name"

records = StudentRecords()

records.add_student(1, "Andri", "andri@gmail.com", {"Math": "A", "Science": "B"})
records.add_student(2, "Bonjing", "bonj@gmail.com", {"Math": "C"})
records.add_student(3, "wow", "wow@gmail.com", {"History": "A"})

print(records.students[0].calculate_gpa()) 

print(records.search_by_name("andri"))
