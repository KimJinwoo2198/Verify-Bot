import discord
from discord.ext import commands
from discord.commands import slash_command

from verify import LOGGER, BOT_NAME_TAG_VER, color_code, AboutBot, DebugServer

class About (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @slash_command(description="저에 대한 정보를 알려드려요!", guild_ids=DebugServer)
    async def about(self, ctx) :
        e=discord.Embed(title="**봇에 대한 정보**", description=AboutBot, color=color_code)
        e.add_field(name="서버 수", value=len(self.bot.guilds), inline=True)
        e.add_field(name="유저 수", value=len(self.bot.users), inline=True)
        e.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed=e)

def setup (bot) :
    bot.add_cog (About (bot))
    LOGGER.info('About loaded!')