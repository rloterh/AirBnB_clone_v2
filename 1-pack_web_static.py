#!/usr/bin/python3
""" This module creates a tgz file from
the content of a wep page
"""

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Returns the archived file"""
    date = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                         date.month,
                                                         date.day,
                                                         date.hour,
                                                         date.minute,
                                                         date.second)
    if not (os.path.isdir("versions")):
        if local("mkdir -p versions").failed:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed:
        return None
    return file
