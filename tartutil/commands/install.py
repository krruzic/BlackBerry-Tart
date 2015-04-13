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
        parser.add_argument('-r', '--release', metavar='RELEASE',
            help="Include to sign the bar before deploying (include storepass)")
        parser.add_argument('-p', '--password', default='', metavar='PASSWORD',
            help="The device's password")
        parser.add_argument('-d', '--device', default='169.254.0.1', metavar='IP',
            help='Device IP address (default: %(default)s')
        parser.add_argument('-b', '--bar', default='.', metavar='PACKAGE',
            help='The package to install')
        parser.add_argument('-v', '--verbose', action='store_true',
            help='spew more details')

    def run(self, args):
        sign = ['blackberry-signer']
        deploy = ['blackberry-deploy', '-installApp']
        self.args = args

        def opt(cmd, *args):
            cmd.extend(args)

        opt(deploy, '-password', args.password)
        opt(deploy, '-device', args.device)
        opt(deploy, '-package', args.bar)

        if args.verbose:
            print('install args: ', args)

        if args.release:
            opt(sign, '-storepass', args.release)
            opt(sign, args.bar)
            res, err = self.do_cmd(sign)
            if err:
                self.handle_err(err)
            print(res)

        res, err = self.do_cmd(deploy)
        if err:
            self.handle_err(err)
        if (res.splitlines()[-1] == "result::success"):
            print(self.args.bar + " successfully installed to " + self.args.device)

    def do_cmd(self, cmd):
        if self.args.verbose:
            print('do_cmd:', cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.stdout.read().decode('ascii').strip()
        stderr = p.stderr.read().decode('ascii').strip()
        return (output, stderr)

    def handle_err(self, err):
        if 'unreachable' in err or 'cannot' in err:
            print("Error connecting to: " + self.args.device + ", install failed!")
        else:
            print(err)
        sys.exit(-1)