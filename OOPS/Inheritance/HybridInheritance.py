#Hybrid inheritance means a combination of multiple types of inheritance.
#         Animal
#         /    \
#        Dog   Cat
#         \    /
#          Puppy


#   1 isinstance() with Inheritance


class Animal:
    pass

class Dog(Animal):
    pass

dog  = Dog()

print(isinstance(dog ,Dog))
print(isinstance(dog,Animal))



#Why is the second one True?

# Because:

#    Dog
#     ↓  inherits
#   Animal

#Dog object is also an Animal object.



#issubclass()

# issubclass() checks whether one class inherits from another.

class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))





# isinstance() → object relationship

# issubclass() → class relationship

