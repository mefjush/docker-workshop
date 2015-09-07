#!/bin/bash

ADDRESS=$RATES_PORT_8080_TCP_ADDR
PORT=$RATES_PORT_8080_TCP_PORT
URL="http://$ADDRESS:$PORT"

echo "Rates service url: ${URL}"
export RATES_URL="${URL}"

python -u server.py 8888 

