# try:
#     a = 10/0

#     print(a)

# except ZeroDivisionError:
#     print("connot divide by zero")

# finally:
#     print("finished")


# try:
#     num = int(input("Enter a number: "))
#     print(num)

# except ValueError:
#     print("Please enter a valid number")


def divide_numbers():

    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        result = a / b

    except ValueError:
        print("Please enter numbers only")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    else:
        print("Result:", result)

    finally:
        print("Operation completed")


divide_numbers()


