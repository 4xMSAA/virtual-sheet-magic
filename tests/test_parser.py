"""Tests whether parsing works as expected"""
import unittest
from core.vp.parser import parse


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.vp_sheet = ""
        with open("tests/resources/test.vpsheet") as file:
            for line in file:
                self.vp_sheet = self.vp_sheet + line

    def test_parser(self):
        parser = parse(self.vp_sheet)
        self.assertEqual(parser, self.vp_sheet.replace(r"(\n|\r)", " "))
