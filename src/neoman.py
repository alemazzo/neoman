#!/usr/bin/python3

import subprocess
import time
import readchar
from arguments import handle_arguments


def getMan(command):
    ps = subprocess.Popen(
        f"man {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    return output


if __name__ == "__main__":
    args = vars(handle_arguments())
    command = args['command'][0]
    man = getMan(command)
    print(man)
