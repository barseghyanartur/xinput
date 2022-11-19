from __future__ import print_function

import os
import re
import sys
import getopt

__title__ = 'xinput.operate_xinput_device'
__author__ = 'Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__copyright__ = 'Copyright 2013-2017 Artur Barseghyan'
__all__ = (
    'DEVICE_NAME_ELANTECH_TOUCHPAD',
    'DEVICE_NAME_SYNAPTIC_TOUCHPAD',
    'DEVICE_NAME_TOUCHPAD',
    'MODE_DISABLE',
    'MODE_ENABLE',
    'operate_xinput_device',
    'VERBOSITY_DEBUG',
    'VERBOSITY_ERROR',
    'VERBOSITY_INFO',
    'VERBOSITY_NONE',
)


MODE_ENABLE = '1'
MODE_DISABLE = '0'
DEFAULT_MODE = MODE_DISABLE

DEVICE_NAME_TOUCHPAD = 'Synaptics TouchPad'
DEVICE_NAME_SYNAPTIC_TOUCHPAD = 'Synaptics TouchPad'
DEVICE_NAME_ELANTECH_TOUCHPAD = 'Elantech TouchPad'
DEFAULT_DEVICE_NAME = DEVICE_NAME_TOUCHPAD
VERBOSITY_DEBUG = 3
VERBOSITY_INFO = 2
VERBOSITY_ERROR = 1
VERBOSITY_NONE = 0

# For backwards compatibility
DEVICE_NAME_SYNAPTIC = DEVICE_NAME_SYNAPTIC_TOUCHPAD


def operate_xinput_device(mode=None,
                          device_name=None,
                          verbosity=VERBOSITY_NONE):
    """Operates touchpad.

    :param mode:
    :param device_name:
    :param verbosity:
    :type mode: str
    :type device_name: str
    :type mode: bool
    """
    if mode not in (MODE_ENABLE, MODE_DISABLE):
        mode = DEFAULT_MODE
    if not device_name:
        device_name = DEFAULT_DEVICE_NAME
    try:
        # We simply rely on "xinput" command. We grep "Synaptics TouchPad"
        # word there.
        shell_response = os.popen(
            'xinput list | grep -i "{0}"'.format(str(device_name))
        ).read()
        if verbosity == VERBOSITY_DEBUG:
            print(shell_response)
        # RegEx to grab device ID
        regex = re.compile('id=(?P<line>\d+)', re.IGNORECASE)
        # Grab device ID. If any errors occur, device name is invalid (no
        # such device).
        try:
            touchpad_id = regex.findall(shell_response)[0]
            if verbosity == VERBOSITY_DEBUG:
                print(touchpad_id)
        except Exception as err:
            raise Exception(
                'No such device "{0}". Type "xinput list" in terminal to see'
                ' the list of available devices.'.format(str(device_name))
            )
        # Our command to enable/disable device.
        os.system(
            'xinput set-prop {0} "Device Enabled" '
            '{1}'.format(touchpad_id, str(mode))
        )
    except Exception as err:
        print(err)


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
            print(operate_xinput_device.__doc__)
            sys.exit(0)
    # Process arguments
    try:
        mode = args[0]
    except Exception as err:
        mode = None
    try:
        device_name = ' '.join(args[1:])
    except Exception as err:
        device_name = None

    operate_xinput_device(mode, device_name)


if __name__ == "__main__":
    main()
