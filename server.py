import asyncio
import random
from aiohttp import web


async def websocket_handler(request, event_name):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    try:
        while True:
            data = random.uniform(0, 100)
            await ws.send_str(f'{data:.2f}')
            await asyncio.sleep(0.25)
    except asyncio.CancelledError:
        await ws.close()

    return ws


async def pressure_handler(request):
    return await websocket_handler(request, 'Pressure')


async def temperature_handler(request):
    return await websocket_handler(request, 'Temperature')


async def flow_handler(request):
    return await websocket_handler(request, 'Flow')


async def index(request):
    return web.FileResponse('brewery.html')


app = web.Application()
app.add_routes(
    [
        web.get('/', index),
        web.get('/ws/pressure', pressure_handler),
        web.get('/ws/temperature', temperature_handler),
        web.get('/ws/flow', flow_handler),
    ]
)

if __name__ == '__main__':
    try:
        web.run_app(app, port=8080)
    except Exception as e:
        print(f'Failed to start server: {e}')
