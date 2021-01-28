import aiohttp, asyncio

async def req():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8080/wonryang') as response:
            print("Status: ", response.status)
            print("C-type: ", response.headers['content-type'])
            html = await response.text()
            print("Body:", html)

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(req())
