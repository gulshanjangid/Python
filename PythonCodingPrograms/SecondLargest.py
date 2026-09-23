nums = list(map(int, input("Enter nums: ").split()))

largest = float("-inf")
second = float("-inf")

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)