from orai_f_25.orai_feladat.Accountable.Accountable import Accountable

class Bank(Accountable):
    # TODO: is_account_number_exists
    def __init__(self):
        self.customers: dict[str, float] = {}

    def create_account(self, account_number: str, initial_balance: float = 0) -> None:
        if account_number in self.customers:
            print("Account already exists")
        else:
            self.customers[account_number] = initial_balance
            print("Account created")

    def make_deposit(self, account_number: str, amount: float) -> None:
        if account_number in self.customers:
            self.customers[account_number] += amount
        else:
            print("Account number does not exist")

    def make_withdrawal(self, account_number: str, amount: float) -> None:
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal succesful")
            else:
                print("Not enough money")
        else:
            print("Account number does not exists")

    def check_balance(self, account_number: str) -> None:
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f'Balance: {balance}')
        else:
            print("Account does not exists")