from core.note import Note


class Chord(list):
    def __init__(self,
                 notes: Note = None,
                 from_keys: str = None,
                 transpose: int = 0,
                 value: float = 1/4,
                 rate: float = 0):
        self.value = value
        self.rate = rate

        if notes is not None:
            for note in notes:
                note.set_value(self.rate)
                self.append(note)
        if from_keys is not None:
            for key in from_keys:
                self.append(Note(from_key=key, transpose=transpose, value=rate))

    def chromatic_transpose(self, amount: int):
        for note in self:
            note.chromatic_transpose(self, amount)

    def as_keys(self, global_transpose: int = 0):
        keys_list = []
        for _, note in enumerate(self):
            keys_list.append(note.to_key(global_transpose))

        return keys_list
