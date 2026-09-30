class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class PayPalPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


class UPIPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


def run_payment_demo():
    payment_methods = {
        1: CreditCardPayment,
        2: PayPalPayment,
        3: UPIPayment,
    }

    print("Select a payment method")
    print("1. Credit Card")
    print("2. PayPal")
    print("3. UPI")

    choice = int(input("Enter your choice: "))
    amount = int(input("Enter the amount: "))

    payment_method = payment_methods.get(choice)
    if payment_method is None:
        print("Invalid payment choice")
        return

    processor = PaymentProcessor(payment_method())
    processor.make_payment(amount)


if __name__ == "__main__":
    run_payment_demo()