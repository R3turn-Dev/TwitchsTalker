from discord import Game
from discord.ext import tasks
from discord.ext.commands import command, group, Cog
from CfTwMonitor.service import DiscordClient


class Logger(Cog):
    def __init__(self, bot: DiscordClient):
        self.bot = bot
        self.logger = self.bot.monitor.logger

    def cog_unload(self):
        self.update_presence.cancel()


    @tasks.loop(seconds=5)
    async def update_presence(self):
        await self.bot.change_presence(
            activity=Game("{} Testers | {} Channels | {} Guilds".format(
                len(self.bot.users), len([*self.bot.get_all_channels()]), len(self.bot.guilds)
            ))
        )

    @Cog.listener()
    async def on_ready(self):
        self.logger.info("Discord Client Started with User {}(#{})".format(self.bot.user.name, self.bot.user.id))
        self.update_presence.start()


def setup(bot):
    bot.add_cog(Logger(bot))
