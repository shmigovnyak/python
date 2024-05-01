class Wallet:
    payment_system = "МИР"

    def __init__(self, name: str, currency: str):
        if currency not in ["USD", "EUR", "RUB"]:
            raise ValueError("Неподдерживаемая валюта")
        self.name = name
        self.currency = currency
        self._balance = 0

    def top_up_balance(self, amount: float):

        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount
        print(f"Баланс пополнен на {amount} {self.currency}")

    def pay(self, amount: float):

        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if self._balance >= amount:
            self._balance -= amount
            print(f"Оплата в размере {amount} {self.currency} прошла успешна")
        else:
            print("Недостаточно средств")


    def info(self):

        print(f"Имя кошелька: {self.name}")
        print(f"Валюта: {self.currency}")
        print(f"Баланс: {self._balance} {self.currency}")

    def delete_account(self):

        del self


my_wallet = Wallet("Кошелечек", "RUB")

my_wallet.top_up_balance(10000)

my_wallet.info()

my_wallet.pay(5000000)

my_wallet.info()

my_wallet.delete_account()