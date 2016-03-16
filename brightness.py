#!/usr/bin/env python

import os
import subprocess
import sys

bright = str(sys.argv[1])

#os.system('xrandr > 83hfjnfkjsbnefgkjsnefk')
#
#with open('83hfjnfkjsbnefgkjsnefk', 'r') as f:
#    out = f.read()

out = subprocess.check_output('xrandr')

out =  out.split('\n')
out =  out[1:len(out)-1]

for line in out:
    cur = line.split()
    if cur[1] == 'connected':
        dp = cur[0]
        break

os.system('xrandr --output '+dp+' --brightness '+bright)

#os.system('rm -f 83hfjnfkjsbnefgkjsnefk')
