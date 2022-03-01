import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from verify.utils.get_chart import *
from verify import LOGGER, BOT_NAME_TAG_VER, color_code, DebugServer

class Chart (commands.Cog) :
    def __init__ (self, bot) :
        self.bot = bot

    @slash_command(description="Show Music Chart",guild_ids=DebugServer)
    async def chart(self, ctx, *, chart : Option(str, "Choose chart.", choices=["Melon", "Billboard"])):
        if not chart == None:
            chart = chart.upper()
        if chart == "MELON":
            title, artist = await get_melon()
            embed=discord.Embed(title="**멜론 차트**", color=color_code)
        elif chart == "BILLBOARD":
            title, artist = await get_billboard()
            embed=discord.Embed(title="**빌보드 차트**", color=color_code)
        for i in range(0, 10):
            embed.add_field(name=str(i+1) + ".", value = f"{artist[i]} - {title[i]}", inline=False)
        embed.set_footer(text=BOT_NAME_TAG_VER)
        await ctx.respond(embed=embed)

def setup (bot) :
    bot.add_cog (Chart (bot))
    LOGGER.info('Chart loaded!')