class DefinitionDict(DefinitonProvider):
    def __init__(self, fogalmak, meghatarozasok):
        self.fogalmak = fogalmak
        self._meghatarozasok = meghatarozasok
        self._dictionary = self._create_dictionary()

    def _create_dictionary(self):
        return {meghatarzoas: fogalom for fogalom, meghatarzoas in zip(self.fogalmak, self._meghatarozasok)}

    def get_definiton(self):
        meghatarozas = choice(list(self._dictionary.keys()))
        return meghatarozas, self._dictionary[meghatarozas]

    def check_answer(self, user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.strip().lower()