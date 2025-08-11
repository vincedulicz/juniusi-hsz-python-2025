class Game:
    def __init__(self, question_handler: QuestionHandler):
        self._question_handler = question_handler
        self._correct_aswers = 0
        self._total_questions = 0

    def play(self):
        for _ in range(len(self._question_handler.definiton_provider.fogalmak)):
            valasz, correct_fogalom = self._question_handler.ask_question()

            if valasz.lower() in ['end', "..."]:
                break

            self._total_questions += 1

            if self._question_handler.definiton_provider.check_answer(valasz, correct_fogalom):
                print("helyes")
                self._correct_aswers += 1
            else:
                print("rossz válasz")

    def display_result(self):
        pass

    def ask_for_new_game(self):
        response = input("szeretné e még akkor játszani vagy ? (i/n)").strip().lower()
        return response == "i"
