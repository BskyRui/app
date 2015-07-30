import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Hello, Rainbow~</h1>')

# 把一个generator标记为coroutine类型 协程(微线程)
@asyncio.coroutine
def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET', '/', index)
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8080)
	logging.info('server start at 127.0.0.0:8080')
	return srv

# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(init(loop))

loop.run_forever()

#loop.close()