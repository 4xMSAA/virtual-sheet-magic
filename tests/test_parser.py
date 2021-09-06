"""Tests whether parsing works as expected"""
import unittest
from core.vp.parser import parse

location = "tests/resources/test.vpsheet"

sheet_simple = "a b c d e f"


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.vp_sheet = ""
        with open(location) as file:
            for line in file:
                self.vp_sheet = self.vp_sheet + line

    def test_parser_from_str(self):
        sheet = parse(self.vp_sheet)

        self.assertCountEqual(sheet.track, 10)

    def test_parser_from_stdio(self):
        with open(location) as file:
            sheet = parse(file)

            self.assertCountEqual(sheet.track, 10)

    def test_parser_simple(self):
        sheet = parse(sheet_simple)

        self.assertCountEqual(sheet.track, 6)
