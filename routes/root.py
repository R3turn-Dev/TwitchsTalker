from sanic import Blueprint
from sanic.response import json, html
from CfTwMonitor.service import SanicServer


class Introduce:
    def __init__(self, app: SanicServer, name="welcome", prefix="/"):
        self.app = app
        self.name = name or self.__class__.__name__
        self.prefix = prefix

        self.bp = Blueprint(name=self.name, url_prefix=self.prefix)

        @self.bp.route("/", methods=["GET"])
        def root(req):
            return html("""안녕하세요, 디스코드 봇 + Sanic 서버입니다!""")

        self.app.blueprint(self.bp)


def setup(app: SanicServer):
    Introduce(app)
