nums = list(map(int,input("Enter a nums:").split()))

# User Input
#    ↓
# "10 45 23 89 12"
#    ↓  split()
# ["10", "45", "23", "89", "12"]
#    ↓  map(int)
# 10, 45, 23, 89, 12
#    ↓  list()
# [10, 45, 23, 89, 12]
#    ↓
# nums

ans = nums[0]

for num in nums:
    if  num > ans:
        ans = num
print("ans: ",ans)