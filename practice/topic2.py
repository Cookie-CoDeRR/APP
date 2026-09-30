class Bankamount:
    def __init__(self, amount, balance):
        self.amount = amount
        self.__balance = balance

    @property
    # we read data but dont overwrite it
    def balance(self):
        return f"${self.__balance}"
    @classmethod
    # parase a string like alice-500
    def string(cls, string_data):
        name, amount = string_data.split("-")
        return cls(name, int(amount))

    @staticmethod
    def isvalid(amount):
        return amount > 0 

my_bank = Bankamount.string("Alice-500")
print(my_bank.balance)
my_bank.isvalid
