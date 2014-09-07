#!/usr/bin/env python

import subprocess

if __name__ == '__main__':
    subprocess.call(['apt-get', '-y', 'install', 'python-pip'])
    subprocess.call(['pip', 'install', 'fig'])
