#!/usr/bin/python3

import subprocess
import argparse


def execute_command(commands):
    try:
        return subprocess.check_output(commands.split())
    except subprocess.CalledProcessError as err:
        print(err)


def handle_arguments():
    parser = argparse.ArgumentParser(
        description='NeoMan - Beautiful & Powerfull man reader')

    """
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    """
    args = parser.parse_args()


if __name__ == "__main__":
    handle_arguments()
    pass
