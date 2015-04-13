''' Deploy an app based on parameters read from an ini file.
    Runs `package` and `install`
'''

import sys
import os
import configparser
import argparse
import errno
import subprocess

from .package import Command as packagecmd
from .install import Command as installcmd
from .. import command, project
from ..core import tart

import tart as tartImport

class Command(command.Command):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = os.getcwd()
        self.pkg_cmd = packagecmd()
        self.inst_cmd = installcmd()

    def add_arguments(self, parser):
        parser.add_argument('-c', '--config', metavar='INI FILE',
            help="File to read cmd arguments from", required=True)

    def config(self, name, section='package', default=None):
        '''Convenience routine to grab data from the default section.'''
        return self.ini.get(section, name, fallback=default)

    def ini(self):
        ini = configparser.ConfigParser()
        ini.read(os.path.join(self.root, self.args.config))
        return ini

    def run(self, args):
        self.args = args
        self.ini = self.ini()
        pkg_parser = argparse.ArgumentParser()
        self.pkg_cmd.add_arguments(pkg_parser)

        pkg_arr = []
        for arg in self.ini['package']:
            pkg_arr.append("--" + arg)
            pkg_arr.append(self.config(arg, 'package'))

        self.pkg_cmd.run(pkg_parser.parse_args(pkg_arr))

        inst_parser = argparse.ArgumentParser()
        self.inst_cmd.add_arguments(inst_parser)

        inst_arr = []
        for arg in self.ini['install']:
            inst_arr.append("--" + arg)
            inst_arr.append(self.config(arg, 'install'))

        self.inst_cmd.run(inst_parser.parse_args(inst_arr))