### Apps
# portal     - main app       - offers 2 'exciting' features: favicon collecting and currency conversion
# rates      - currency rates - provides the rates fetched from ecb
# rates-stub - stub for rates - provides hardcoded set of rates

### Dependencies 
# python 2
# web.py (easy_install web.py)

### Running
cd portal
python server.py

cd rates-stub
python server.py 8888

#or

cd rates
python server.py 8888
