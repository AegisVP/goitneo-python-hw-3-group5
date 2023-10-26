import json
from pathlib import Path


class FileWriter:
    DO_SAVE = True

    def __init__(self, filename="phonebook.json"):
        self.file = Path(__file__).parent / filename

    def save(self, data):
        if FileWriter.DO_SAVE:
            self.file.write_text(json.dumps(data))

    def load(self):
        if not self.file.exists():
            self.save('')

        return json.loads(self.file.read_text())
