#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

# Install liquidsoap
/usr/local/bin/opam init --comp 4.05.0 -a
eval `opam config env`
opam install depext -y
opam depext taglib mad lame vorbis cry samplerate liquidsoap -y
opam install taglib mad lame vorbis cry samplerate liquidsoap liquidsoap-daemon -y


pip3 install --user pipenv

make install