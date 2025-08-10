class Battle:
    def __init__(self, hero: Hero, hero_other: Hero):
        if isinstance(hero, Hero) and isinstance(hero_other, Hero):
            self.hero = hero
            self.hero_other = hero_other
        else:
            raise NotImplementedError(f'Wrong type: {Hero} only!!44!!')

    def start_battle(self):
        print("start....")

        while self.hero.is_alive() and self.hero_other.is_alive():
            self.hero_other.take_damage(
                self.hero.attack()
            )

            if self.hero_other.is_alive():
                self.hero.take_damage(
                    self.hero_other.attack()
                )

        if self.hero.is_alive():
            print(f'{self.hero.name} wins!')
        else:
            print(f'{self.hero_other} wins!')