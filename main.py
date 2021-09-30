from argparse import ArgumentParser
from subcommands import play, parse
SUBCOMMANDS = (play, parse)


argparser = ArgumentParser(
    description="""Edit, step through or autoplay virtual piano sheets"""
)
subcommand_parser = argparser.add_subparsers()
for subcommand in SUBCOMMANDS:
    subcommand.add_command(subcommand_parser)


def main(args):
    args.func(args)


if __name__ == "__main__":
    args = argparser.parse_args()
    main(args)
