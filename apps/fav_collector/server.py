import web
import os
from os import listdir
from os.path import isfile, join
import urllib
import xml.etree.ElementTree as ET

rates_url = os.environ.get('RATES_URL', "http://localhost:8888")
static_dir = join(os.path.dirname(os.path.realpath(__file__)), "static")
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/submit', 'submit',
    '/eur/(.+)', 'currency'
)

class index:        
    def GET(self):
        files = [ f for f in listdir(static_dir) if isfile(join(static_dir, f)) ]
        return render.index(files)

class submit:
    def GET(self):
        url = web.input(url="").url
        url = url if ("http" in url) else ("http://" + url) 
        url = url if (url.endswith("/")) else (url + "/")
       
        filename = reduce(lambda url, s : url.replace(s, ""), ["http://", "https://", "www.", "/"], url)
        urllib.urlretrieve(url + "favicon.ico", join(static_dir, filename))
        raise web.redirect("/")

class currency:
    def GET(self, curr):
        currency = curr.upper()
        req = urllib.urlopen(rates_url)
        xmlRoot = ET.fromstring(req.read())
        query = ".//*[@currency='" + currency + "']"
        nodes = xmlRoot.findall(query)

        value = nodes[0].get('rate') if (len(nodes) > 0) else "unknown"
        return "EUR/" + currency + " = " + value 

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

