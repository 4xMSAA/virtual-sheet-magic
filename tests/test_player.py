import unittest
from core.sheet import Sheet
from core.vp.parser import parse_into
from player.main import Player

location = "tests/resources/test.vpsheet"


class MockInputWrapper():
    def send_key(self, key):
        raise NotImplementedError()

    def send_chord(self, chord):
        raise NotImplementedError()


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.sheet = Sheet()
        with open(location) as file:
            parse_into(self.sheet, file)

        self.player = Player(self.sheet)
        self.player.set_input_wrapper(MockInputWrapper())

    def test_step(self):
        # TODO: mock input wrapper for testing purposes
        self.player.step()
