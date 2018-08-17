#!/usr/bin/env bash

set -e

sudo mkdir -p "/srv/http/"
cd /srv/http/
sudo git clone https://github.com/HackSoc/readme-updater $(hostname)
cd $(hostname)
sudo python conf.py