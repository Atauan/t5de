#!/usr/bin/env python
import os
from distutils.core import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

setup(
    name='T5DE',
    version=os.getenv('T5DE_VERSION', '1.0.0'),
    description='A modified IMVU client that unlocks useful features.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/dhkatz/t5de',
    packages=['t5de'],
    install_requires=[
      'autogui', 'requests', 'uncompyle2', 'typing'
    ],
    entry_points={
        'console_scripts': [
            't5de = t5de.__main__:main'
        ]
    }
)
