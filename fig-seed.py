#!/usr/bin/env python
""" Fig Seed, plant your project.

Usage:
  fig-seed.py list
  fig-seed.py [-v] kill
  fig-seed.py [-v] stop
  fig-seed.py [-v] up <template_name>
  fig-seed.py [-v] sample <template_name>
  fig-seed.py [-uv] init [<template_name> <target_directory>]

  -v, --verbose       verbose mode
  -u, --up            fig up -d

Arguments:
  template_name        folder name in template directory
  target_directory     where the template is copied.


Example: fig-seed.py init /tmp/init
         fig-seed.py init fig-flask /tmp/fig-flask
"""
from docopt import docopt

import os
import shutil
import subprocess
import shelve
import docker

__author__ = 'arby'

#docker run --rm -v /usr/local/bin:/target jpetazzo/nsenter
#docker-enter a30645361de9 ls -la

fig_dir = os.path.expanduser("~")+'/.figseed'


def get_client():
    try:
    #     url = os.environ['DOCKER_HOST']
        url = 'unix://var/run/docker.sock'
    except KeyError, e:
        print 'Please check that the $' + e.message + ' environment variable is properly set.'
        raise SystemExit

    return docker.Client(base_url=url,
                       timeout=10)


def create_folder():
    if not os.path.isdir(fig_dir):
        os.mkdir(fig_dir)


def vprint(value):
    if args['-v']:
        print value


def call(call_args):
    subprocess.call(call_args)


def list_templates():
    template_dir = os.getcwd() + '/template'
    templates = os.listdir(template_dir)

    print('Template list:')
    for x in templates:
        print(x)


def export(name, dest, template_dir):
    if os.path.isdir(dest):
        vprint('Found %s, removing.' % dest)
        shutil.rmtree(dest)

    vprint('Copying to %s.' % dest)

    template = template_dir + '/' + name
    shutil.copytree(template, dest)

    if args['-v']:
        for root, dirs, files in os.walk(dest):
            for dest_file in files:
                print 'Copied %s.' % dest_file


def init():
    template_dir = os.getcwd() + '/template'

    if args['<template_name>']:
        template_name = args['<template_name>']
    else:
        template_name = 'init'

    if args['<target_directory>']:
        target_dir = args['<target_directory>']
    else:
        target_dir = '/tmp/' + template_name

    vprint('Creating %s at %s.' % (template_name, template_dir))

    export(template_name, target_dir, template_dir)

    if args['-u']:
        os.chdir(target_dir)
        call(["fig", "up", "-d"])


def up():
    target_dir = os.getcwd() + '/template/' + args['<template_name>']
    os.chdir(target_dir)
    call(["fig", "up", "-d"])

    client = get_client()

    with open(fig_dir+"/up", "w") as upfile:
        for container in client.containers():
            upfile.write(str(dir(container)))


def kill():
    # TODO only kill containers initiated by fig-seed.py
    try:
        answer = raw_input('Kill all running containers? [Y,n] ')
        if 'n' in answer.lower():
            raise SystemExit
        else:
            client = get_client()

            for container in client.containers():
                client.kill(container)
                c = container
                vprint('Killed s% s% s%' % c['Id'][:12], c['Command'], c['Status'])
    except KeyboardInterrupt:
        raise SystemExit


def stop():
    # TODO only kill containers initiated by fig-seed.py
    try:
        answer = raw_input('Stop all running containers? [Y,n] ')
        if 'n' in answer.lower():
            raise SystemExit
        else:
            client = get_client()

            for container in client.containers():
                client.stop(container)
                c = container
                vprint('Stopped s% s% s%' % c['Id'][:12], c['Command'], c['Status'])
    except KeyboardInterrupt:
        raise SystemExit




if __name__ == '__main__':
    args = docopt(__doc__, version='fig-seed 0.3')

    create_folder()

    if args['list']:
        list_templates()

    if args['init']:
        init()

    if args['up']:
        up()

    if args['sample']:
        up()

    if args['stop']:
        stop()

    if args['kill']:
        kill()
