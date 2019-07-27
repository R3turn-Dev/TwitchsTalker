import sys
import logging
import importlib
from typing import List
from discord.ext.commands import Bot
from sanic import Sanic
from traceback import format_exc


class DiscordClient(Bot):
    def __init__(self, parent, token: str, prefix: str = ";"):
        self.monitor = parent
        self.logger = self.monitor.logger

        self.token = token
        self.prefix = prefix

        super().__init__(prefix, help_command=None)

    def kick(self):
        self.monitor.loop.create_future(self.start())


class SanicServer(Sanic):
    def __init__(self, parent, host, port, debug):
        self.monitor = parent
        self.logger = self.monitor.logger

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

    def load_routes(self, blueprints: List[str]):
        for bp in blueprints:
            try:
                lib = importlib.import_module(bp)
                if not hasattr(lib, 'setup'):
                    del lib
                    del sys.modules[bp]

                    raise Exception("This route has not to setup.")

                lib.setup(self)
            except:
                self.logger.error("Error on load route `{}` due to \n{}".format(bp, format_exc()))
