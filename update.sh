#!/bin/bash

cd ~/scripts/faucets
git stash push --include-untracked
git pull
chmod +x *.sh
