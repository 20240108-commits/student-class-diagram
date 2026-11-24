class Student:
    def __init__(self, student_id, name, surname, department, gpa):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.department = department
        self.gpa = gpa

    def get_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name, self.surname)
        print("Department:", self.department)
        print("GPA:", self.gpa)

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa


student1 = Student(
    20240986,
    "Emre",
    "Zengin",
    "Software Engineering",
    2.75
)

student1.get_info()

student1.update_gpa(3.00)

print("\nAfter GPA Update:")
student1.get_info()
