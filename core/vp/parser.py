"""Parses virtual piano sheets."""


import io
from enum import Enum
from core.vp.notations import NOTE_VALUE_OFFSETS, PAUSE, CHORDS, BROKEN_CHORDS
from core.sheet import Sheet
from core.note import Note
from core.chord import Chord

PAUSE_SYMBOLS = {}
for notation in PAUSE:
    for symbol in notation["symbols"]:
        PAUSE_SYMBOLS[symbol] = notation["scale"]

NOTE_VALUE_OFFSET_SYMBOLS = {}
for notation in NOTE_VALUE_OFFSETS:
    for symbol in notation["symbols"]:
        NOTE_VALUE_OFFSET_SYMBOLS[symbol] = notation

ACTIVE_SYMBOLS = {}
for notations in (BROKEN_CHORDS, CHORDS):
    for key, notation in notations.items():
        if "symbols" in notation:
            for symbol in notation["symbols"]:
                ACTIVE_SYMBOLS[symbol] = key
        else:
            ACTIVE_SYMBOLS[notation["symbol"]] = key


class Mode(Enum):
    NORMAL = 0
    CHORD = 1
    BROKEN_CHORD = 2


def on_chord(sheet, keys, value):
    raise NotImplementedError()


def on_broken_chord(sheet, keys, value):
    raise NotImplementedError()


def on_note(sheet, key, value):
    raise NotImplementedError()


def parse_rhythmic_value(buffer):
    divisor = 8  # initial rhythmic value. no spaces
    offset = 0

    for char in buffer:
        if char in NOTE_VALUE_OFFSET_SYMBOLS:
            keyword = NOTE_VALUE_OFFSET_SYMBOLS[char]
            offset = offset + keyword == "less" and -1 or 1
        elif char.isspace():
            divisor = divisor / 2

    return 1 / (divisor * (2 ** offset))


def parse_into(sheet, input_source):
    buffer = ""

    if isinstance(input_source, io.IOBase):
        for line in input_source:
            buffer = buffer + line
    else:
        buffer = input_source

    mode = Mode.NORMAL
    chord_stack = []
    word = ""

    for char in buffer:
        if char in ACTIVE_SYMBOLS or char.isalnum():
            key = word.strip(PAUSE_SYMBOLS.keys()).strip().strip(ACTIVE_SYMBOLS.keys())
            if mode == Mode.NORMAL and len(word) > 0:
                on_note(sheet, key, parse_rhythmic_value(word))
        else:
            word = word + char

    return sheet
