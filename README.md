# Setting up K3S cluster on Raspberry Pi

1. Download [etcher.io](https://etcher.io) for your OS
2. Flash an SD card using [Raspbian Lite](https://www.raspberrypi.org/software/operating-systems/)
3. Mount SD card to your Mac (simples way to do so is to re-inject it in card)
4. Run `./prepare-volume.py` to enable SSH
5. Eject the card
6. Boot Raspberry Pi
7. Find the RPi IP with `ping -c raspberrypi.local` or using your router interface
8. Configure RPi by running `./configure-rpi.py --hostname k3s-1 --ip 192.168.1.35`. When it will ask for password, use `raspberry`. Don't forget to replace hostname and IP with your values. For additional arguments, call the command with `--help` flag: `./configure-rpi.py --help`
9. If you don't have [k3sup](https://github.com/alexellis/k3sup) on your laptop, get it by running `./get-k3sup.py`
10. For master node, run `k3sup install --k3s-extra-args '--no-deploy traefik' --user illia --ip 192.168.1.35`. Replace IP and user with your values
11. For worker nodes, run `k3sup join ' --user illia --server-ip 192.168.1.35 --ip 192.168.1.50`
12. Check your nodes: ```KUBECONFIG=`pwd`/kubeconfig kubectl get node -o wide```
