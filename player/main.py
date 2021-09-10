from core.sheet import Sheet


class Player:
    def __init__(self, sheet: Sheet):
        self.sheet = sheet
        self.tempo = sheet.tempo
        self.cursor = 0

    def step(self):
        raise NotImplementedError()

    def set_cursor(self, index: int):
        if index < 0 or index > len(self.sheet.track):
            raise ValueError("cursor cannot be lower than 0 or above sheet's note count")

        self.cursor = index
