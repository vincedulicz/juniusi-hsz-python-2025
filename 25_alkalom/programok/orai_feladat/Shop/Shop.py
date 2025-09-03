from orai_f_25.orai_feladat.Accountable.Accountable import Accountable
from orai_f_25.orai_feladat.Person.Person import Person

class Shop:
    def __init__(self):
        self.invetory: dict[str, float] = {}

    def add_item(self, item_name: str, price: float):
        self.invetory[item_name] = price

    def buy_item(self, person: Person, bank: Accountable, item_name: str):
        if item_name not in self.invetory:
            print(f'{item_name} nem kapható')
        elif not person.account_number:
            print(f'{person.name} nem rendelkezik számlával')
        else:
            price = self.invetory[item_name]
            if bank.customers.get(person.account_number, 0) >= price:
                bank.make_withdrawal(person.account_number, price)
                print(f'{person.name} megvette a(z) {item_name} terméket {price} áron')
            else:
                print("Nincs elegendő egyenleg...")