#!/bin/bash 

currencies=("chf" "jpy" "jpy" "jpy" "usd" "usd" "usd" "usd" "usd") 

while [ 1 ]
do
    rnd=$(shuf -i 0-8 -n 1)
    curr=${currencies[$rnd]}
    curl http://localhost:9000/rates/eur/$curr
    echo " $curr"
    sleep 5
done
:
