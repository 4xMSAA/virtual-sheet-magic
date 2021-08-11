import keyboard
from base import BaseInputWrapper

class KeyboardWrapper(BaseInputWrapper):

    def __init__(self):
        BaseInputWrapper.__init__(self)
        self.__specialUpperKeys = {
            "!": "shift+1",
            "@": "shift+2",
            "$": "shift+4",
            "%": "shift+5",
            "^": "shift+6",
            "*": "shift+8",
            "(": "shift+9"
        }

    def __solve_code(self, key):
        if len(key) != 1:
            raise Exception("Invalid key length")

        if key in self.__specialUpperKeys:
            return self.__specialUpperKeys[key]
        elif key.isalnum():
            if key.isupper():
                code = "shift+" + key.lower()
                return code
            else:
                return key

    def send_key(self, key):
        code = self.__solve_code(key)
        keyboard.send(code)

    def send_chord(self, chord):
        for key in chord:
            self.send_key(key)