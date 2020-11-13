from subprocess import run
from time import sleep


def add_parser(subparsers):
    parser = subparsers.add_parser('q', help='Queue jobs')
    parser.set_defaults(func=queue_user_cmd)
    parser.add_argument('node')
    parser.add_argument('script')


def queue_user_cmd(args):
    outfile = '%s.txt' % args.node
    queue_cmd(outfile, args.node, args.script)


def queue_cmd(outfile, node, script):
    cmd = 'rm -f %s' % outfile
    cmd += (
        ' && qsub -q batch@v-qsvr-nda -j oe -o %s'
        ' -l nodes=%s:ppn=2 -d . %s'
        % (
            outfile,
            node,
            script,
        )
    )
    print(cmd)
    run(cmd, shell=True)
    print('  waiting', flush=True, end='')
    while True:
        try:
            with open(outfile) as fin:
                print('')
                print(fin.read(), end='')
            return
        except Exception:
            print('.', flush=True, end='')
            sleep(2)
