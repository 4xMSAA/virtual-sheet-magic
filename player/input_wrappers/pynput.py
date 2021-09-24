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


class PynputWrapper(BaseInputWrapper):
    def __init__(self):
        self.keyboard = keyboard.Controller()

    def send_chord(self, chord: Chord):
        for note in chord:
            self.send_note(note)

    def send_note(self, note: Note):
        key = note.to_key()
        if key in MINOR_KEYS:
            self.keyboard.press(keyboard.Key.shift)
            self.keyboard.type(MINOR_KEYS[key])
            self.keyboard.release(keyboard.Key.shift)
        else:
            self.keyboard.type(key)
