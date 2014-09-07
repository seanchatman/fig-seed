#!/usr/bin/env python
""" Fig Seed, plant your project.

Usage:
  fig-seed.py list
  fig-seed.py up <template_name>
  fig-seed.py sample <template_name>
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

__author__ = 'arby'

#docker run --rm -v /usr/local/bin:/target jpetazzo/nsenter
#docker-enter a30645361de9 ls -la

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


if __name__ == '__main__':
    args = docopt(__doc__, version='fig-seed 0.3')

    if args['list']:
        list_templates()

    if args['init']:
        init()

    if args['up']:
        up()

    if args['sample']:
        up()
