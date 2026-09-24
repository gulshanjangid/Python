class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks):

        super().__init__(name)

        self.marks = marks


student = Student("Gulshan", 85)

print(student.name)
print(student.marks)