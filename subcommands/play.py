from argparse import RawTextHelpFormatter
from textwrap import dedent
from player import Player
from util.project.common import parse_stdin


def play(args):
    from player.input_wrappers.pynput import PynputWrapper
    from player.input_wrappers.keyboard import KeyboardWrapper

    # TODO: determine this from OS
    default_input_wrapper = PynputWrapper()

    sheet = parse_stdin(newline_pauses=args.flag_newline_pauses)
    player = Player(sheet=sheet)

    if args.tempo:
        player.set_tempo(args.tempo)
    if args.seek:
        player.set_cursor(args.seek)

    input_wrapper = default_input_wrapper
    if args.input_wrapper == "keyboard":
        input_wrapper = KeyboardWrapper()

    player.set_input_wrapper(input_wrapper)
    try:
        player.play()
    except KeyboardInterrupt:
        pass

    print(player.cursor)


def add_command(subcommand):
    play_parser = subcommand.add_parser("play",
                                        aliases=["p"],
                                        formatter_class=RawTextHelpFormatter,
                                        help="""
                                        Plays a virtual sheet from `stdin`.
                                        Outputs seeker value on exit to `stdout`""")

    play_parser.set_defaults(func=play)
    play_parser.add_argument("--input-wrapper", "-w",
                             dest="input_wrapper",
                             type=str,
                             default="pynput",
                             help=dedent("""
                             Use an input wrapper preferable to your system configuration
                             \tpynput - preferable on X11, macOS
                             \tkeyboard - preferable on Microsoft Windows
                             """))
    play_parser.add_argument("--seek", "-s",
                             dest="seek",
                             type=int,
                             help="Start the player at the provided number")
    play_parser.add_argument("--tempo", "-t",
                             dest="tempo",
                             type=float,
                             help=dedent("""
                             Overrides the tempo of the sheet being played. If not provided,
                             uses the sheet's tempo or default (120)
                             """))
    play_parser.add_argument("--newline-pauses", "-N",
                             dest="flag_newline_pauses",
                             action="store_true",
                             help="Toggle whether a newline should count as a pause note")
