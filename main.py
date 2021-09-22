import sys
import jsons
from argparse import ArgumentParser
from core.vp.parser import parse_into
from core import Sheet
from player import Player


def parse_stdin() -> Sheet:
    sheet = Sheet()
    parse_into(sheet, sys.stdin)
    return sheet


if __name__ == "__main__":
    argparser = ArgumentParser(
        description="""Edit, step through or autoplay virtual piano sheets"""
    )
    argparser.add_argument("subcommand",
                           type=str,
                           help="""
                           parse - outputs a JSON from virtual piano sheet
                           """
                           )

    argparser.add_argument("--input-wrapper", "-w",
                           dest="input_wrapper",
                           type=str,
                           default="pynput",
                           help="""
                           Use an input wrapper preferable to your system configuration
                           (on Mac, both require root)
                               pynput - preferable on X11
                               keyboard - preferable on Microsoft Windows OS (requires root on *nix)
                           """)
    argparser.add_argument("--tempo", "-t",
                           dest="tempo",
                           type=float,
                           help="""
                           Overrides the tempo of the sheet being played. If not provided,
                           uses the sheet's tempo or default (110)
                           """)

    args = argparser.parse_args()

    if args.subcommand == "parse":
        sheet = parse_stdin()
        sys.stdout.write(jsons.dumps(sheet))

    if args.subcommand == "play":
        from player.input_wrappers.pynput import PynputWrapper
        from player.input_wrappers.keyboard import KeyboardWrapper

        # TODO: get this from a configuration file mayhaps
        default_input_wrapper = PynputWrapper()

        sheet = parse_stdin()
        player = Player(sheet=sheet)

        if args.tempo:
            player.set_tempo(args.tempo)

        input_wrapper = default_input_wrapper
        if args.input_wrapper == "keyboard":
            input_wrapper = KeyboardWrapper()

        player.set_input_wrapper(input_wrapper)
        player.play()
