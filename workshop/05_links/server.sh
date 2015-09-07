#!/bin/bash

ADDRESS=$...
PORT=$...
URL="http://$ADDRESS:$PORT"

echo "Rates service url: ${URL}"
export RATES_URL="${URL}"

python -u server.py 8888 

