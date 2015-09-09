#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage $0 YOUR_NAME"
    exit 1
fi

HOSTNAME=$(hostname)
echo "Hello $1, I'm $HOSTNAME!"
