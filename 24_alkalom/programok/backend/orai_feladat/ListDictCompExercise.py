class ListDictComp:
    @staticmethod
    def square_numbers():
        print("négyzetek", [x ** 2 for x in range(1, 21)])

    @staticmethod
    def even_numbers():
        print("páros számok", [x for x in range(1, 51) if x % 2 == 0])

    @staticmethod
    def filter_non_divisible_by_3():
        print("nem osztható 3-al", [x for x in range(1, 21) if x % 3 != 0])

    @staticmethod
    def dict_square():
        print("dict négyzet", {x: x ** 2 for x in range(1, 11)})

    @staticmethod
    def update_dict():
        data = {"A": 10, "B": 20}
        data["C"] = 30
        data["A"] = 100
        print("modify data", data)

    @staticmethod
    def filter_dict():
        data = {"A": 10, "B": 20, "C": 30}
        szurt = {k: v for k, v in data.items() if v > 15}
        print("szűrt szótár", szurt)
