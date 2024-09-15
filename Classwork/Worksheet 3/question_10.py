class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_attributes(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")

student1 = Student(102323006, "Arin Goyal", "2nd year")
student2 = Student(102324116, "Akshat", "1st year")

print("Attributes of student1:")
student1.display_attributes()

print()

print("Attributes of student2:")
student2.display_attributes()
