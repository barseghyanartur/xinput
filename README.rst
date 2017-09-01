======
xinput
======
Enable/disable xinput devices (for example, a touchpad) from terminal or using
the API.

Prerequisites
=============
- Python 2.6.8+, 2.7.+, 3.3.+

Installation
============
Latest stable version from PyPI.

.. code-block:: sh

    pip install xinput

Latest stable version from BitBucket.

.. code-block:: sh

    pip install https://bitbucket.org/barseghyanartur/xinput/get/stable.tar.gz

Latest stable version from GitHub.

.. code-block:: sh

    pip install https://github.com/barseghyanartur/xinput/archive/stable.tar.gz

Usage examples
==============
First argument represents device state (0 for disable and 1 for enable).
Second argument represents device name.

By default we operate with `Synaptics TouchPad` but it's possible to have
custom device names.

After installation you should be able to disable/enable touchpad by typing
"disable-touchpad" or "enable-touchpad" commands in your terminal.

Command-line
------------
To enable Synaptics TouchPad, type in terminal:

.. code-block:: sh

    xinput-manage 1 Synaptic TouchPad

To disable Genius Optical Mouse, type in terminal:

.. code-block:: sh

    xinput-manage 0 Genius Optical Mouse

There are also shortcuts for enabling/disabling the touchpad.

Type the following in terminal to disable the touchpad:

.. code-block:: sh

    disable-touchpad

Type the following in terminal to enable the touchpad:

.. code-block:: sh

    enable-touchpad

Programmatically
----------------

.. code-block:: python

    from xinput import (
        operate_xinput_device,
        MODE_ENABLE,
        DEVICE_NAME_SYNAPTIC,
        MODE_DISABLE,
    )
    operate_xinput_device(MODE_DISABLE, DEVICE_NAME_SYNAPTIC)
    operate_xinput_device(MODE_ENABLE, DEVICE_NAME_SYNAPTIC)

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author` section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
