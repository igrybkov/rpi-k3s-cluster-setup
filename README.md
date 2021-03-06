# Setting up K3S cluster on Raspberry Pi

1. Download [etcher.io](https://etcher.io) for your OS
2. Flash an SD card using [Raspbian Lite](https://www.raspberrypi.org/software/operating-systems/)
3. Mount SD card to your Mac (simples way to do so is to re-inject it in card)
4. Run `./prepare-volume.py` to enable SSH
5. Eject the card
6. Boot Raspberry Pi
7. Find the RPi IP with `ping -c1 raspberrypi.local` or using your router interface
8. Configure RPi by running `./configure-rpi.py --hostname k3s-worker1 --ip 192.168.50.101`. When it will ask for password, use `raspberry`. Don't forget to replace hostname and IP with your values. For additional arguments, call the command with `--help` flag: `./configure-rpi.py --help`
9. Run `make-cluster.py` to setup cluster and workers: `./make-cluster.py --user illia --server 192.168.50.100 --worker 192.168.50.101 --worker 192.168.50.102 --worker 192.168.50.103`
10. Check your nodes: ```KUBECONFIG=`pwd`/kubeconfig kubectl get node -o wide```
10. (Optional) Copy cluster configuration: `cp ./kubeconfig ~/.kube/config`
