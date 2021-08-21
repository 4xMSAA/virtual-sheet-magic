# pylint: disable=too-few-public-methods
"""
Parses virtual piano sheets by callbacks provided from an abstracted music sheet class
"""
import io
from core.vp.notations import PAUSE, CHORDS

symbol_to_notation = {}
for notations in (PAUSE, CHORDS):
    for key, notation in notations.items():
        if "symbols" in notation:
            for symbols in notation["symbols"]:
                symbol_to_notation[symbols] = key
        else:
            symbol_to_notation[notation["symbol"]] = key


class Parser:
    def __init__(self, callback_meta, callback_note, callback_chord,
                 callback_pause):
        self.buffer = ""
        self.callback_meta = callback_meta
        self.callback_note = callback_note
        self.callback_chord = callback_chord
        self.callback_pause = callback_pause

    def parse(self, input_source):

        if isinstance(input_source, io.IOBase):
            for line in input_source:
                self.buffer = self.buffer + line
        else:
            self.buffer = input_source

        chord_buffer = ""
        for char in self.buffer:
            if char in symbol_to_notation:
                if char == CHORDS["begin"]["symbol"]:
                    chord_buffer = char
                if char == CHORDS["end"]["symbol"]:
                    self.callback_chord(
                        chord_buffer.strip(CHORDS["begin"]["symbol"]))
                    chord_buffer = ""

            elif len(chord_buffer) == 0:
                self.callback_note(char)
            else:
                chord_buffer = chord_buffer + char
