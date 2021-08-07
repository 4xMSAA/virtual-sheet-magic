from enum import Enum

class EXPORT_TYPE(Enum):
    VP_SHEET = 0
    VP_SHEET_NO_METADATA = 1
    MIDI = 2

class Sheet(SheetParserDefaults):
    def __init__(self, tempo=110, beats=4, measure=4):
        self.tempo = 0
        self.beats = 0
        self.measure = 0

    def export(self, export_type):

        if export_type == EXPORT_TYPE.VP_SHEET or export_type == EXPORT_TYPE.VP_SHEET_NO_METADATA:
            # do conversion to virtual piano sheet

            # include metadata
            if export_type == EXPORT_TYPE.VP_SHEET:
                pass
    
    def append(self, notes, index=None):
        pass

class SheetParserDefaults:

    def on_note():
        pass