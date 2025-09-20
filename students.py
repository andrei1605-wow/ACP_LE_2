class student():
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else set {}
    def __str__(self):
        pass 
class StudentRecords:
    def __init__(self):
        self.students = []
    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        student = student(student_id, student_name, email, grades, courses)
        self.student.append(student)
        return "Student added successfully"
