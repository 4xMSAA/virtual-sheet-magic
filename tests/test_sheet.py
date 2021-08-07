from core.sheet import Sheet, EXPORT_TYPE
import unittest

import os
import time

class TestSheet(unittest.TestCase):

    def setUp(self):
        self.sheet = Sheet()

    def test_sheet_append(self):
        self.assertEquals(self.sheet.export(EXPORT_TYPE.VP_SHEET_NO_METADATA), "")
        self.sheet.append("[qwe]")
        self.assertEquals(self.sheet.export(EXPORT_TYPE.VP_SHEET_NO_METADATA), "[qwe]")