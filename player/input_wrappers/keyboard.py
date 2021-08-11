import keyboard
from base import BaseInputWrapper

class KeyboardWrapper(BaseInputWrapper):

    def __init__(self):
        BaseInputWrapper.__init__(self)
        self.__specialUpperKeys = {
            "!": "shift+1",
            "@": "shift+2",
            "#": "shift+3",
            "$": "shift+4",
            "%": "shift+5",
            "^": "shift+6",
            "&": "shift+7",
            "*": "shift+8",
            "(": "shift+9",
            ")": "shift+0",
        }

    def send_key(self, key):
        pass

    def send_chord(self, key):
        pass