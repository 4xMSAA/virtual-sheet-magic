import unittest
from core.sheet import Sheet
from core.note import Note
from core.chord import Chord
from core.vp.parser import parse_into
from player.input_wrappers.base import BaseInputWrapper
from player.main import Player


test_sheet = "a b c d e f [abc][def] abcdef"


class MockInputWrapper(BaseInputWrapper):
    """Mocks an input wrapper that sends virtual piano keys to an input sending library"""
    def __init__(self):
        self.buffer = ""

    def send_note(self, note: Note):
        self.buffer = self.buffer + note.to_key()

    def send_chord(self, chord: Chord):
        for note in chord:
            self.buffer = self.buffer + note.to_key()

    def clear(self):
        self.buffer = ""

    def __eq__(self, other):
        return self.buffer == other


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.input_mock = MockInputWrapper()
        self.sheet = Sheet()
        parse_into(self.sheet, test_sheet)

        self.player = Player(self.sheet)
        self.player.set_input_wrapper(self.input_mock)

    def test_step(self):
        for _ in range(len(self.sheet.track)):
            self.player.step()

        self.assertEqual(self.input_mock, "abcdefabcdefabcdef")
