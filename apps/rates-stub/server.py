import web

urls = (
    '/', 'index'
)

rates = """<?xml version="1.0" encoding="UTF-8"?>
<gesmes:Envelope xmlns:gesmes="http://www.gesmes.org/xml/2002-08-01" xmlns="http://www.ecb.int/vocabulary/2002-08-01/eurofxref">
	<gesmes:subject>Reference rates</gesmes:subject>
	<gesmes:Sender>
		<gesmes:name>European Central Bank</gesmes:name>
	</gesmes:Sender>
	<Cube>
		<Cube time='2015-07-30'>
			<Cube currency='USD' rate='8.0955'/>
			<Cube currency='JPY' rate='136.25'/>
		</Cube>
	</Cube>
</gesmes:Envelope>"""

class index:        
    def GET(self):
        return rates

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

