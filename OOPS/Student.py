class Student:

    # name = "Gulshan"
    # age = 25


    def __init__(self):
        print("Student object created")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)


student1 = Student("gulshan",22)
student1.show()
print(student1.name)
print(student1.age)
