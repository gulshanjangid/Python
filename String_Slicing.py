
# Slicing

name = "Gulshan"
#string[start:stop:step]

print(name[0:7:2])
# 0 → G
# 2 → l
# 4 → h
# 6 → n
print(name[::2])
# G u l s h a n
# ↑   ↑   ↑   ↑
# G   l   h   n

print(name[0])    
print(name[1])    
print(name[-1])   
print(name[-2])
print(name[:])   #Copy the Whole String
print(name[-3:])
print(name[1:])
print(name[::-1])  #Reverse a String

#  G   u   l   s   h   a   n
#  0   1   2   3   4   5   6
# -7  -6 -5   -4   -3  -2 -1   Negative indexing


phone = input("enter your phone :")

masked = "******" + phone[-4:]

print(masked)








