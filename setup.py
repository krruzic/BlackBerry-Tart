#!/usr/bin/env python

from distutils.core import setup

setup(name='bbtart',
      version='1.0',
      description='blackberry-py libraries',
      author='blackberry-py project',
      author_email='',
      url='https://bitbucket.org/microcode/blackberry-py/',
      packages=['tartutil', 'tartutil.commands', 'tart', 'tart.bbutilities', 'tart.bbutilities.bb', 'tart.bbutilities.tart', 'tart.bbutilities.pyggles'],
      package_data = {'tart': ['assets/*', 'entry/*', 'tart.hgid'],
                      'tartutil': ['*.png'],
                      'tartutil.commands': ['bar-descriptor-template.xml', 'app_template/*'],
                      'tartutil.bbutilities': ['libdynload/*']},
     )