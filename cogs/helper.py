from discord.ext import commands
from discord.ext.commands import command


class DiscordHelp(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @command(alias=["도움", "도움말"])
    async def help(self, ctx):
        await ctx.send(
            ctx.author.mention + """ 안녕하세요! 이 봇은 __**Discord + Web**__ 테스트 중입니다.
모든 코드는 깃허브 레포지토리에 공개되어 있습니다.
문의가 필요하시면 아래 연락처로 연락바랍니다.

__**Github**__: <https://github.com/R3turn-Dev/TwitchsTalker>
__**Web**__: http://bot.return0927.xyz/
__**Admin**__: 이은학#9999 / invoice@return0927.xyz"""
        )


def setup(bot):
    bot.add_cog(DiscordHelp(bot))
