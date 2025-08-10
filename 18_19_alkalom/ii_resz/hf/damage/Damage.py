class Damage:
    def __init__(self, base_damage: tuple[int, int], level):
        self.base_damage: tuple[int, int] = base_damage
        self.level = level

    def calcalute_damage(self):
        return randint(self.base_damage[0], self.base_damage[1]) + self.level

    def __add__(self, other: Damage):
        if isinstance(other, Damage):
            new_base_damage = (
                self.base_damage[0]
                + other.base_damage[0],
                self.base_damage[1],
                + other.base_damage[1]
            )
            return Damage(new_base_damage, self.level + other.level)
        return NotImplemented