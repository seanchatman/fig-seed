#!/usr/bin/env python

import subprocess

if __name__ == '__main__':
    subprocess.call(['python', 'get-pip.py'])
    subprocess.call(['pip', 'install', 'fig'])
