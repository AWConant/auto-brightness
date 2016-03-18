# auto-brightness
To be run in a .bash_profile to automatically adjust screen brightness using xrandr. Because school computers vary in terms of the connected display number, this script parses the output of 'xrandr' and then runs it with the appropriate display code and the given brightness setting. Use the following template in .bash_profile to suppress errors when ssh'd.

if [ -z "$SSH_CLIENT" ] ; then
  ~/brightness.py 0.7
fi
