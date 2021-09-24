import sys
import jsons
from argparse import ArgumentParser
from core.vp.parser import parse_into
from core import Sheet
from player import Player


def parse_stdin(**flags) -> Sheet:
    sheet = Sheet()
    parse_into(sheet, sys.stdin, flags)

    return sheet


def play(args):
    from player.input_wrappers.pynput import PynputWrapper
    from player.input_wrappers.keyboard import KeyboardWrapper

    # TODO: get this from a configuration file mayhaps
    default_input_wrapper = PynputWrapper()

    sheet = parse_stdin(newline_pauses=args.flag_newline_pauses)
    player = Player(sheet=sheet)

    if args.tempo:
        player.set_tempo(args.tempo)

    input_wrapper = default_input_wrapper
    if args.input_wrapper == "keyboard":
        input_wrapper = KeyboardWrapper()

    player.set_input_wrapper(input_wrapper)
    player.play()


def parse():
    sheet = parse_stdin()
    sys.stdout.write(jsons.dumps(sheet))


if __name__ == "__main__":
    argparser = ArgumentParser(
        description="""Edit, step through or autoplay virtual piano sheets"""
    )
    subcommand = argparser.add_subparsers("subcommand")
    parse_parser = subcommand.add_parser("parse", func=parse)

    play_parser = subcommand.add_parser("play", aliases=["p"], func=play)
    play_parser.add_argument("--input-wrapper", "-w",
                             dest="input_wrapper",
                             type=str,
                             default="pynput",
                             help="""
                             Use an input wrapper preferable to your system configuration
                                pynput - preferable on X11
                                keyboard - preferable on Microsoft Windows
                             """)
    play_parser.add_argument("--tempo", "-t",
                             dest="tempo",
                             type=float,
                             help="""
                             Overrides the tempo of the sheet being played. If not provided,
                             uses the sheet's tempo or default (120)
                             """)
    play_parser.add_argument("--newline-pauses", "-N",
                             dest="flag_newline_pauses",
                             action="store_true")

    args = argparser.parse_args()
