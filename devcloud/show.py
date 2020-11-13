from pkg_resources import resource_filename

from devcloud.q import queue_cmd


def add_parser(subparsers):
    parser = subparsers.add_parser('show', help='Show resources')
    parser.set_defaults(func=show_cmd)
    parser.add_argument('resource', choices=['free'])


def free(args):
    queue_cmd('free.txt', '1', resource_filename('devcloud', 'data/free.sh'))


def show_cmd(args):
    if args.resource == 'free':
        free(args)
