from threading import Thread
from core import Sheet, Note, Chord, Pause
from editor import UndoHistory


class Editor:
    def __init__(self, sheet: Sheet):
        self.sheet = sheet
        self.dirty = False;
        self.cursor = [0, -1]
        self.mode = 0
        self._file_path = None

    def insert(self, note: str):
        self.dirty = True
        pass

    def replace(self, note: str):
        self.dirty = True
        pass

    def delete(self):
        self.dirty = True
        pass

    def redo(self):
        pass

    def undo(self):
        pass
