nums  = [1, 2, 3, 4, 5, 6, 7, 8]

even =[]
odd =[]

for  num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)


print("Even", even)
print("Odd", odd)
