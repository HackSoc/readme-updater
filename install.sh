#!/usr/bin/env bash

set -e

mkdir -p "/srv/http/"
cd /srv/http/
git clone https://github.com/HackSoc/readme-updater $(hostname)
cd $(hostname)
sudo python conf.py