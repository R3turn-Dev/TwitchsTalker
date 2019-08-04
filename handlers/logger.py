from CfTwMonitor.twitch import Handler
from CfTwMonitor.service import TwitchDownloader


class Logger(Handler):
    def __init__(self, parent: TwitchDownloader):
        self.parent = parent

    @Handler.listener()
    async def on_message(self, ctx):
        print(ctx)
