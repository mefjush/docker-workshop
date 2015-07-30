import web
import urllib

urls = (
    '/', 'index'
)

class index:        
    def GET(self):
        req = urllib.urlopen("http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml")
        return req.read()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

