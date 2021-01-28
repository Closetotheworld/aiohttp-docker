from aiohttp import web

async def handler(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text = text)

if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get('/', handler), web.get('/{name}', handler)])
    web.run_app(app)

