#generator is a special function that gives values one by one, instead of creating all values at once.



# normal  function
def nums():
    return [1,2,3,4,5]

rs  = nums()

print(rs)

#Generator

def  nums():
    yield 1
    yield 2
    yield 3
    yield 4

rs  = nums()
print(next(rs))
print(next(rs))
print(next(rs))
print(next(rs))



#Generator with for Loop
def nums():
    yield 1             
    yield 2
    yield 3
    yield 4
    yield 5

for num in nums():
    print(num)



# Generator
#    ↓
# yield 1
#    ↓
# pause
#    ↓
# yield 2
#    ↓
# pause
#    ↓
# yield 3



# Generator with Loop
def nums():
    for i in range(1,6):
        yield i

    for num in nums():
        print(num)






