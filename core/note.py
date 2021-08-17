# https://www.deimos.ca/notefreqs/
# https://en.wikipedia.org/wiki/Piano_key_frequencies

key_map = list("1!2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCvVbBnm")
A4_key_index = key_map.index("p") 
A4_midi_index = 69
midi_index_boundary = (0, 127)
midi_to_note_index_boundary = (12, 108)
transpose_range = (-12, 12)

def key_to_midi_index(key):
   return A4_midi_index + (key_map.index(key) - A4_key_index) - 12 

def midi_index_to_key(index, transpose):
    return key_map[ 
        ((index - midi_to_note_index_boundary[0]) 
        + (transpose_range[0] + transpose))
        % len(key_map)
    ]

class Note():
    
    def __init__(self, index=A4_midi_index, from_key=None, transpose=0): 
        if from_key is not None:
            self.from_key(from_key)
        else:
            self.index = index

        self.chromatic_transpose(transpose)
        

    def chromatic_transpose(self, amount):
        self.index = self.index + amount

    def from_key(self, key):
        self.index = key_to_midi_index(key)
        
    def to_key(self, global_transpose=0):
        return midi_index_to_key(self.index, global_transpose)