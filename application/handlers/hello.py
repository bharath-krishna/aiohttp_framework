import aiohttp
import logging
from aiohttp import web


app = web.Application()
root_path = '/hello'

class HelloHandler(web.View):
    async def get(self):
        ret = {"greet": "hello", "message": "welcome..!"}
        logging.info("accessed hello endpoint")
        
        return web.json_response(ret)

app.router.add_get('', HelloHandler)
