#!/bin/bash

cd ~/faucets
git stash push --include-untracked
git pull
chmod +x *.sh
