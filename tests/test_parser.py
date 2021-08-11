import unittest
from core.vp.parser import Parser
from core.vp.sheet_defaults import SheetParserDefaults

class TestParsing(unittest.TestCase):

    def setUp(self):
        self.vp_sheet = open("tests/resources/test.vpsheet").read()
    
    def test_parser(self):
        parser = Parser()
        parser.parse(self.vp_sheet, 
            callback_meta=SheetParserDefaults.on_meta, 
            callback_note=SheetParserDefaults.on_note,
            callback_chord=SheetParserDefaults.on_chord,
            callback_pause=SheetParserDefaults.on_pause
        )
        self.assertEquals(parser.buffer, self.vp_sheet.replace(r"(\n|\r)", " "))