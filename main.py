import sys
import jsons
from argparse import ArgumentParser
from core.vp.parser import parse_into
from core import Sheet
from player import Player
from player.input_wrappers import PynputWrapper, KeyboardWrapper


def parse_stdin() -> Sheet:
    sheet = Sheet()
    parse_into(sheet, sys.stdin)
    return sheet


if __name__ == "__main__":
    # TODO: get this from a configuration file mayhaps
    default_input_wrapper = PynputWrapper()

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
                           pynput - preferable on X11
                           keyboard - preferable on Microsoft Windows OS (requires root on *nix)
                           """)
    argparser.add_argument("--tempo", "-t",
                           dest="tempo",
                           type=float,
                           help="""
                           Overrides the tempo of the sheet being played. If the sheet has
                           """)

    args = argparser.parse_args()
    print(args)

    if args.subcommand == "parse":
        sheet = parse_stdin()
        sys.stdout.write(jsons.dumps(sheet))

    if args.subcommand == "play":
        sheet = parse_stdin()
        player = Player(sheet=sheet)

        if args.tempo:
            player.set_tempo(args.tempo)

        input_wrapper = default_input_wrapper
        if args.input_wrapper == "keyboard":
            input_wrapper = KeyboardWrapper()

        player.set_input_wrapper(input_wrapper)
        player.play()
