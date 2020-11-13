from argparse import ArgumentParser

from devcloud import q, show


def parse_args():
    parser = ArgumentParser(description='CLI for devcloud')
    parser.add_argument(
        '--verbose', action='store_true', help='display log information'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='do not perform actions that modify system state',
    )
    subparsers = parser.add_subparsers(dest='cmd')
    subparsers.required = True
    q.add_parser(subparsers)
    show.add_parser(subparsers)
    return parser.parse_args()


def setup():
    pass


def main():
    args = parse_args()
    setup()
    args.func(args)
