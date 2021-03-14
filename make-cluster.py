#!/usr/bin/env python3

import argparse
import os
import glob
import sys
import json

parser = argparse.ArgumentParser(
    description='Make k3s cluster')

parser.add_argument(
    '-s',
    '--server',
    dest='server',
    action='store',
    required=True,
    type=str,
    help='Server IP address'
)

parser.add_argument(
    '-w',
    '--worker',
    dest='workers',
    action='append',
    required=True,
    type=str,
    help='Worker IP address'
)

parser.add_argument(
    '-u',
    '--user',
    dest='user',
    action='store',
    required=False,
    default="illia",
    type=str,
    help='Username'
)

args = parser.parse_args()

user = args.user
server = args.server
workers = args.workers

print('Installing/updating k3sup')

os.system("curl -sLS https://get.k3sup.dev | sh")
if (os.path.isfile(os.path.join('./', 'k3sup'))):
    os.system("sudo install k3sup /usr/local/bin/")

print("")
print("Install k3s server")
os.system("k3sup install --k3s-extra-args '--no-deploy traefik --no-deploy servicelb --disable-cloud-controller' --user % s --ip % s" %
          (user, server))

for worker in workers:
    print("")
    print("Install k3s worker for % s" % worker)
    os.system("k3sup join --user % s --server-ip % s --ip % s" %
              (user, server, worker))
