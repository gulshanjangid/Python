class Animal1:
    def sound(self):
        print("Animal1 sound")
 


class Dog(Animal1):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()