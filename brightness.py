#!/usr/bin/env python

import os
import subprocess
import sys

try:
    bright = str(sys.argv[1])
except IndexError:
    print 'Usage: ./brightness.py <0.1 - 1.0>'
    exit(1) 

out = subprocess.check_output('xrandr')

out =  out.split('\n')
out =  out[1:len(out)-1]

for line in out:
    cur = line.split()
    if cur[1] == 'connected':
        dp = cur[0]
        break

os.system('xrandr --output '+dp+' --brightness '+bright)
