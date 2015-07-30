import web
import os
from os import listdir
from os.path import isfile, join
import urllib
import xml.etree.ElementTree as ET

dir = os.path.dirname(os.path.realpath(__file__))
static_dir = dir + "/static"

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/submit', 'submit',
    '/eur/(.+)', 'currency'
)

class index:        
    def GET(self):
        onlyfiles = [ f for f in listdir(static_dir) if isfile(join(static_dir,f)) ]
        return render.index(onlyfiles)

class submit:
    def GET(self):
        data = web.input(url="")
        url = data.url
        if ("http" not in url):
            url = "http://" + url

        if (not(url.endswith("/"))):
            url = url + "/"
        
        filename = url.replace("http://", "").replace("https://", "").replace("www.", "").replace("/", "") + ".ico"

        urllib.urlretrieve(url + "favicon.ico", static_dir + "/" + filename)

        raise web.redirect("/")

class currency:
    def GET(self, curr):
        curr = curr.upper()
        req = urllib.urlopen("http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml")
        root = ET.fromstring(req.read())
        query = ".//*[@currency='" + curr + "']"

        nodes = root.findall(query)

        if (len(nodes) > 0):
            return "EUR/" + curr + " = " + nodes[0].get('rate')
        else:
            return "Error"        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

