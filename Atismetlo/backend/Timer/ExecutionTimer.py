class ExecutionTimer:
    @staticmethod
    def measure_time(func: Callable, data: List) -> tuple:
        start = time.perf_counter()
        result = func(data)
        end = time.perf_counter()

        return result, end - start