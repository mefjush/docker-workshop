import web

urls = (
    '/rates/eur/(.*)', 'index'
)

class index:        
    def GET(self, foo):
        return "1" 

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

