#!/usr/bin/python3

import subprocess
import time
import readchar
from arguments import handle_arguments


def execute_command(commands):

    ps = subprocess.Popen(
        commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    return output


if __name__ == "__main__":
    args = vars(handle_arguments())
    command = f"man {args['command'][0]} | mdvl "
    """
    if 'search' in args.keys():
        command += f" | grep \"{args['search']}\" "
    """
    print(execute_command(command).decode())
