class BankAccount:
       
    #Constructor runs when an object is created.
    def __init__(self, balance):  
        self.__balance = balance  #We make balance private.

     #how money is deposited.
    def deposit(self, amount): 

        if amount  > 0:
            self.__balance += amount
            print("Money deposited")
        else:
            print("Invalid amount")

      #withdrawal
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount
            print("Money withdrawn")


    def get_balance(self):
        return self.__balance


account = BankAccount(10000)

account.deposit(5000)

account.withdraw(3000)

print("Balance:", account.get_balance())

