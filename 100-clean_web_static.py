#!/usr/bin/python3
"""  This module uses fabric to refresh archieves"""
import os
from fabric.api import *

env.hosts = ["34.139.153.52", "18.208.132.140"]


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archieves to keep
        Keep the most recent only
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
