class BankAccount:
    # 1. The __init__ sets up the attributes when we create the account
    def __init__(self, owner_name, starting_balance):
        self.owner_name = owner_name
        self.__balance = starting_balance  # The double __ makes it private!

    # 2. deposit is an ACTION, so it's a method inside the class
    def deposit(self, amount):
        self.__balance += amount           # Add to the private balance
        print(f"Deposit successful! Your final balance is = {self.__balance}")

# --- How we use it ---
# We create ONE object:
my_account = BankAccount("John Doe", 100)

# We call the method on that object:
my_account.deposit(50) 
# Output: Deposit successful! Your final balance is = 150