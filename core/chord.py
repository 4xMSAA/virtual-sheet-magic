from core.note import Note

class Chord(list[Note]):

    def chromatic_transpose(self, amount):
        for note in self:
            note.chromatic_transpose(self, amount)
    
    def as_keys(self, global_transpose=0):
        keys_list = []

        for note in self:
            keys_list.append(note.to_key(global_transpose))
        
        return keys_list
