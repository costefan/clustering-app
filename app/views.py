from aiohttp import web


async def clusterize(request: web.Request) -> web.Response:

    return web.json_response(
        {'res': True},
        status=200
    )
