import pickle
from pathlib import Path


class FileWriter:
    DO_SAVE = True

    def __init__(self, filename="phonebook.json"):
        self.file = Path(__file__).parent / filename
    # end def

    def save(self, data):
        if FileWriter.DO_SAVE:
            self.file.write_bytes(pickle.dumps(data))
        # end if
    # end def

    def load(self):
        if not self.file.exists():
            return
        # end if

        return pickle.loads(self.file.read_bytes())
    # end def
