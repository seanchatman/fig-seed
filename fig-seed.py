""" Fig Seed, plant your ideas.

Usage:
  fig-seed.py list
  fig-seed.py demo <name>

"""
from docopt import docopt

import os, sys, shutil

__author__ = 'arby'


def init(args):
    print args

if __name__ == '__main__':
    args = docopt(__doc__, version='Naval Fate 2.0')
    templateDir = os.getcwd() + '/template'
    templates = os.listdir(templateDir)

    if args['list']:
        print templates

    if args['demo']:
        print args['demo']
        print args['<name>']
        shutil.copytree(templateDir + '/' + args['<name>'], '/tmp/' + args['<name>'])