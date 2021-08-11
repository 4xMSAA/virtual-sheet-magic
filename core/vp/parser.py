# parse virtual piano sheet files
from .notations import pause, chords
from enum import Enum
import io

symbol_to_notation = {}
for key, notation in (pause, chords):
    if "symbols" in notation:
        for symbols in notation[symbols]:
            symbol_to_notation[symbols] = key
    else:
        symbol_to_notation[notation["symbol"]] = key

class Parser:
    def __init__(self, input_source=None, callback_meta=None, callback_note=None, callback_chord=None, callback_pause=None):
        self.buffer = ""
        if input_source and callback_meta and callback_note and callback_chord and callback_pause:
            self.parse(input_source, callback_meta, callback_note, callback_chord, callback_pause) 

    def parse(self, input_source, callback_meta, callback_note, callback_chord, callback_pause):
        if isinstance(input_source, io.IOBase):
            for line in input_source:
                self.buffer = self.buffer + line
        else:
            self.buffer = input_source
        
        for char in self.buffer:
            if char in symbol_to_notation:
                if char == chords["begin"]:
                    pass
                pass
            else:
                pass