from core.sheet import Sheet, ExportType
from core.chord import Chord
import unittest


class TestSheet(unittest.TestCase):
    def setUp(self):
        self.sheet = Sheet()

    def test_sheet_append(self):
        self.assertEqual(self.sheet.export(ExportType.VP_SHEET_NO_METADATA),
                         "")
        self.sheet.append(Chord(from_keys="qwe"))
        self.assertEqual(self.sheet.export(ExportType.VP_SHEET_NO_METADATA),
                         "[qwe]")

    def test_sheet_export(self):
        self.sheet.append("[qwe]")
        self.sheet.append("[qwe]")
        self.sheet.append("[qwe]")
        self.sheet.append("[qwe]")
        self.sheet.append("[qwe]")
        self.sheet.append("[qwe]")
        buffer = self.sheet.export(ExportType.VP_SHEET_NO_METADATA),
