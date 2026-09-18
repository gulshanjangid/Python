
# *args 

# def add(*numbers):
#     print(numbers)

# add(10, 20, 30)


def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add(10, 20, 30))



# What are **kwargs?
# **kwargs accepts multiple keyword arguments.

def s(**data):
    print(data)

s(name="Gulshan", age=25)

#lambda function
#A lambda is a small one-line function.
sq =lambda x:x*x

print(sq(3))