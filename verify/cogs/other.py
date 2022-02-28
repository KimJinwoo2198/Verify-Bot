import discord
from discord.ext import commands
import platform
import subprocess
from discord.commands import slash_command

from verify import LOGGER, BOT_NAME_TAG_VER, DebugServer, color_code

class Other (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @slash_command(description="Invite Bot Your Server", guild_ids=DebugServer)
    async def invite(self, ctx):
        link = f'https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=414501391424&scope=bot%20applications.commands'
        embed=discord.Embed(title="**절 당신이 관리하는 서버에 초대해주시다니!**", description="정말 감사합니다! [여기](<{link}>)를 눌러 서버에 초대해주세요!".format(link=link), color=color_code)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed=embed)

    @slash_command(description="Software Version", guild_ids=DebugServer)
    async def softver(self, ctx) :
        javaver = subprocess.check_output("java --version", shell=True, encoding='utf-8')
        lavalinkver = subprocess.check_output("java -jar Lavalink.jar --version", shell=True, encoding='utf-8')
        embed=discord.Embed(title="**관련 모듈 버전**", color=color_code)
        embed.add_field(name="Python Ver", value=("%s %s") %(platform.python_implementation(), platform.python_version()), inline=False)
        embed.add_field(name="Py-Cord.py Ver", value=discord.__version__, inline=False)
        embed.add_field(name="Lavalink.py Ver", value=lavalink.__version__, inline=False)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed=embed)

def setup (bot) :
    bot.add_cog (Other (bot))
    LOGGER.info('Other loaded!')