from sanic import Blueprint
from sanic.response import json
from CfTwMonitor.service import SanicServer


class ApiV1:
    def __init__(self, app: SanicServer, name="v1", prefix="/api"):
        self.app = app
        self.discord = self.app.monitor.discord
        self.name = name or self.__class__.__name__
        self.prefix = prefix

        self.bp = Blueprint(name=self.name, url_prefix=self.prefix)

        @self.bp.route("/ping", methods=["GET"])
        def ping(req):
            return json({"code": 200, "message": "I give pong for you!"})

        self.app.blueprint(self.bp)


def setup(app: SanicServer):
    ApiV1(app)
