#!/usr/bin/python3
"""
This module deploys the files web_static from archived files
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['34.139.153.52', '18.208.132.140']


def do_pack():
    """Archives our files"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date)
    if not os.path.isdir("versions"):
        local(" mkdir versions")
    local('tar -cvzf ' + file_path + ' web_static')
    if os.path.exists(file_path):
        return file_path
    return None


def do_deploy(archive_path):
    """Deploys archive files"""
    if not os.path.exists(archive_path):
        return False
    arch_name = archive_path.split('/')[1]
    arch_name_nex = arch_name.split(".")[0]
    re_path = "/data/web_static/releases/" + arch_name_nex
    up_path = '/tmp/' + arch_name
    put(archive_path, up_path)
    run('mkdir -p ' + re_path)
    run('tar -xzf /tmp/{} -C {}/'.format(arch_name, re_path))
    run('rm {}'.format(up_path))
    mv = 'mv ' + re_path + '/web_static/* ' + re_path + '/'
    run(mv)
    run('rm -rf ' + re_path + '/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s ' + re_path + ' /data/web_static/current')
    return True


def deploy():
    """Implements deploy"""
    path = do_pack()
    if not path:
        return False
    deploy = do_deploy(path)
    if not deploy:
        return False
    return deploy
