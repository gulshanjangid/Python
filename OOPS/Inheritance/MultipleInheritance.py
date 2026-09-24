#One child inherits from multiple parents.


# Father       Mother
#    \           /
#     \         /
#       Child


class Father :
    def father_feature(self):
        print("Father feature")

class Mother:
    def mother_feature(self):
        print("mother feature")

class Child(Father, Mother):
    def child_feature(self):
        print("Child feature")

child = Child()
child.father_feature()
child.mother_feature()
child.child_feature()




#Multiple Inheritance Problem

#Suppose both parents have the same method.

#Python follows "MRO"
#  MRO — Method Resolution Order

class Father:

    def show(self):
        print("Father")

class Mother:

    def show(self):
        print("Mother")

class Child(Mother, Father):
    pass


child = Child()

child.show()




# Diamond Problem in Python

# The Diamond Problem happens in multiple inheritance when a child class gets the same method from two parent classes.


# The inheritance structure looks like a diamond:

#         A
#        / \
#       B   C
#        \ /
#         D

# Here, D inherits from both B and C, and both B and C inherit from A.
# Interview answer:

# The Diamond Problem occurs in multiple inheritance when a class inherits from two classes that have a common parent. Python solves this using MRO (Method Resolution Order) and the C3 linearization algorithm.

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass


obj = D()
obj.show()




# Diamond Problem
#       ↓
# Multiple Inheritance
#       ↓
# Same method exists in multiple classes
#       ↓
# Python uses MRO
#       ↓
# MRO decides which method runs




