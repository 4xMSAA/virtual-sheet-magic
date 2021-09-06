"""
Provides an abstraction from notes found in MIDI, real music sheets and virtual piano notes.

Resources to consider when changing the way notes are treated
https://www.deimos.ca/notefreqs/
https://en.wikipedia.org/wiki/Piano_key_frequencies
https://en.wikipedia.org/wiki/List_of_musical_symbols
https://en.wikipedia.org/wiki/Note_value
"""

from typing import Union
from enum import Enum
KEY_MAP = list("1!2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCvVbBnm")
A4_KEY_INDEX = KEY_MAP.index("p")
A4_MIDI_INDEX = 69
MIDI_INDEX_BOUNDARY = (0, 127)
MIDI_TO_NOTE_INDEX_BOUNDARY = (12, 108)
TRANSPOSE_RANGE = (-12, 12)


class NoteValue(Enum):
    LARGE = 8
    LONG = 4
    DOUBLE = 2
    WHOLE = 1
    HALF = 1/2
    QUARTER = 1/4
    EIGTH = 1/8
    SIXTEENTH = 1/16
    THIRTYSECOND = 1/32
    SIXTYFOURTH = 1/64


def key_to_midi_index(key):
    return A4_MIDI_INDEX + (KEY_MAP.index(key) - A4_KEY_INDEX) - 12


def midi_index_to_key(index, transpose):
    return KEY_MAP[((index - MIDI_TO_NOTE_INDEX_BOUNDARY[0]) +
                    (TRANSPOSE_RANGE[0] + transpose)) % len(KEY_MAP)]


class Note():
    def __init__(self,
                 index: int = A4_MIDI_INDEX,
                 from_key: str = None,
                 value: Union[float, NoteValue] = NoteValue.QUARTER,
                 transpose: int = 0):
        """Creates a Note object from either virtual piano keys or a MIDI note index

        Args:
            index (int, optional): The MIDI note index to use. Defaults to A4_MIDI_INDEX.
            from_key (str, optional): Virtual piano key that is converted to MIDI index.
                                      Defaults to None.
            value (Union[float, NoteValue], optional): Note value that indicates the relative pause
                                                       between notes in a multiplying manner.
                                                       Defaults to QUARTER.
            transpose (int, optional): How much to transpose the note up/down. Defaults to 0.
        """
        if from_key is not None:
            self.from_key(from_key)
        else:
            self.index = index

        self.value = value
        self.chromatic_transpose(transpose)

    def chromatic_transpose(self, amount: int):
        self.index = self.index + amount

    def from_key(self, key: str):
        self.index = key_to_midi_index(key)

    def to_key(self, global_transpose: int = 0):
        return midi_index_to_key(self.index, global_transpose)
