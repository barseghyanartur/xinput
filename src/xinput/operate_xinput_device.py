from __future__ import print_function

__title__ = 'xinput.operate_xinput_device'
__author__ = 'Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__copyright__ = 'Copyright 2013-2014 Artur Barseghyan'
__all__ = (
    'operate_xinput_device', 'MODE_ENABLE', 'DEVICE_NAME_SYNAPTIC', 'MODE_DISABLE',
)

import os
import re
import sys
import getopt

MODE_ENABLE = '1'
MODE_DISABLE = '0'
DEFAULT_MODE = MODE_DISABLE

DEVICE_NAME_SYNAPTIC = 'Synaptics TouchPad'
DEFAULT_DEVICE_NAME = DEVICE_NAME_SYNAPTIC

def operate_xinput_device(mode=None, device_name=None):
    """
    Operates touchpad.

    :param str mode:
    :param str device_name:
    """
    if not mode in (MODE_ENABLE, MODE_DISABLE):
        mode = DEFAULT_MODE
    if not device_name:
        device_name = DEFAULT_DEVICE_NAME
    try:
        # We simply rely on "xinput" command. We grep "Synaptics TouchPad" word there.
        shell_response = os.popen('xinput list | grep "{0}"'.format(str(device_name))).read()
        # RegEx to grab device ID        
        regex = re.compile('id=(?P<line>\d+)', re.IGNORECASE)
        # Grab device ID. If any errors occur, device name is invalid (no such device).        
        try:
            touchpad_id = regex.findall(shell_response)[0]
        except Exception as e:
            raise Exception('No such device "{0}". Type "xinput list" in terminal to see the '
                            'list of available devices.'.format(str(device_name)))
        # Our command to enable/disable device.        
        os.system('xinput set-prop {0} "Device Enabled" {1}'.format(touchpad_id, str(mode)))
    except Exception as e:
        print(e)

def main(args=None):
    # Parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error as msg:
        print(msg)
        print("for help use --help")
        sys.exit(2)
    # Process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print(__doc__)
            sys.exit(0)
    # Process arguments
    try:
        mode = args[0]
    except Exception as e:
        mode = None
    try:
        device_name = ' '.join(args[1:])
    except Exception as e:
        device_name = None

    operate_xinput_device(mode, device_name)


if __name__ == "__main__":
    main()
