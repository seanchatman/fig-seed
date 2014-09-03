#!/usr/bin/env python
""" Fig Seed, plant your project.

Usage:
  fig-seed.py list
  fig-seed.py [-v] init
  fig-seed.py [-v] init <template_name>
  fig-seed.py [-v] init <template_name> <target_directory>


Arguments:
  template_name        folder name in template directory
  target_directory     where the template is copied.

Options:
  -h       --help
  -v       verbose mode

Example: fig-seed.py init /tmp/init
         fig-seed.py init fig-flask /tmp/fig-flask
"""
from docopt import docopt
#from subprocess import call

import os
import shutil

__author__ = 'arby'


def list_templates():
    template_dir = os.getcwd() + '/template'
    templates = os.listdir(template_dir)

    print('Template list:')
    for x in templates:
        print(x)


def export(name, dest, template_dir):
    if os.path.isdir(dest):
        if args['-v']:
            print 'Found %s, removing.' % dest
        shutil.rmtree(dest)

    if args['-v']:
        print 'Copying to %s.' % dest

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

    if args['-v']:
        print 'Creating %s at %s.' % (template_name, template_dir)

    export(template_name, target_dir, template_dir)


if __name__ == '__main__':
    args = docopt(__doc__, version='fig-seed 0.2')

    if args['list']:
        list_templates()

    if args['init']:
        init()