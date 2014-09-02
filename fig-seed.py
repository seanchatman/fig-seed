#!/usr/bin/env python
""" Fig Seed, plant your ideas.

Usage:
  fig-seed.py list
  fig-seed.py [-v] init <target_directory>
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
    for x in templates:
        print('Template list:')
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
        if args['-v']:
            print 'Creating %s.' % args['<template_name>']
        export(args['<template_name>'], args['<target_directory>'], template_dir)
    else:
        if args['-v']:
            print 'Creating %s.' % args['<template_name>']
        export('init', args['<target_directory>'], template_dir)


if __name__ == '__main__':
    args = docopt(__doc__, version='fig-seed 0.1')

    if args['list']:
        list_templates()

    if args['init']:
        init()