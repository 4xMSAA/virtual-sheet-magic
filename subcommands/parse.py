from sys import stdout
from util.project.common import parse_stdin


def parse(args):
    from jsons import dumps

    sheet = parse_stdin(newline_pauses=args.flag_newline_pauses)
    # TODO: serialize the sheet better. this is just a lazy fix rn
    stdout.write(dumps(sheet))


def add_command(subcommand):
    parse_parser = subcommand.add_parser("parse")
    parse_parser.set_defaults(func=parse)
    parse_parser.add_argument("--newline-pauses", "-N",
                              dest="flag_newline_pauses",
                              action="store_true")
