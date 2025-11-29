# Multilevel Inheritance: Person → Student → Exam

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Derived class from Person
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        print("Course:", self.course)


# Derived class from Student
class Exam(Student):
    def __init__(self, name, age, course, m1, m2, m3):
        super().__init__(name, age, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.total = m1 + m2 + m3

    def display_exam(self):
        print("Marks:", self.m1, self.m2, self.m3)
        print("Total Marks:", self.total)


# Creating an object of Exam class with sample data
student1 = Exam("Pratima", 18, "BCA", 85, 90, 88)

# Displaying all details
student1.display_person()
student1.display_student()
student1.display_exam()
