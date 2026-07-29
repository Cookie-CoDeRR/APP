from abc import ABC, abstractmethod
from pickle import NONE

class paymentstrategy(ABC):
    @abstractmethod
    def payment(self,amount):
        pass

class cash_payment(paymentstrategy):
    def payment(self,amount):
        print(f"Payment ${amount} made in cash")
class card_payment(paymentstrategy):
    def payment(self,amount):
        print(f"Payment ${amount} made in card")
class UPI_payment(paymentstrategy):
    def payment(self,amount):
        print(f"Payment ${amount} made in UPI")
class Netbanking_payment(paymentstrategy):
    def payment(self,amount):
        print(f"Payment ${amount} made in Netbanking")

class PaymentProcessor():
    def __init__(self, strategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy=strategy

    def process_payment(self,amount):
        if self.strategy is None:
            print("No payment strategy set. Please set a payment strategy before processing payment.")
        else:
            self.strategy.payment(amount)

processor = PaymentProcessor()

while True:
        print("*"*37)
        print("===== Payment Processing System =====")
        print("*"*37)
        print("1. Cash Payment")
        print("2. Card Payment")
        print("3. UPI Payment")
        print("4. Net Banking")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            print("*"*37)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        except KeyboardInterrupt:
            print("\nExiting the Payment System. Goodbye!")
            break

        if choice == 5:
            print("Thank you for using the Payment System!")
            break

        try:
            amount = float(input("Enter payment amount: "))
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")
            continue
        except TypeError:
            print("Invalid amount! Please enter a numeric value.")
            continue

        if choice == 1:
            processor.set_strategy(cash_payment())
        elif choice == 2:
            processor.set_strategy(card_payment())
        elif choice == 3:
            processor.set_strategy(UPI_payment())
        elif choice == 4:
            processor.set_strategy(Netbanking_payment())
        else:
            print("Invalid choice!")
            continue

        processor.process_payment(amount)

