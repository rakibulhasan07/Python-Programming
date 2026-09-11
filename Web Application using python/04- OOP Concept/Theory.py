class Student :
    def __init__(self, name, age, roll, grade, section, department, registration_number):
        self.name = name
        self.age = age
        self.roll = roll
        self.grade = grade
        self.section = section
        self.department = department
        self.registration_number = registration_number
Rakib = Student("Rakib", 20, 101, "A", "B", "CSE", "2021-001")
karim = Student("Karim", 21, 102, "B", "A", "EEE", "2021-002")
rahim = Student("Rahim", 22, 103, "C", "C", "BBA", "2021-003")