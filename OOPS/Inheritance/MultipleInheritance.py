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
