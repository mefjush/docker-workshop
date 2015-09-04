#!/bin/bash
URL="http://$RATES_PORT_8080_TCP_ADDR:$RATES_PORT_8080_TCP_PORT"
echo "Rates service url: ${URL}"
export RATES_URL="${URL}"

python -u server.py 8888 
