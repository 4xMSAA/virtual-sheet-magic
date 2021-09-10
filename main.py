import sys
import jsons
from argparse import ArgumentParser
from core.vp.parser import parse_into
from core.sheet import Sheet

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

    args = argparser.parse_args()

    if args.subcommand == "parse":
        sheet = Sheet()
        parse_into(sheet, sys.stdin)
        sys.stdout.write(jsons.dumps(sheet))
