import sys
import logging
import importlib
from typing import List
from discord.ext.commands import Bot
from sanic import Sanic
from traceback import format_exc
from datetime import datetime


class DiscordClient(Bot):
    """Discord Bot Client for integrated Monitor management"""
    def __init__(self, parent, token: str, prefix: str = ";"):
        """

        Parameters
        ----------
        parent: :class:`CfTwMonitor.Monitor`
            Parent Monitor class to register
        token: str
            Token of Discord Bot
        prefix: str
            Command Prefix of Discord Bot
        """
        self.monitor = parent
        self.logger = self.monitor.logger

        self.token = token
        self.prefix = prefix

        super().__init__(prefix, help_command=None)

    def kick(self):
        """
        Register awaitable starting function onto the main event loop
        """
        self.monitor.loop.create_future(self.start())


class SanicServer(Sanic):
    """Sanic Server for integrated Monitor management"""
    def __init__(self, parent, host, port, debug=False):
        """

        Parameters
        ----------
        parent: :class:`CfTwMonitor.Monitor`
            Parent Monitor class to register
        host
            Hostname of Sanic server
        port
            Port of Sanic server
        debug
            Debug mode of Sanic server
        """
        self.monitor = parent
        self.logger = self.monitor.logger

        self._host = host
        self._port = port
        self._debug = debug

        super().__init__()

    def make_asyncio(self):
        """
        Make an awaitable starting function

        Returns
        -------
        awaitable
            starting function
        """
        return self.create_server(
            host=self._host,
            port=self._port,
            debug=self._debug,
            return_asyncio_server=True
        )

    def load_routes(self, blueprints: List[str]):
        """

        Parameters
        ----------
        blueprints: List[str]
            List of Path to each blueprint to register

        """
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


class TwitchDownloader:
    def __init__(
            self,
            channels: List[str],
            ):
        self.channels = dict((k, None) for k in channels)

        self.extensions = []
        self.listeners = []

    @property
    def logger(self):
        return logging.getLogger(self.__class__.__module__ + "." + self.__class__.__name__)

    def load_extension(self, name):
        try:
            lib = importlib.import_module(name)
            if not hasattr(lib, 'setup'):
                del lib
                del sys.modules[name]

                raise Exception("This route has not to setup.")

            lib.setup(self)
        except:
            self.logger.error("Error on load route `{}` due to \n{}".format(name, format_exc()))


class TwitchIRCClient:
    def __init__(
            self,
            parent,
            channels: List[str],
            nick: str,
            token: str,
            host: str = "irc.twitch.tv",
            port: int = 6667,
            ):

        self.monitor = parent
        self.channels = dict((c, {}) for c in channels)
        self.nick = nick
        self.token = token
        self.host = host
        self.port = port

    @property
    def logger(self):
        return self.monitor.logger

    def load_extension(self, name):
        try:
            lib = importlib.import_module(name)
            if not hasattr(lib, 'setup'):
                del lib
                del sys.modules[name]

                raise Exception("This route has not to setup.")

            lib.setup(self)
        except:
            self.logger.error("Error on load route `{}` due to \n{}".format(name, format_exc()))
