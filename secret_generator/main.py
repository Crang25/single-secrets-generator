from aiohttp import web

from settings import config
from secret_generator.store.database.accessor import PostgresAccessor


def setup_config(app: web.Application):
    app['config'] = config


def setup_accessor(app: web.Application):
    app['db'] = PostgresAccessor()
    app['db'].setup(app)


def setup_app(app: web.Application):
    setup_config(app)
    setup_accessor(app)


if __name__ == '__main__':
    app = web.Application()
    setup_app(app)
    web.run_app(
        app,
        host=app['config']['common']['host'],
        port=app['config']['common']['port'],
    )