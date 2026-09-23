def fact(n):
    rs = 1

    for i in range(1, n+1):
        rs = rs * i

    return rs 

print(fact(5))
