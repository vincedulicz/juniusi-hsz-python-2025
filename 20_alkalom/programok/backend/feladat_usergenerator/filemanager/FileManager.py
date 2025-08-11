class FileManager:
    @staticmethod
    def save_to_file(file_name, data):
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def read_from_file(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
