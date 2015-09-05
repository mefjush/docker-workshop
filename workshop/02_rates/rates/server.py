import web
import urllib
import logging
import time
import os
import xml.etree.ElementTree as ET

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(level=logging.INFO)

handler = logging.FileHandler('logs/rates.log')
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

logger = logging.getLogger('rates')
logger.addHandler(handler)

urls = (
    '/rates/eur/(.*)', 'rates'
)

class rates:
    def GET(self, currency):
        start = time.time()

        currency = currency.upper()
        req = urllib.urlopen("http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml")
        xmlRoot = ET.fromstring(req.read())
        query = ".//*[@currency='" + currency + "']"
        nodes = xmlRoot.findall(query)

        rate = nodes[0].get('rate') if (len(nodes) > 0) else 0

        millis = (time.time() - start) * 1000
        logger.info('currency: ' +  currency + ' - rate: ' + str(rate)  + ' - millis: ' + str(millis))

        return rate 


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

