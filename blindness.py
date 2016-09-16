#!/usr/bin/env python

import os
import subprocess
import sys


# Sanitize input
try:
    bright = str(sys.argv[1])
except IndexError:
    print 'Usage: ./brightness.py <0.1 - 1.0>'
    exit(1) 

out = subprocess.check_output('xrandr').splitlines()
out = out[1:len(out)-1]

# Seeks the connected display value
for line in out:
    if 'connected' in line.split():
        dp = line.split()[0]
        break

# Sets brightness
os.system('xrandr --output %s --brightness %s' % (dp, bright))
