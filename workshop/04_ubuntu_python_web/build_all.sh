#!/bin/bash
docker build -t workshop/ubuntu_python_web .

cd ../02_rates
docker build -t workshop/rates .

cd ../03_portal
docker build -t workshop/portal .
