"""Tests whether parsing works as expected"""
import unittest
from core.vp.parser import parse

location = "tests/resources/test.vpsheet"


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.vp_sheet = ""
        with open(location) as file:
            for line in file:
                self.vp_sheet = self.vp_sheet + line

    def test_parser_from_str(self):
        parsed_sheet, buffer = parse(self.vp_sheet)
        self.assertEqual(buffer, self.vp_sheet.replace(r"(\n|\r)", " "))

    def test_parser_from_stdio(self):
        with open(location) as file:
            parsed_sheet, buffer = parse(file)
            self.assertEqual(buffer, self.vp_sheet.replace(r"(\n|\r)", " "))
