from core.note import Note


class Chord(list[Note]):
    def __init__(self,
                 notes: Note = None,
                 from_keys: str = None,
                 transpose: int = 0):
        if notes is not None:
            for note in notes:
                self.append(note)
        if from_keys is not None:
            for key in from_keys:
                self.append(Note(from_key=key, transpose=transpose))

    def chromatic_transpose(self, amount: int):
        for note in self:
            note.chromatic_transpose(self, amount)

    def as_keys(self, global_transpose: int = 0):
        keys_list = []
        for _, note in enumerate(self):
            keys_list.append(note.to_key(global_transpose))

        return keys_list
