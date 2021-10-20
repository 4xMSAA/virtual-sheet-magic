import keyboard
from core import Note
from core import Chord
from .base import BaseInputWrapper, MINOR_KEYS


class KeyboardWrapper(BaseInputWrapper):
    def __init__(self):
        pass

    def send_chord(self, chord: Chord) -> None:
        if self.has_minor_keys(chord):
            # TODO: investigate keyboard.write() behaviour
            # maybe it's better to just use that for shift keys?
            keyboard.press("shift")

            for note in chord:
                key = note.to_key()
                if key in MINOR_KEYS:
                    keyboard.send(MINOR_KEYS[key])

            keyboard.release("shift")

        for note in chord:
            key = note.to_key()
            if key not in MINOR_KEYS:
                keyboard.send(key)

    def send_note(self, note: Note) -> None:
        key = note.to_key()

        # see TODO for same thing here
        if key in MINOR_KEYS:
            keyboard.press("shift")
            keyboard.send(MINOR_KEYS[key])
            keyboard.release("shift")
        else:
            keyboard.send(key)
