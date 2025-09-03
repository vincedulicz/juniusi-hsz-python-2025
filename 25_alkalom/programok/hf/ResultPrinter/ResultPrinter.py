class ResultPrinter:
    @staticmethod
    def print_result(result: float, comparison_type: str):
        """ print comp. result """
        print(f'{comparison_type} hasonlóság a két fájl között: {result:.2f}%')
