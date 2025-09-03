from orai_f_25.orai_feladat.Accountable.Accountable import Accountable

class Person:
    """
    TODO: property
    Represents a person with basic attributes and banking functionality.
    """

    def __init__(self, name: str, age: int, person_id: str, country: str) -> None:
        """
        Initialize a person with name, age, ID, and country.
        """
        self.name = name
        self.age = age
        self.person_id = person_id
        self.country = country
        self.account_number = None

    @property
    def full_name(self) -> str:
        """
        Get the person's full name and age.
        """
        return f'{self.name} ({self.age} éves)'

    def greet(self) -> None:
        """
        Print a greeting message for the person.
        """
        print(f'Hello! {self.name} üdv a rendszerben')

    def open_bank_account(self, bank: Accountable, initial_balance: float = 0) -> None:
        """
        Open a bank account for the person.
        """
        if self.account_number:
            print(f'{self.name} már rendelekzik számlával')
        else:
            self.account_number = f'ACC-{self.person_id}'
            bank.create_account(self.account_number, initial_balance)
            print(f'{self.name} sikeresen nyitott bankszámlát')