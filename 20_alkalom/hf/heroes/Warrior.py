class Warrior(Hero):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)
        self.damage = Damage((10, 20), self.level)

    def attack(self):
        damage = self.damage.calcalute_damage()
        print("attackol... ")
        return damage