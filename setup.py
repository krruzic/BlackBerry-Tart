#!/usr/bin/env python

from distutils.core import setup

setup(name='bbtart',
      version='1.2',
      description="blackberry-py's Tart Project",
      author='blackberry-py project',
      author_email='',
      url='https://github.com/krruzic/blackberry-tart/',
      requires=['pillow'],
      packages=['tartutil', 'tartutil.commands', 'tart', 'tart.bbutilities', 'tart.bbutilities.bb', 'tart.bbutilities.tart', 'tart.bbutilities.pyggles'],
      package_data = {'tart': ['assets/*', 'entry/*', 'tart.hgid'],
                      'tartutil': ['*.png'],
                      'tartutil.commands': ['bar-descriptor-template.xml'],
                      'tartutil.bbutilities': ['libdynload/*']},
      scripts = ['tartutil/packager.py']
     )