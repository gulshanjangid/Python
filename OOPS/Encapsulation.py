# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def get_balance(self):
#         return self.__balance


# account = BankAccount(5000)

# account.deposit(1000)

# print(account.get_balance())




class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age


student = Student("Gulshan", 22)

print(student.get_name())
print(student.get_age())

student.set_age(23)

print(student.get_age())
