#!/bin/bash

folder=$(echo $(cd -- $(dirname -- "${BASH_SOURCE[0]}") && pwd) | awk -F/ '{print $NF}')

cd ~/scripts/$folder
apt install python3.10-venv
python3 -m venv venv
source venv/bin/activate
pip install -r dependencies
deactivate
