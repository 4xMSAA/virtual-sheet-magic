"""Responsible for storing notes/chords."""


from typing import Union
from core.chord import Chord
from core.note import Note


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
