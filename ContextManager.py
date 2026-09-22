
#Context Manager is used when you need to start something, use it, and automatically clean it up

#Without Context Manager
# file = open("dataz.txt", "r")

# data = file.read()
# print(data)

# file.close()


#With Context Manager

with open("data.txt", "r") as file:
    data = file.read()
    print(data)



#     with                   
#      ↓
#   Open file
#      ↓
#  Run code inside block
#      ↓
#   Close file automatically


