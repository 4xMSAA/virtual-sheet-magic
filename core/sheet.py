"""Responsible for storing notes/chords. Implement `on_*` callbacks by extending this class."""
from typing import Union
from enum import Enum
from core.chord import Chord
from core.note import Note


class ExportType(Enum):
    """Enum for types of files that can be exported"""
    VP_SHEET = 0
    VP_SHEET_NO_METADATA = 1
    MIDI = 2


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
                    buffer = buffer + "[" + "".join(
                        note_or_chord.as_keys(self.transpose)) + "]"
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

    def on_meta(self):
        raise NotImplementedError()

    def on_note(self):
        raise NotImplementedError()

    def on_chord(self):
        raise NotImplementedError()

    def on_pause(self):
        raise NotImplementedError()
