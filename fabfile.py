from fabric.api import *

#env.hosts = ["ubuntu@34.139.153.52"]
@task(alias="cd")
def change_dir():
    """changes currect directory"""
    cd("/etc/")

