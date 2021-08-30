"""Parses virtual piano sheets"""
import io
from core.vp.notations import PAUSE, CHORDS, BROKEN_CHORDS
from core.sheet import Sheet
from core.note import Note
from core.chord import Chord

symbol_to_notation = {}
for notations in (PAUSE, CHORDS):
    for key, notation in notations.items():
        if "symbols" in notation:
            for symbols in notation["symbols"]:
                symbol_to_notation[symbols] = key
        else:
            symbol_to_notation[notation["symbol"]] = key


def on_chord(keys, value, rate):
    raise NotImplementedError()


def on_note(key, value):


def parse_rhythmic_value(buffer, )

def parse(input_source):
    buffer = ""
    sheet = Sheet()

    if isinstance(input_source, io.IOBase):
        for line in input_source:
            buffer = buffer + line
    else:
        buffer = input_source

    # nobody would nest broken chords into chords... right?
    chord_buffer = ""
    broken_chord_buffer = ""
    for char in buffer:
        if char in symbol_to_notation:
            if char == BROKEN_CHORDS["begin"]["symbol"]:
                broken_chord_buffer = char
            elif char == BROKEN_CHORDS["end"]["symbol"]:
                on_chord(sheet,
                         broken_chord_buffer.strip(BROKEN_CHORDS["begin"]["symbol"]), 1/16)
                broken_chord_buffer = ""

            elif char == CHORDS["begin"]["symbol"]:
                chord_buffer = char
            elif char == CHORDS["end"]["symbol"]:
                on_chord(sheet,
                         chord_buffer.strip(CHORDS["begin"]["symbol"]), 1/4)
                chord_buffer = ""

        elif len(chord_buffer) == 0:
            on_note(char)
        else:
            chord_buffer = chord_buffer + char

    return sheet, buffer
