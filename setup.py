import sys
import os
from setuptools import setup, find_packages

PROJECT_DIR = lambda base : os.path.abspath(os.path.join(os.path.dirname(__file__), base).replace('\\','/'))

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

exec_dirs = [
    'src/xinput/',
    'src/xinput/bin/',
]

execs = []
for exec_dir in exec_dirs:
    execs += [os.path.join(exec_dir, f) for f in os.listdir(exec_dir)]

install_requires = []

try:
    PY2 = sys.version_info[0] == 2
    PY3 = sys.version_info[0] == 3
except:
    pass

version = '0.1'
title = 'xinput'

setup(
    name = title,
    version = version,
    description = ("Enable/disable xinput devices from terminal."),
    long_description = readme,
    classifiers = [
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords = 'xinput',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://github.com/barseghyanartur/xinput',
    package_dir = {'': 'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    include_package_data = True,
    package_data = {
        'xinput': execs,
    },
    scripts = ['src/xinput/bin/xinput-manage', 'src/xinput/bin/enable-touchpad', 'src/xinput/bin/disable-touchpad',]
)
