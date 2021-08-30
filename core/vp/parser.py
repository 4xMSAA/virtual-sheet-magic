"""Parses virtual piano sheets by callbacks provided from an abstracted music sheet class"""
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


def on_chord(keys):
    raise NotImplementedError()


def on_note(key):
    raise NotImplementedError()


def parse(input_source):
    buffer = ""

    if isinstance(input_source, io.IOBase):
        for line in input_source:
            buffer = buffer + line
    else:
        buffer = input_source

    chord_buffer = ""
    for char in buffer:
        if char in symbol_to_notation:
            if char == CHORDS["begin"]["symbol"]:
                chord_buffer = char
            if char == CHORDS["end"]["symbol"]:
                on_chord(
                    chord_buffer.strip(CHORDS["begin"]["symbol"]))
                chord_buffer = ""

        elif len(chord_buffer) == 0:
            on_note(char)
        else:
            chord_buffer = chord_buffer + char
