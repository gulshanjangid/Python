with open("data.txt", "w") as file:
    file.write("heelo gulsha jangid ")

with open("data.txt", "r") as file:
    data = file.read()

print(data)