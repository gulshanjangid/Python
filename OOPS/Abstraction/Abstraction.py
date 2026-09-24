
#Show only what is necessary and hide the internal implementation.
# When you drive a car:

# You use steering
# You use brake
# You use accelerator

# But you don't need to know exactly how the engine internally works.

from abc import ABC, abstractmethod


class Animal(ABC):   #Animal is an abstract class.

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("dog says..")

class Cat(Animal):

    def sound(self):
        print("Cat says..")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


