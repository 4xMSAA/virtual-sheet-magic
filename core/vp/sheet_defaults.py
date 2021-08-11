class SheetParserDefaults:
    def __init__(self):
        self.notes = {}

    def on_meta(self):
        raise NotImplementedError()
    def on_note(self):
        raise NotImplementedError()
    def on_chord(self):
        raise NotImplementedError()
    def on_pause(self):
        raise NotImplementedError()