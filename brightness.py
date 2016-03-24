#!/usr/bin/env python

import os
import subprocess
import sys

"""
Andrew Conant
Spring 2016
For use in .bash_profile; parses output of xrandr and uses it to properly
set brightness for that display.
"""

# Sanitize input
try:
    bright = str(sys.argv[1])
except IndexError:
    print 'Usage: ./brightness.py <0.1 - 1.0>'
    exit(1) 

# Grabs output of 'xrandr' on linux machine
out = subprocess.check_output('xrandr')

# Chops out useless elements of the output
out =  out.split('\n')
out =  out[1:len(out)-1]

# Seeks the connected display value
for line in out:
    cur = line.split()
    if cur[1] == 'connected':
        dp = cur[0]
        break

# Sets brightness
os.system('xrandr --output '+dp+' --brightness '+bright)
