from sys import stdout
from time import sleep
from threading import Thread
from core import Sheet
from core import Note
from core import Chord
from player.input_wrappers.base import BaseInputWrapper


class Player:
    def __init__(self, sheet: Sheet, input_wrapper: BaseInputWrapper = None):
        self.input = input_wrapper
        self.sheet = sheet
        self.tempo = sheet.tempo
        self.cursor = -1
        self.__thread = None
        self.playing = False

    def step(self):
        if self.cursor + 1 >= len(self.sheet.track):
            raise Exception(
                f"cursor cannot exceed track length @{self.cursor + 1} > {len(self.sheet.track)}")

        if not isinstance(self.input, BaseInputWrapper):
            raise Exception("no active input wrapper")

        self.cursor = self.cursor + 1
        entry = self.sheet.track[self.cursor]
        if isinstance(entry, Chord):
            self.input.send_chord(entry)
        elif isinstance(entry, Note):
            self.input.send_note(entry)
        else:
            print(f"unknown instance in track (@{self.cursor}")

        return entry

    def stop(self):
        self.cursor = -1
        self.playing = False

    def set_cursor(self, index: int):
        if index < -1 or index > len(self.sheet.track):
            raise Exception("cursor cannot be lower than -1 or above sheet's note count")

        self.cursor = index

    def set_tempo(self, tempo: float):
        self.tempo = tempo

    def set_input_wrapper(self, input_wrapper: BaseInputWrapper):
        if isinstance(input_wrapper, BaseInputWrapper):
            self.input = input_wrapper
        else:
            raise Exception("input wrapper doesn't extend from BaseInputWrapper")

    def play(self, asynchronous: bool = False):
        self.playing = True

        if asynchronous and not self.__thread:
            self.__thread = Thread(target=self.__play_loop, args=(self,))
            self.__thread.start()
        elif not asynchronous:
            self.__play_loop()

    def pause(self):
        self.playing = False

    def __play_loop(self):
        while self.playing and self.cursor + 1 < len(self.sheet.track):
            entry = self.step()

            # TODO: figure out how to use beats per measure for sleeping
            sleep_time = (60 / self.tempo) * (4 * entry.value)

            stdout.write(f"n{entry.value} s{sleep_time}; ")
            sleep(sleep_time)
