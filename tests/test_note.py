import unittest
from core.note import Note

key_map = list("1!2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCvVbBnm")
midi_index_start = 12 # C1
class TestNote(unittest.TestCase):

    def test_key_to_note(self):
        for key in key_map:
            note = Note(from_key=key)
            self.assertEqual(note.index, key_map.index(key) + midi_index_start)

    def test_note_to_key(self):
        for key in key_map:
            note = Note(from_key=key)
            self.assertEqual(key, note.to_key(0))