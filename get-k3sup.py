#!/usr/bin/env python3

import os

os.system("curl -sLS https://get.k3sup.dev | sh")
if (os.path.isfile(os.path.join('./', 'k3sup'))):
    os.system("sudo install k3sup /usr/local/bin/")
