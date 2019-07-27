from discord.ext.commands import Bot
from sanic import Sanic


class DiscordClient(Bot):
    def __init__(self, parent, token: str, prefix: str = ";"):
        self.monitor = parent

        self.token = token
        self.prefix = prefix

        super().__init__(prefix)

    def kick(self):
        self.monitor.loop.create_future(self.start())


class SanicServer(Sanic):
    def __init__(self, parent, host, port, debug):
        self.monitor = parent

        self._host = host
        self._port = port
        self._debug = debug

        super().__init__()

    def make_asyncio(self):
        return self.create_server(
            host=self._host,
            port=self._port,
            debug=self._debug,
            return_asyncio_server=True
        )
