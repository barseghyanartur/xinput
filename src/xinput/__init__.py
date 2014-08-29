__title__ = 'xinput'
__version__ = '0.1.3'
__build__ = 0x000004
__author__ = 'Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__copyright__ = 'Copyright 2013-2014 Artur Barseghyan'
__all__ = (
    'operate_xinput_device', 'MODE_ENABLE', 'DEVICE_NAME_TOUCHPAD',
    'MODE_DISABLE', 'DEVICE_NAME_SYNAPTIC_TOUCHPAD',
    'DEVICE_NAME_ELANTECH_TOUCHPAD', 'DEFAULT_DEVICE_NAME',

    # For backwards compatibility
    'DEVICE_NAME_SYNAPTIC',
)

from xinput.operate_xinput_device import (
    operate_xinput_device, MODE_ENABLE, DEVICE_NAME_TOUCHPAD,
    MODE_DISABLE, DEVICE_NAME_SYNAPTIC_TOUCHPAD,
    DEVICE_NAME_ELANTECH_TOUCHPAD, DEFAULT_DEVICE_NAME,

    # For backwards compatibility
    DEVICE_NAME_SYNAPTIC
)
