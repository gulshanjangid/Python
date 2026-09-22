#decorator is a function that adds extra behavior to another function without changing its original code.


# Original function
#        ↓
#    Decorator
#        ↓
# Extra functionality


def decorator_function(orginal_function):

    def wrapper():
        print("function started")

        orginal_function()

        print("function ended")

    return wrapper
@decorator_function
def hello():
    print("hello gulshan")

# hello = decorator_function(hello)
# means => 
# hello function
#       ↓
# decorator_function
#       ↓
# wrapper function
#       ↓
# hello now points to wrapper

hello()







#Decorator with Arguments

def decorator_function(original_function):

    def wrapper(name):
        print("Before function")

        original_function(name)

        print("After function")

    return wrapper

@decorator_function
def greet(name):
    print(f"Hello {name}")


greet("Gulshan")




#Decorator for Authentication

# User requests API
#        ↓
# Check authentication
#        ↓
# Authenticated?
#    ↓          ↓
#  Yes          No
#  ↓             ↓
# Run API      Reject



def login_required(func):
    def wrapper(user):
        if user == "Gulshan":
            return func(user)
        else:
            print("access denied")

    return wrapper

@login_required
def home_page(user):
    print("welcome gulshan")

home_page("gulshan")
