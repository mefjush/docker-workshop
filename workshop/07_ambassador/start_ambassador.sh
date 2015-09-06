#!/bin/bash
docker run -d --link rates:rates --expose 8080 --name rates_ambassador svendowideit/ambassador
