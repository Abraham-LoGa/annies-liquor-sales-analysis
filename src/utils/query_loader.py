from pathlib import Path

class QueryLoader:

    @staticmethod
    def load(path:Path):
        with open(path, "r", encoding="utf-8") as file:
            return file.read()