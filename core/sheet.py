"""Responsible for storing notes/chords."""
from typing import Union
from enum import Enum
from core.chord import Chord
from core.note import Note
import core.vp.notations as notations


class ExportType(Enum):
    """Enum for types of files that can be exported."""
    VP_SHEET = 0
    VP_SHEET_NO_METADATA = 1
    MIDI = 2


def value_to_notation(value: int):
    return value > 1 and ">" * value or value < 1 and "<" * (1 / value) or None


def make_vp_chord(chord: Chord, transpose: int):
    buffer = ""
    if chord.value == 1/16:
        buffer = buffer + notations.BROKEN_CHORDS["begin"]["symbol"] + "".join(
            chord.as_keys(transpose)) + notations.BROKEN_CHORDS["end"]["symbol"]
    else:
        buffer = buffer + notations.CHORDS["begin"]["symbol"] + "".join(
            chord.as_keys(transpose)) + notations.CHORDS["end"]["symbol"]
    return buffer


class Sheet():
    def __init__(self,
                 tempo: float = 110,
                 beats: int = 4,
                 measure: int = 4,
                 transpose: int = 0):
        self.track = []
        self.tempo = tempo
        self.beats = beats
        self.measure = measure
        self.transpose = transpose

    def export(self, export_type: ExportType) -> str:
        if export_type == ExportType.VP_SHEET or export_type == ExportType.VP_SHEET_NO_METADATA:
            # do conversion to virtual piano sheet
            buffer = ""

            for note_or_chord in self.track:
                if isinstance(note_or_chord, Chord):
                    buffer = buffer + make_vp_chord(note_or_chord, self.transpose)
                elif isinstance(note_or_chord, Note):
                    buffer = buffer + note_or_chord.to_key(self.transpose)

            # include metadata
            if export_type == ExportType.VP_SHEET:
                raise NotImplementedError()

            return buffer

        raise ValueError("no such ExportType as {}".format(export_type))

    def append(self, note_or_chord: Union[Note, Chord]):
        self.track.append(note_or_chord)

    def replace(self, index: int, note_or_chord: Union[Note, Chord]):
        self.track[index] = note_or_chord

    def set_tempo(self, tempo: float):
        self.tempo = tempo

    def set_beats_per_measure(self, beats: int, measure: int):
        self.beats = beats
        self.measure = measure

    def set_transpose(self, transpose: int):
        self.transpose = transpose
