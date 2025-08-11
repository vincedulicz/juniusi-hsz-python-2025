class CharacterDataManager:
    def __init__(self, filename: str):
        self.filename: str = filename

    def read_data(self) -> list[dict]:
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def write_data(self, data: list[dict]) -> None:
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_character(self, name: str, character_type: str, hp: int, level: int) -> None:
        character = {"name": name, "type": character_type, "hp": hp, "level": level}
        data = self.read_data()
        data.append(character)
        self.write_data(data)