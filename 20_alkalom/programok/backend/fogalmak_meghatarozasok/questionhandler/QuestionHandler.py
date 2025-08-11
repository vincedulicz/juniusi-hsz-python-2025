class QuestionHandler:
    def __init__(self, definiton_provider: DefinitionProvider):
        self.definiton_provider = definiton_provider

    def ask_question(self):
        meghatarozas, correct_fogalom = self.definiton_provider.get_definition()
        valasz = input("melyik fogalom társul hozzá:").strip()

        return valasz, correct_fogalom