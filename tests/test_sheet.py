from core.sheet import Sheet
from core.chord import Chord
import unittest


class TestSheet(unittest.TestCase):
    def setUp(self):
        self.sheet = Sheet()

    def test_sheet_append(self):
        self.assertEqual(len(self.sheet.track), 0)
        self.sheet.append(Chord(from_keys="qwe"))
        self.assertEqual(len(self.sheet.track), 1)
