'''Install an app on a USB device.'''

import sys
import os
import configparser
import errno
import subprocess

from .. import command, project
from ..core import tart

import tart as tartImport

class Command(command.Command):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def add_arguments(self, parser):
        parser.add_argument('password', default='', metavar='PASSWORD',
            help="The device's password")
        parser.add_argument('device', default='169.254.0.1', metavar='IP',
            help='Device IP address (default: %(default)s')
        parser.add_argument('package', metavar='BAR FILE',
            help='The package to install')
        parser.add_argument('-v', '--verbose', action='store_true',
            help='spew more details')

    def run(self, args):
        command = ['blackberry-deploy', '-installApp']

        self.args = args
        if args.verbose:
            print('install args: ', args)

        def opt(*args):
            command.extend(args)

        opt('-password', args.password)
        opt('-device', args.device)
        opt('-package', args.package)

        res, err = self.do_cmd(command)
        if err:
            self.handle_err(err)
        if (res.splitlines()[-1] == "result::success"):
            print(self.args.package + " successfully installed to " + self.args.device)

    def do_cmd(self, cmd):
        if self.args.verbose:
            print('do_cmd:', cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.stdout.read().decode('ascii').strip()
        stderr = p.stderr.read().decode('ascii').strip()
        return (output, stderr)

    def handle_err(self, err):
        if 'unreachable' in err:
            print("Error connecting to: " + self.args.device + ", install failed!")
        else:
            print(err)
        sys.exit(-1)