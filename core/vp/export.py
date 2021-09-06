import core.vp.notations as notations
from core.note import Note, NoteValue
from core.chord import Chord


def value_to_notation(value: float):
    return value > 1 and ">" * value or value < 1 and "<" * (1 / value) or None


def make_vp_chord(chord: Chord, transpose: int):
    buffer = ""
    if chord.value == 1/16:
        buffer = buffer + notations.BROKEN_CHORDS["begin"]["symbols"][0] + "".join(
            chord.as_keys(transpose)) + notations.BROKEN_CHORDS["end"]["symbols"][0]
    else:
        buffer = buffer + notations.CHORDS["begin"]["symbols"][0] + "".join(
            chord.as_keys(transpose)) + notations.CHORDS["end"]["symbols"][0]
    return buffer


def export(self, metadata: bool = False) -> str:
    # do conversion to virtual piano sheet
    buffer = ""

    for note_or_chord in self.track:
        if isinstance(note_or_chord, Chord):
            buffer = buffer + make_vp_chord(note_or_chord, self.transpose)
        elif isinstance(note_or_chord, Note):
            buffer = buffer + note_or_chord.to_key(self.transpose)

    # include metadata
    if metadata:
        raise NotImplementedError()

    return buffer
