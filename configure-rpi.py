#!/usr/bin/env python3

import argparse
import os
import glob
import sys
import json

parser = argparse.ArgumentParser(
    description='Configure new RPI host to comply with basic OS requirements')

parser.add_argument(
    '--ip',
    dest='ip',
    action='store',
    required=True,
    type=str,
    help='Node IP address'
)

parser.add_argument(
    '--hostname',
    dest='hostname',
    action='store',
    required=True,
    type=str,
    help='Node hostname'
)

parser.add_argument(
    '--username',
    dest='username',
    action='store',
    required=False,
    default="illia",
    type=str,
    help='Node username to create instead of default "pi" user'
)

parser.add_argument(
    '--github',
    dest='github',
    action='store',
    required=False,
    default="igrybkov",
    type=str,
    help='GitHub username to take SSH keys for access to this user account'
)

parser.add_argument(
    '--timezone',
    dest='timezone',
    action='store',
    required=False,
    default="America/Chicago",
    type=str,
    help='Node timezone'
)

parser.add_argument(
    '--locale',
    dest='locale',
    action='store',
    required=False,
    default="en_US.UTF-8",
    type=str,
    help='Node locale'
)

args = parser.parse_args()

params = {
    "target_ansible_host": args.ip,
    "target_ansible_user": "pi",
    "target_ansible_port": 22,
    "target_hostname": args.hostname,
    "target_timezone": args.timezone,
    "target_user": args.username,
    "github": args.github,
    "target_locale": args.locale,
}

paramsJson = json.dumps(params)

os.system("ssh-copy-id pi@'% s'" % args.ip)
os.system("ansible-playbook ansible/new_rpi.yml -v --extra-vars '% s'" % paramsJson)
