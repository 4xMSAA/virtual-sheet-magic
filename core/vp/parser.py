"""Parses virtual piano sheets."""


import io
from enum import Enum
from core.vp.notations import NOTE_VALUE_OFFSETS, PAUSE, CHORDS, BROKEN_CHORDS
from core import KEY_MAP, Note, Chord, Pause


NOTE_VALUE_OFFSET_SYMBOLS = {}
for notation in NOTE_VALUE_OFFSETS.values():
    for symbol in notation["symbols"]:
        NOTE_VALUE_OFFSET_SYMBOLS[symbol] = notation

INTERRUPT_SYMBOLS = {}
for notations in (BROKEN_CHORDS, CHORDS, PAUSE):
    for index, notation in notations.items():
        for symbol in notation["symbols"]:
            INTERRUPT_SYMBOLS[symbol] = {
                "name": index,
                "meaning": notation,
                "set": notations
            }


class Mode(Enum):
    NORMAL = 0
    CHORD = 1
    BROKEN_CHORD = 2


def on_chord(sheet, keys, value):
    chord = Chord(from_keys=keys, value=value)
    sheet.append(chord)


def on_broken_chord(sheet, keys, value):
    raise NotImplementedError()


def on_note(sheet, key, value):
    note = Note(from_key=key, value=value)
    sheet.append(note)


def on_pause(sheet, value):
    sheet.append(Pause(value=value))


def parse_rhythmic_value(buffer):
    divisor = 16  # initial rhythmic value. no spaces
    offset = 0

    for char in buffer:
        if char in NOTE_VALUE_OFFSET_SYMBOLS:
            keyword = NOTE_VALUE_OFFSET_SYMBOLS[char]
            offset = offset + keyword == "less" and -1 or 1
        elif char.isspace():
            divisor = divisor / 2
            if char == "\n":
                break

    return 1 / (divisor * (2 ** offset))


def parse_into(sheet, input_source, **flags):
    # TODO: refactor me!

    buffer = ""

    if isinstance(input_source, io.IOBase):
        for line in input_source:
            buffer = buffer + line
    else:
        buffer = input_source

    buffer = buffer + "\0"
    mode = Mode.NORMAL
    chord_stack = []
    word = ""
    line = 1
    col = 0

    for char in buffer:
        col = col + 1

        if char == "\n":
            col = 0
            line = line + 1

            if flags["newline_pauses"]:
                on_pause(sheet, PAUSE["eight"]["scale"])

        if char in INTERRUPT_SYMBOLS or char in KEY_MAP or char == "\0":
            key = word.translate(word.maketrans("", "", "".join(INTERRUPT_SYMBOLS.keys()))).strip()
            rhythmic_value = parse_rhythmic_value(word)

            if mode == Mode.NORMAL and len(key) > 0:
                # hacky behaviour that i do not like
                # because this should be handled by the "end" of a chord
                # but if we do it there, we can't get the rhythmic value
                if len(key) > 1:
                    on_chord(sheet, key, rhythmic_value)
                else:
                    on_note(sheet, key, rhythmic_value)
                word = ""

            if char in INTERRUPT_SYMBOLS:
                entry = INTERRUPT_SYMBOLS[char]

                if entry["set"] is PAUSE:
                    on_pause(sheet, entry["meaning"]["scale"] + rhythmic_value)
                    word = ""

                if entry["set"] is CHORDS:
                    if entry["name"] == "begin":
                        # hacky behaviour that i do not like [2]
                        if word != "" and len(key) > 1:
                            on_chord(sheet, key, rhythmic_value)
                            word = ""

                        chord_stack.append(mode)
                        mode = Mode.CHORD
                    elif entry["name"] == "end" and Mode.CHORD:
                        previous_mode = chord_stack.pop()
                        mode = previous_mode

                    else:
                        raise SyntaxError("CHORD mode did not end properly (@{line},{col})")

            word = word + char
        else:
            word = word + char

    return sheet
