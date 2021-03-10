#!/usr/bin/env python3

import argparse
import os
import sys

parser = argparse.ArgumentParser(
    description='Enable ssh on a boot volume')

parser.add_argument(
    '--volume',
    dest='volume',
    action='store',
    required=False,
    default="/Volumes/boot",
    type=str,
    help='Path to boot volume'
)

args = parser.parse_args()

if (not os.path.isdir(args.volume)):
    sys.exit("Path % s is not a directory" % args.volume)

with open(os.path.join(args.volume, 'ssh'), 'w') as fp:
    pass

os.system("diskutil unmount '% s'" % args.volume)
