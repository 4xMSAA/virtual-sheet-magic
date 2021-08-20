"""
Somewhat arbitrary notations from the varied amount of
virtual piano music sheets seen online.
"""

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

# notes which are played simultaneously
CHORDS = {"begin": {"symbol": "["}, "end": {"symbol": "]"}}

# notes which are played VERY FAST but not simultaneously
BROKEN_CHORDS = {"begin": {"symbol": "{"}, "end": {"symbol": "}"}}
