

#Normal way  , Suppose we want squares of numbers:
numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num * num)

print(squares)

#Using List Comprehension
# [what you want    for each item    in where]

numbers = [1, 2, 3, 4, 5]

# squares = [num * num for num in numbers]
squares =[x * 2 for x in numbers]

print(squares)


#List Comprehension with if
numbers = [1, 2, 3, 4, 5, 6]

even = [num for num in numbers if num % 2 == 0]

print(even)


