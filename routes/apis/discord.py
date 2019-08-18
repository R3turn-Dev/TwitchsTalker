from sanic import Blueprint
from sanic.response import json
from json import dumps
from discord import Guild
from CfTwMonitor.service import SanicServer


class DiscordIntegration(Blueprint):
    def __init__(self, app: SanicServer, name="discord", prefix="/discord"):
        self.app = app
        self.discord = self.app.monitor.discord
        self.name = name or self.__class__.__name__
        self.prefix = prefix

        super().__init__(name=self.name, url_prefix=self.prefix)

        @self.route("/guild", methods=["GET"])
        def guilds(req):
            return json({
                "code": 200,
                "guilds": [{
                    "name": x.name,
                    "id": x.id,
                    "description": x.description
                } for x in self.discord.guilds]
            })

        @self.route("/guild/<id:int>", methods=["GET"])
        def get_guild(req, id: int):
            guild = None

            for g in self.discord.guilds:
                if g.id == id:
                    return json({
                        "status": 200,
                        "data": dumps(guild)
                    })

            return json({
                "status": 404,
                "message": f"Guild {id} not found"
            })
