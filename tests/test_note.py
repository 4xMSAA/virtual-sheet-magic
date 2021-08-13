import unittest
from core.note import Note

class TestNote(unittest.TestCase):

    def test_note_to_key(self):
        key_map = list("1!2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCvVbBnm")
        for key in key_map:
            note = Note(from_key=key)
            self.assertEqual(key, note.to_key(0))