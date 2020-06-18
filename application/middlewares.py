from aiohttp.web import middleware

@middleware
async def request_middlware(request, handler):
    resp = await handler(request)
    return resp