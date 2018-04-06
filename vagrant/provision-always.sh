#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

pushd /vagrant
make serve
popd