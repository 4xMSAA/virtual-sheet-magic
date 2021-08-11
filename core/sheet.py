from enum import Enum
from .vp.sheet_defaults import SheetParserDefaults

class EXPORT_TYPE(Enum):
    VP_SHEET = 0
    VP_SHEET_NO_METADATA = 1
    MIDI = 2

class Sheet(SheetParserDefaults):
    def __init__(self, tempo=110, beats=4, measure=4):
        SheetParserDefaults.__init__(self)
        self.tempo = tempo
        self.beats = beats
        self.measure = measure

    def export(self, export_type):

        if export_type == EXPORT_TYPE.VP_SHEET or export_type == EXPORT_TYPE.VP_SHEET_NO_METADATA:
            # do conversion to virtual piano sheet
            buffer = ""

            # include metadata
            if export_type == EXPORT_TYPE.VP_SHEET:
                raise NotImplementedError()
            return buffer
    
    def append(self, notes, index=None):
        raise NotImplementedError()

    def on_meta(self):
        raise NotImplementedError()

    def on_note(self):
        raise NotImplementedError()
    
    def on_chord(self):
        raise NotImplementedError()
    
    def on_pause(self):
        raise NotImplementedError()
