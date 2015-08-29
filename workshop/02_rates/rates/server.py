import web
import urllib
import xml.etree.ElementTree as ET

urls = (
    '/rates/eur/(.*)', 'rates'
)

class rates:
    def GET(self, currency):
        req = urllib.urlopen("http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml")
        xmlRoot = ET.fromstring(req.read())
        query = ".//*[@currency='" + currency.upper() + "']"
        nodes = xmlRoot.findall(query)

        rate = nodes[0].get('rate') if (len(nodes) > 0) else 0
        return rate 


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

