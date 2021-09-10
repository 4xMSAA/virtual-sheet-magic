class BaseInputWrapper():
    def send_chord(self, chord):
        raise NotImplementedError()

    def send_note(self, note):
        raise NotImplementedError()
