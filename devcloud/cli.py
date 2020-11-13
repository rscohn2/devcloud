from argparse import ArgumentParser
from subprocess import run
from sys import exit
from time import sleep


def get_args():
    parser = ArgumentParser()
    parser.add_argument("node")
    parser.add_argument("script")
    return parser.parse_args()


def queue_cmd(args):
    outfile = "%s.txt" % args.node
    cmd = "rm -f %s" % outfile
    cmd += (
        " && qsub -q batch@v-qsvr-nda -j oe -o %s"
        " -l nodes=%s:ppn=2 -d . %s"
        % (
            outfile,
            args.node,
            args.script,
        )
    )
    print(cmd)
    run(cmd, shell=True)
    print("  waiting", flush=True, end="")
    while True:
        try:
            with open(outfile) as fin:
                print("")
                print(fin.read(), end="")
            exit(0)
        except Exception:
            print(".", flush=True, end="")
            sleep(2)


def main():
    args = get_args()
    queue_cmd(args)
