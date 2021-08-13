import unittest
from core.note import Note

key_map = list("1!2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCvVbBnm")
midi_index_start = 12 # C1
transpose_range = range(-12, 12)
class TestNote(unittest.TestCase):

    def test_key_to_note(self):
        for transpose in transpose_range:
            for key in key_map:
                note = Note(from_key=key, transpose=transpose)
                self.assertEqual(note.index, key_map.index(key) + midi_index_start + (12 + transpose))

    def test_note_to_key(self):
        for transpose in transpose_range:
            for key in key_map:
                note = Note(from_key=key, transpose=transpose)
                self.assertEqual(key, note.to_key(-transpose))
                
    
    def test_note_to_key_global_transposed(self):
        key_map_transposing = list("oOpPa")
        expected_key_map = list("pPasS")
        for key in key_map_transposing:
            note = Note(from_key=key)
            self.assertEqual(
                expected_key_map[key_map_transposing.index(key)], 
                note.to_key(2)
            )

    def test_note_to_key_note_transposed(self):
        key_map_transposing = list("oOpPa")
        expected_key_map = list("pPasS")
        for key in key_map_transposing:
            note = Note(from_key=key, transpose=2)
            self.assertEqual(
                expected_key_map[key_map_transposing.index(key)], 
                note.to_key(0)
            )