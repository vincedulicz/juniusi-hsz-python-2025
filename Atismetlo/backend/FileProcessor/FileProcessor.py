class FileProcessor:
    @staticmethod
    def read_file(filename: str) -> List:
        data = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        data.append(int(line))
                    except ValueError:
                        data.append(line)
            return data
        except FileNotFoundError:
            Logger.error(f"Fájl nem található: {filename}")
            return []
        except Exception as e:
            Logger.error(f"Hiba a fájl olvasása közben: {e}")
            return []


    @staticmethod
    def write_file(filename: str, data: List):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                if isinstance(data[0], int):
                    file.write('\n'.join(map(str, data)))
                else:
                    file.write('\n'.join(data))
        except Exception as e:
            Logger.error(e)