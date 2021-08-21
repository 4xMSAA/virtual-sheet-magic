import unittest
from core.note import Note
from core.chord import Chord

KEY_MAP = list("1!2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCvVbBnm")
MIDI_INDEX_START = 12  # C1
TRANSPOSE_RANGE = range(-12, 12)


class TestNote(unittest.TestCase):
    def test_key_to_note(self):
        for transpose in TRANSPOSE_RANGE:
            for key in KEY_MAP:
                note = Note(from_key=key, transpose=transpose)
                self.assertEqual(
                    note.index,
                    KEY_MAP.index(key) + MIDI_INDEX_START + (12 + transpose))

    def test_note_to_key(self):
        for transpose in TRANSPOSE_RANGE:
            for key in KEY_MAP:
                note = Note(from_key=key, transpose=transpose)
                self.assertEqual(key, note.to_key(-transpose))

    def test_note_to_key_global_transposed(self):
        key_map_transposing = list("oOpPa")
        expected_key_map = list("pPasS")
        for key in key_map_transposing:
            note = Note(from_key=key)
            self.assertEqual(expected_key_map[key_map_transposing.index(key)],
                             note.to_key(2))

    def test_note_to_key_note_transposed(self):
        key_map_transposing = list("oOpPa")
        expected_key_map = list("pPasS")
        for key in key_map_transposing:
            note = Note(from_key=key, transpose=2)
            self.assertEqual(expected_key_map[key_map_transposing.index(key)],
                             note.to_key(0))


class TestChord(unittest.TestCase):
    def test_chord_list(self):
        input_notes = list("tewi")

        chord = Chord()
        for key in input_notes:
            chord.append(Note(from_key=key))

        self.assertEqual(input_notes, chord.as_keys())
