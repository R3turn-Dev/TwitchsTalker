from sanic import Blueprint
from sanic.response import json, html
from CfTwMonitor.service import SanicServer


class Introduce:
    def __init__(self, app: SanicServer, name="welcome", prefix="/"):
        self.app = app
        self.discord = self.app.monitor.discord
        self.name = name or self.__class__.__name__
        self.prefix = prefix

        self.bp = Blueprint(name=self.name, url_prefix=self.prefix)

        @self.bp.route("/", methods=["GET"])
        def root(req):
            return html(open("./templates/root/welcome.html", encoding="UTF-8").read().format(
                monitor=self.app.monitor,
                guild_count=len(self.discord.guilds),
                channel_count=len([*self.discord.get_all_channels()]),
                user_count=len(self.discord.users),
                guilds="\n".join([f"<li>{guild.name}</li>" for guild in self.discord.guilds])
            ))

        self.app.blueprint(self.bp)


def setup(app: SanicServer):
    Introduce(app)
