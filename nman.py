#!/usr/bin/python3

import subprocess
from arguments import handle_arguments


def execute_command(commands):
    try:
        return subprocess.check_output(commands.split())
    except subprocess.CalledProcessError as err:
        print(err)


if __name__ == "__main__":
    args = handle_arguments()
    command = args.command[0]
    print(command)
