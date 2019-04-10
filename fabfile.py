from fabric.api import run, put, execute, task, env, settings, cd, sudo, parallel, prefix
from config import Config

env.hosts = Config.DEPLOY_HOSTS
env.passwords = Config.DEPLOY_PASSWORDS


def deploy(mode=''):
    with settings(sudo_user='webmaster'):
        with cd('/home/webmaster/annotation-tool'):
            sudo("sudo git pull origin master")
            with prefix('source /home/webmaster/annotation-tool/ENV/bin/activate'):
                sudo("uwsgi --reload uwsgi.pid")
