import unittest
from core.vp.parser import Parser
from core.sheet import Sheet

class TestParsing(unittest.TestCase):

    def setUp(self):
        self.vp_sheet = ""
        for line in open("tests/resources/test.vpsheet"):
            self.vp_sheet = self.vp_sheet + line
    
    def test_parser(self):
        parser = Parser()
        parser.parse(self.vp_sheet, 
            callback_meta=Sheet.on_meta, 
            callback_note=Sheet.on_note,
            callback_chord=Sheet.on_chord,
            callback_pause=Sheet.on_pause
        )
        self.assertEquals(parser.buffer, self.vp_sheet.replace(r"(\n|\r)", " "))