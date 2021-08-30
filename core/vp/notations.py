"""Somewhat arbitrary notations from the varied amount of virtual piano music sheets seen online."""

# notes that indicate pausing
PAUSE = {
    "eight": {
        "symbols": [",", "-"],
        "scale": 1 / 8
    },
    "quarter": {
        "symbols": ["'", "="],
        "scale": 1 / 4
    },
    "half": {
        "symbols": ["|"],
        "scale": 1 / 2
    },
    "whole": {
        "symbol": ":",
        "scale": 1
    }
}

# used for more precise control over note values. e.g: every < splits further by 2
# more examples:
# <[qwerty]<[qwerty] -> play [qwerty][qwerty] by
#                       1/16 1/16 rhythmic value instead of 1/8 1/8
# q>w>e>r>t>y> -> play every note as half note rather than quarter note (1/2, 1/4)
NOTE_VALUES = {
    "less": {"symbol": "<"},
    "more": {"symbol": ">"}
}

# notes which are played simultaneously
CHORDS = {"begin": {"symbol": "["}, "end": {"symbol": "]"}}

# notes which are played VERY FAST but not simultaneously
# assumably, this is used with 1/16 rhyhtmic values
BROKEN_CHORDS = {"begin": {"symbol": "{"}, "end": {"symbol": "}"}}
