import web
import os
import urllib
import uuid

RATES_ADDRESS = os.environ.get("SOME_ADDRESS_FROM_SYS_ENV", "localhost")
RATES_PORT = os.environ.get("SOME_PORT_FROM_SYS_ENV", "8080")

rates_url = "http://" + RATES_ADDRESS + ":" + RATES_PORT
print "Rates url: " + rates_url

static_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/favicons', 'favicons',
    '/collect', 'collect',
    '/convert', 'convert'
)

class index:        
    def GET(self):
        return render.index(str(uuid.uuid1()))

class favicons:
    def GET(self):
        files = [ f for f in os.listdir(static_dir) if os.path.isfile(os.path.join(static_dir, f)) ]
        return render.favicons(files)

class collect:
    def GET(self):
        url = web.input(url="").url
        url = url if ("http" in url) else ("http://" + url) 
        url = url if (url.endswith("/")) else (url + "/")
       
        filename = reduce(lambda url, s : url.replace(s, ""), ["http://", "https://", "www.", "/"], url)
        urllib.urlretrieve(url + "favicon.ico", os.path.join(static_dir, filename))
        raise web.redirect("/favicons")

class convert:
    def GET(self):
        data = web.input(currency="USD", amount="1")
        currency = data.currency.lower()
        amount = data.amount

        req = urllib.urlopen(rates_url + "/rates/eur/" + currency)

        rate = req.read() 
        converted = str(float(amount) * float(rate))
        return amount + " EUR = " + converted + " " + currency.upper()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

