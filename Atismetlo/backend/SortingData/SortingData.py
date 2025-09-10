class SortingData:
    """ TODO: app osztály """

    @staticmethod
    def sort_file(input_file: str, output_file: str, algorithm: SortAlgorithm):
        data = FileProcessor.read_file(input_file)

        if data:
            sorted_data, duration = ExecutionTimer.measure_time(algorithm.sort, data)
            FileProcessor.write_file(output_file, sorted_data)
            print(f"Rendezés {algorithm.__class__.__name__}-vel: {duration:.6f} mp")
