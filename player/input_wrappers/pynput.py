from .base import BaseInputWrapper
from pynput import keyboard


class PynputWrapper(BaseInputWrapper):
    def send_chord(self, chord):
        raise NotImplementedError()

    def send_key(self, key):
        raise NotImplementedError()