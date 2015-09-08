### Dependencies 
# apt-get update 
# DEBIAN_FRONTEND=noninteractive apt-get -y install python python-setuptools
# easy_install web.py

### Running
python -u server.py 8888

### Access
A web-app is running on port 8888

### You can modify 'rates' microservice url with 'RATES_URL' env variable
export RATES_URL=http://www.xyz.eu:1234
