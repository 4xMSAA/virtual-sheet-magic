from sys import stdin
from core.vp.parser import parse_into
from core import Sheet


def parse_stdin(**flags) -> Sheet:
    sheet = Sheet()
    parse_into(sheet, stdin, **flags)

    return sheet
