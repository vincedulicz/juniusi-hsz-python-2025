class Mage(Hero):
    def __init__(self, name: str, hp: int, level: int):
        super().__init__(name, hp, level)
        self.damage = Damage((15, 25), self.level)

    def attack(self) -> int:
        damage = self.damage.calculate_damage()
        print(f'{self.name} casts a spell, dealing {damage} damage')
        return damage
