import aiohttp
from aiohttp import web
import asyncio

async def handle(request):
    data = await request.json()
    return web.json_response({"data": data['num'], "result": count})

async def update():
    global count
    while True:
        await asyncio.sleep(0.01)
        count += 1

if __name__ == '__main__':
    count = 0
    main_loop = asyncio.new_event_loop()
    
    task = main_loop.create_task(update())
    asyncio.gather(task)

    app = web.Application()
    app.router.add_get('/', handle)
    web.run_app(app=app, host="127.0.0.1", port=8081, loop=main_loop)