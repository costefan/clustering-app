from aiohttp import web

from .routes import app_routes


def setup_routes(app: web.Application):
    for route in app_routes:
        app.router.add_route(*route)


def create_app(loop):
    app = web.Application(middlewares=[web.normalize_path_middleware()])

    app.update(name='games_scrapper')
    app.on_startup.append(setup_routes)

    return app
