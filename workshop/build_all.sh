#!/bin/bash
cd "$(dirname "$0")"

cd 04_ubuntu_python_web
docker build -t workshop/ubuntu_python_web .

cd ../02_rates
docker build -t workshop/rates .

cd ../03_portal
docker build -t workshop/portal .
