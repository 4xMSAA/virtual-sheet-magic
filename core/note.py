"""
Provides an abstraction from notes found in MIDI, real music sheets and virtual piano notes.

Resources to consider when changing the way notes are treated
https://www.deimos.ca/notefreqs/
https://en.wikipedia.org/wiki/Piano_key_frequencies
https://en.wikipedia.org/wiki/List_of_musical_symbols
https://en.wikipedia.org/wiki/Note_value
"""

KEY_MAP = list("1!2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCvVbBnm")
A4_KEY_INDEX = KEY_MAP.index("p")
A4_MIDI_INDEX = 69
MIDI_INDEX_BOUNDARY = (0, 127)
MIDI_TO_NOTE_INDEX_BOUNDARY = (12, 108)
TRANSPOSE_RANGE = (-12, 12)


def key_to_midi_index(key):
    return A4_MIDI_INDEX + (KEY_MAP.index(key) - A4_KEY_INDEX) - 12


def midi_index_to_key(index, transpose):
    return KEY_MAP[((index - MIDI_TO_NOTE_INDEX_BOUNDARY[0]) +
                    (TRANSPOSE_RANGE[0] + transpose)) % len(KEY_MAP)]


class Note():
    def __init__(self, index: int = A4_MIDI_INDEX, from_key: str = None, value: int = 1, transpose: int = 0):
        """Creates a Note object from either virtual piano keys or a MIDI note index

        Args:
            index (int, optional): The MIDI note index to use. Defaults to A4_MIDI_INDEX.
            from_key (str, optional): Virtual piano key that is converted to MIDI index. Defaults to None.
            value (int, optional): Note value that indicates the relative pause between notes in a multiplying manner. Defaults to 1.
            transpose (int, optional): How much to transpose the note  up/down. Defaults to 0.
        """
        if from_key is not None:
            self.from_key(from_key)
        else:
            self.index = index
        
        self.value = value
        self.chromatic_transpose(transpose)

    def chromatic_transpose(self, amount):
        self.index = self.index + amount

    def from_key(self, key):
        self.index = key_to_midi_index(key)

    def to_key(self, global_transpose: int = 0):
        return midi_index_to_key(self.index, global_transpose)