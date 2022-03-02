import discord
import platform
import psutil
import math

from discord.ext import commands
from discord.commands import CommandPermission, slash_command

from verify import LOGGER, color_code, BOT_NAME_TAG_VER, EXTENSIONS, DebugServer

class Owners(commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot
        self._last_members = None
        self.color = color_code
        self.error_color = 0xff4a4a

    @slash_command(description="Load Module",permissions=[CommandPermission("owner", 2, True)], guild_ids=DebugServer)
    async def load(self, ctx, module) :
        try:
            self.bot.load_extension("verify.cogs." + module)
            LOGGER.info(f"로드 성공!\n모듈 : {module}")
            embed = discord.Embed (
                title = "로드 성공!",
                description = "모듈 : {module}".format(module=module),
                color = self.color
            )
            if f"*~~{module}~~*" in EXTENSIONS:
                EXTENSIONS[EXTENSIONS.index(f"*~~{module}~~*")] = module
            else:
                EXTENSIONS.append(module)
        except Exception as error :
            LOGGER.error(f"로드 실패!\n에러 : {error}")
            embed = discord.Embed (
                title = "로드 실패!",
                description = "에러 : {error}".format(error=error),
                color = self.error_color
            )
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed = embed)

    @slash_command(description="Reload Module",permissions=[CommandPermission("owner", 2, True)], guild_ids=DebugServer)
    async def reload(self, ctx, module) :
        try :
            self.bot.reload_extension("verify.cogs." + module)
            LOGGER.info(f"리로드 성공!\n모듈 : {module}")
            embed = discord.Embed (
                title = "리로드 성공!",
                description = "모듈 : {module}".format(module=module),
                color = self.color
            )
        except Exception as error :
            LOGGER.error(f"리로드 실패!\n에러 : {error}")
            embed = discord.Embed (
                title = "리로드 실패!",
                description = f'에러 : {error}',
                color = self.error_color
            )
            if module in EXTENSIONS:
                EXTENSIONS[EXTENSIONS.index(module)] = f"*~~{module}~~*"
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed = embed)

    @slash_command(description="Unload Module",permissions=[CommandPermission("owner", 2, True)], guild_ids=DebugServer)
    async def unload(self, ctx, module) :
        try :
            self.bot.unload_extension("verify.cogs." + module)
            LOGGER.info(f"언로드 성공!\n모듈 : {module}")
            embed = discord.Embed (
                title = "언로드 성공!",
                description = "모듈 : {module}".format(module=module),
                color = self.color
            )
            if module in EXTENSIONS:
                EXTENSIONS[EXTENSIONS.index(module)] = f"*~~{module}~~*"
        except Exception as error :
            LOGGER.error(f"언로드 실패!\n에러 : {error}")
            embed = discord.Embed (
                title = "언로드 실패!",
                description = f'에러 : {error}',
                color = self.error_color
            )
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed = embed)

    @slash_command(description="List for Module",permissions=[CommandPermission("owner", 2, True)], guild_ids=DebugServer)
    async def module_list(self, ctx):
        modulenum = 0
        for m in EXTENSIONS:
            if not m[0:3] == "*~~":
                modulenum += 1
        modulenum = '{modulenum}개의 모듈들이 로드되어 있습니다.'.format(modulenum=modulenum)
        e1 = "\n".join(EXTENSIONS)
        embed=discord.Embed(title='**모듈 리스트**', color=color_code)
        embed.add_field(name=modulenum, value=e1, inline=False)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed=embed)

    @slash_command(description="Show serverinfo",permissions=[CommandPermission("owner", 2, True)], guild_ids=DebugServer)
    async def serverinfo(self, ctx) :
        embed=discord.Embed(title='owners_server_info', color=color_code)
        embed.add_field(name="Platform", value=platform.platform(), inline=False)
        embed.add_field(name="Kernel", value=platform.version(), inline=False)
        embed.add_field(name="Architecture", value=platform.machine(), inline=False)
        embed.add_field(name="CPU Usage", value=str(psutil.cpu_percent()) +"%", inline=False)
        memorystr = str(round((psutil.virtual_memory().used / (1024.0 ** 3)), 1)) + "GB" + " / " + str(round((psutil.virtual_memory().total / (1024.0 ** 3)), 1)) + "GB"
        embed.add_field(name="Memory Usage", value=memorystr, inline=False)
        embed.add_field(name="Python Ver", value=("%s %s") %(platform.python_implementation(), platform.python_version()), inline=False)
        embed.add_field(name="Py-cord.py Ver", value=discord.__version__, inline=False)
        embed.add_field(name="Ping", value=str(round(self.bot.latency * 1000)) + "ms", inline=False)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed=embed)
    
    @slash_command(description="Show serverlist",permissions=[CommandPermission("owner", 2, True)], guild_ids=DebugServer)
    async def server_list(self, ctx) :
        page = 10
        if len(self.bot.guilds) <= page:
            embed = discord.Embed(title = "{BOT_NAME} (이)가 들어가 있는 서버목록\n".format(BOT_NAME=self.bot.user.name), description="**{server_count}개**의 서버, **{members_count}명**의 유저".format(server_count=len(self.bot.guilds), members_count=len(self.bot.users)), color=color_code)
            srvr = str()
            for i in self.bot.guilds:
                srvr = srvr + "**{server_name}** - **{server_members_count}명** **{server_id}\n".format(server_name=i, server_members_count=i.member_count, server_id=i.id)
            embed.add_field(name="​", value=srvr, inline=False)
            embed.set_footer(text=BOT_NAME_TAG_VER)
            return await ctx.respond(embed = embed)
        botguild = self.bot.guilds
        allpage = math.ceil(len(botguild) / page)

        pages_list = []
        for i in range(1, allpage+1):
            srvr = ""
            numb = (page * i)
            numa = numb - page
            for a in range(numa, numb):
                try:
                    srvr = srvr + "**{server_name}** - **{server_members_count}명** 서버 아이디 :**{server_id}**\n".format(server_name=botguild[a], server_members_count=botguild[a].member_count)
                except IndexError:
                    break

            pages_list.append(
                [
                    discord.Embed(title = "**{server_name}** - **{server_members_count}명** 서버 아이디 :**{server_id}\n".format(BOT_NAME=self.bot.user.name), description="owners_server_list_description2".format(server_count=len(self.bot.guilds), members_count=len(self.bot.users), servers=srvr), color=color_code).set_footer(text=f"{'owners_page'} {str(i)}/{str(allpage)}\n{BOT_NAME_TAG_VER}")
                ]
            )
        paginator = pages.Paginator(pages=pages_list)
        await paginator.respond(ctx.interaction, ephemeral=False)

    @slash_command(description="Send Embed",permissions=[CommandPermission("owner", 2, True)], guild_ids=DebugServer)
    async def embed(self, ctx, embed):
        e = discord.Embed(description=embed,color=color_code)
        await ctx.respond(embed=e)

def setup (bot) :
    bot.add_cog(Owners(bot))
    LOGGER.info('Owners Loaded!')