def main() -> None:
    file_manager = CharacterDataManager('characters.json')

    file_manager.add_character("Thor", "Warrior", 120, 8)
    file_manager.add_character("Merlin", "Mage", 85, 5)

    characters_data = file_manager.read_data()
    heroes: list[Hero] = []

    for character in characters_data:
        if character['type'] == 'Warrior':
            heroes.append(
                Warrior(
                    character['name'],
                    character['hp'],
                    character['level'])
            )
        elif character['type'] == 'Mage':
            heroes.append(
                Mage(
                    character['name'],
                    character['hp'],
                    character['level'])
            )
        elif character['type'] == 'Archer':
            heroes.append(
                Archer(
                    character['name'],
                    character['hp'],
                    character['level'])
            )

    battle = Battle(heroes[0], heroes[1])
    battle.start_battle()


main()