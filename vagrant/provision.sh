#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

apt-get install software-properties-common
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get clean
apt-get -y autoremove

apt-get -y install python3.6 m4 unzip build-essential aspcud mercurial git darcs
wget https://raw.github.com/ocaml/opam/master/shell/opam_installer.sh -O - | sh -s /usr/local/bin

wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py
python3 /tmp/get-pip.py