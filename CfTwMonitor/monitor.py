import logging
import asyncio
from .service import DiscordClient, SanicServer


class Monitor:
    """Integrated Object to run multiple sub-modules"""
    def __init__(self, token: str, prefix: str = ";", host: str="127.0.0.1", port: int=88, debug =False, loop=None):
        """

        Parameters
        ----------
        token
            Token of Discord Bot Client
        prefix
            Command Prefix of Discord Bot Client
        host
            Hostname of Sanic Server
        port
            Port of Sanic Server
        debug
            Debug mode of Sanic Server
        loop
            Custom Event loop
        """
        self.loop = loop or self._loop()
        self.debug = debug

        # Discord Attributes
        self.discord_token = token
        self.discord_prefix = prefix
        self.discord = None

        # Sanic Attributes
        self.sanic_host = host
        self.sanic_port = port
        self.sanic = None

        self.logger.debug(f"{self} has been initialized.")

    def _loop(self):
        return asyncio.get_event_loop()

    @property
    def logger(self):
        return logging.getLogger(self.__class__.__module__ + "." + self.__class__.__name__)

    def setup(self):
        self.discord = DiscordClient(self, self.discord_token, self.discord_prefix)
        self.sanic = SanicServer(self, self.sanic_host, self.sanic_port, debug=self.debug)

    def run(self):
        asyncio.ensure_future(self.sanic.make_asyncio(), loop=self.loop)
        asyncio.ensure_future(self.discord.start(self.discord_token), loop=self.loop)
        self.loop.run_forever()
