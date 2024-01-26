#!/bin/bash

cd ~/faucets
apt install python3.10-venv
python3 -m venv venv
source venv/bin/activate
pip install -r dependencies
deactivate

read -p "Capsolver key?" key

echo "CAPSOLVER_KEY="$key > ~/faucets/config/env
