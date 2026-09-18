# A short way to create a list

#normal
nums = []

for i in range(1,6):
 nums.append(i)

print(nums)

# short way   = List comprehension


nums = [i for i in range(1,6)]
print(nums)


even = [i for i in range(10) if i%2==0]

print(even)