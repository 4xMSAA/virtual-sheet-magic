from core import Chord

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


class BaseInputWrapper():
    def has_minor_keys(self, chord: Chord) -> bool:
        for note in chord:
            if note.to_key() in MINOR_KEYS:
                return True

    def send_chord(self, chord):
        raise NotImplementedError()

    def send_note(self, note):
        raise NotImplementedError()
