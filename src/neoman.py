#!/usr/bin/python3

import subprocess
import time
import readchar
from arguments import handle_arguments
from MDConverter import stringToMD

import random
import string


def random_string(length):
    allowed_chars = string.ascii_letters
    return ''.join(random.choice(allowed_chars) for x in range(length))


def output_to_tmp_file(content):
    filename = '/tmp/neoman_' + str(random_string(20))
    with open(filename, 'w+') as f:
        f.write(content)
    return filename


def getMan(command):
    ps = subprocess.Popen(
        f"man {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    return output.decode()


if __name__ == "__main__":
    args = vars(handle_arguments())
    command = args['command'][0]
    man = getMan(command)
    md = stringToMD(man)
    path = output_to_tmp_file(md)
    print(path)
