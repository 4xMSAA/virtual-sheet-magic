from pynput import keyboard
from core import Note
from core import Chord
from .base import BaseInputWrapper, MINOR_KEYS


class PynputWrapper(BaseInputWrapper):
    def __init__(self):
        self.keyboard = keyboard.Controller()

    def send_chord(self, chord: Chord):
        if self.has_minor_keys(chord):
            self.keyboard.press(keyboard.Key.shift)

            for note in chord:
                key = note.to_key()
                if key in MINOR_KEYS:
                    self.keyboard.type(MINOR_KEYS[key])

            self.keyboard.release(keyboard.Key.shift)

        for note in chord:
            key = note.to_key()
            if key not in MINOR_KEYS:
                self.keyboard.type(key)

    def send_note(self, note: Note):
        key = note.to_key()
        if key in MINOR_KEYS:
            self.keyboard.press(keyboard.Key.shift)
            self.keyboard.type(MINOR_KEYS[key])
            self.keyboard.release(keyboard.Key.shift)
        else:
            self.keyboard.type(key)
