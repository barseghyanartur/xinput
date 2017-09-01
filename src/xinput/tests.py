from __future__ import print_function

import unittest

__title__ = 'xinput.tests'
__author__ = 'Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__copyright__ = '2013-2017 Artur Barseghyan'


PRINT_INFO = True


def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        print('\n\n%s' % func.__name__)
        print('============================')
        if func.__doc__:
            print('""" %s """' % func.__doc__.strip())
        print('----------------------------')
        if result is not None:
            print(result)
        print('\n++++++++++++++++++++++++++++')

        return result
    return inner


class XinputTest(unittest.TestCase):
    """
    Tests.
    """
    def setUp(self):
        """
        Set up.
        """

    @print_info
    def test_01_xinput_operate_command(self):
        """
        Test xinput operate command.
        """

    @print_info
    def test_02_xinput_disable_touchpad_command(self):
        """
        Test xinput disable-touchpad command.
        """

    @print_info
    def test_03_xinput_enable_touchpad_command(self):
        """
        Test xinput enable-touchpad command.
        """

    @print_info
    def test_04_xinput_api(self):
        """
        Test xinput API.
        """
