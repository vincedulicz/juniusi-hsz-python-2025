from orai_f_25.orai_feladat.Bank.Bank import Bank
from orai_f_25.orai_feladat.Person.Person import Person
from orai_f_25.orai_feladat.Shop.Shop import Shop

def main():
    bank = Bank()

    person1 = Person("János", 30, "12345", "HU")
    person1.greet()
    person1.open_bank_account(bank, initial_balance=1000)

    shop = Shop()
    shop.add_item("laptop", 500)
    shop.add_item("telefon", 300)
    shop.add_item("drága", 10000000)

    shop.buy_item(person1, bank, "laptop")
    shop.buy_item(person1, bank, "telefon")

    bank.check_balance(person1.account_number)

    shop.buy_item(person1, bank, "drága")

    bank.check_balance(person1.account_number)


main()
