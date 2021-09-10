from core.sheet import Sheet
from core.note import Note
from core.chord import Chord
from player.input_wrappers.base import BaseInputWrapper


class Player:
    def __init__(self, sheet: Sheet, input_wrapper: BaseInputWrapper = None):
        self.input = input_wrapper
        self.sheet = sheet
        self.tempo = sheet.tempo
        self.cursor = -1

    def step(self):
        self.cursor = self.cursor + 1
        entry = self.sheet.track[self.cursor]
        if isinstance(entry, Chord):
            self.input.send_chord(entry)
        elif isinstance(entry, Note):
            self.input.send_note(entry)
        else:
            print(f"unknown instance in track (@{self.cursor}")

        return entry

    def stop(self):
        self.cursor = -1

    def set_cursor(self, index: int):
        if index < -1 or index > len(self.sheet.track):
            raise ValueError("cursor cannot be lower than -1 or above sheet's note count")

        self.cursor = index

    def set_input_wrapper(self, input_wrapper: BaseInputWrapper):
        if isinstance(input_wrapper, BaseInputWrapper):
            self.input = input_wrapper
        else:
            raise ValueError("input wrapper doesn't extend from BaseInputWrapper")
