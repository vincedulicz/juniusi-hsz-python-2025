class Archer(Hero):
    def __init__(self, name: str, hp: int, level: int):
        super().__init__(name, hp, level)
        self.damage = Damage((12, 18), self.level)

    def attack(self) -> int:
        damage = self.damage.calculate_damage()
        print(f'{self.name} shoots an arrow, dealing {damage} damage!')
        return damage
