from aiohttp import web


class PostgresAccessor:

    def __init__(self):
        from secret_generator.secret.models import (
            Secret, SecretKey, SecretCode
        )

        self.secret = Secret
        self.secretKey = SecretKey
        self.secretCode = SecretCode

        self.db = None

    
    def setup(self, app: web.Application) -> None:
        app.on_startup.append(self._on_connect)
        app.on_cleanup.append(self._on_disconnect)

    
    async def _on_connect(self, app: web.Application):
        from secret_generator.store.database.models import db

        self.config = app['config']['postgres']
        await db.set_bind(self.config['database_url'])
        self.db = db

    
    async def _on_disconnect(self, _) -> None:
        if self.db is not None:
            await self.db.pop_bind().close()
