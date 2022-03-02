import discord
from discord.ext import commands
from discord.commands import slash_command, Option, CommandPermission

from verify import LOGGER, BOT_NAME_TAG_VER, color_code, OWNERS, EXTENSIONS, DebugServer

class Help(commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @slash_command(description="Show Help Command", guild_ids=DebugServer)
    async def help(self, ctx, *, help_option : Option(str, "Choose help menu.", choices=["INFO", "GENERAL"])) :
        """ Send help """
        if not help_option == None:
            help_option = help_option.upper()
        if help_option == "GENERAL" or help_option == "일반":
            embed=discord.Embed(title="**기본적인 명령어**", description="", color=color_code)
            if "about" in EXTENSIONS:
                embed.add_field(name="`/about`",      value="저에 대한 정보를 알려드려요!", inline=True)
            if "other" in EXTENSIONS:
                embed.add_field(name="`/invite`",     value="저랑 다른 서버에서 놀고싶으세요? 당신이 서버의 관리자라면 저를 서버에 초대할 수 있어요!", inline=True)
                embed.add_field(name="`/version`",    value="관련 모듈 버전을 알려드려요!", inline=True)
            if "ping" in EXTENSIONS:
                embed.add_field(name="`/ping`",       value="핑 속도를 측정해요!", inline=True)
            embed.set_footer(text=BOT_NAME_TAG_VER)
            await ctx.respond(embed=embed)

            embed=discord.Embed(title="**도움말**", description="안녕하세요! 전 {bot_name} 에요! 아래에 있는 명령어들을 이용해 도움말을 보세요!".format(bot_name=self.bot.user.name), color=color_code)
            embed.add_field(name="`/help GENERAL`", value=">>> 기본적인 명령어들을 보내드려요!", inline=False)

            if ctx.author.id in OWNERS:
                embed.add_field(name="`/dev_help`", value=">>> 개발자님이 사용가능한 명령어들을 보내드려요!  ", inline=False)
            embed.set_footer(text=BOT_NAME_TAG_VER)
            await ctx.respond(embed=embed)

    @slash_command(description="개발자명령어", permissions=[CommandPermission("owner", 2, True)], guilds_id=DebugServer)
    async def dev_help(self, ctx):
        embed=discord.Embed(title="**개발자 명령어**", description="명령어 뒷쪽의 모든 괄호는 빼주세요!", color=color_code)
        embed.add_field(name="`/serverlist`",   value=">>> 제가 들어가 있는 모든 서버 리스트를 출력해요!", inline=False)
        embed.add_field(name="`/module_list`",      value=">>> 모든 모듈의 이름을 알려줘요!", inline=False)
        embed.add_field(name="`/load` [*모듈명*]",         value=">>> 모듈을 로드해요!", inline=False)
        embed.add_field(name="`/unload` [*모듈명*]",       value=">>> 모듈을 언로드해요!", inline=False)
        embed.add_field(name="`/reload` [*모듈명*]",       value=">>> 모듈을 리로드해요!", inline=False)
        embed.add_field(name="`/serverinfo`",   value=">>> 봇 서버의 사양을 알려줘요!", inline=False)
        embed.add_field(name="`/broadcast` [*공지 내용*]",    value=">>> 공지를 모든 서버에 전송해요!", inline=False)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    LOGGER.info('Help loaded!')