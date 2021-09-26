from pynput import keyboard
from core import Note
from core import Chord
from .base import BaseInputWrapper

MINOR_KEYS = {
    "!": "1",
    "@": "2",
    "$": "4",
    "%": "5",
    "^": "6",
    "*": "8",
    "(": "9",
    "Q": "q",
    "W": "w",
    "E": "e",
    "T": "t",
    "Y": "y",
    "I": "i",
    "O": "o",
    "P": "p",
    "S": "s",
    "D": "d",
    "G": "g",
    "H": "h",
    "J": "j",
    "L": "l",
    "Z": "z",
    "C": "c",
    "V": "v",
    "B": "b",
}


def has_minor_keys(chord: Chord) -> bool:
    for note in chord:
        if note.to_key() in MINOR_KEYS:
            return True


class PynputWrapper(BaseInputWrapper):
    def __init__(self):
        self.keyboard = keyboard.Controller()

    def send_chord(self, chord: Chord):
        if has_minor_keys(chord):
            self.keyboard.press(keyboard.Key.shift)
            for note in chord:
                key = note.to_key()
                if key in MINOR_KEYS:
                    self.keyboard.type(MINOR_KEYS[key])
            self.keyboard.release(keyboard.Key.shift)

        for note in chord:
            key = note.to_key()
            if not key in MINOR_KEYS:
                self.keyboard.type(key)


    def send_note(self, note: Note):
        key = note.to_key()
        if key in MINOR_KEYS:
            self.keyboard.press(keyboard.Key.shift)
            self.keyboard.type(MINOR_KEYS[key])
            self.keyboard.release(keyboard.Key.shift)
        else:
            self.keyboard.type(key)
