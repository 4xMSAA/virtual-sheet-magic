import unittest
from core.vp.parser import Parser

class TestParsing(unittest.TestCase):

    def setUp(self):
        self.vp_sheet = open("tests/resources/test.vpsheet").read()
    
    def test_parser(self):
        parser = Parser()
        parser.parse(self.vp_sheet)
        self.assertEquals(parser.buffer, self.vp_sheet)