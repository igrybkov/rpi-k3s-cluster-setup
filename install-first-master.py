#!/usr/bin/env python3

import argparse
import os
import glob
import sys
import commands

parser = argparse.ArgumentParser(
    description='Make first RPI node configuration')

parser.add_argument(
    '--ip',
    dest='ip',
    action='store',
    required=True,
    type=str,
    help='Node IP address'
)

args = parser.parse_args()

commands.getstatusoutput("ssh machine 1 'your script'")
