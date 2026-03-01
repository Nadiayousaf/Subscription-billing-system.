import json

class Storage:
    FILE = "data.json"

    @staticmethod
    def save(data):
        with open(Storage.FILE, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load():
        try:
            with open(Storage.FILE, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}