# Getter - >Used to get/read data.

# Setter = > Used to change/update data with validation.

class Student:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


student = Student(80)

print(student.get_marks())

student.set_marks(90)

print(student.get_marks())




# Private Data
#      ↓
# Getter / Setter
#      ↓
# Validation
#      ↓
# Safe Data