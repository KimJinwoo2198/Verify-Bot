import os
import time
import json
import discord
import asyncio
import requests
import multiprocessing
from urllib import request

from discord.ext import commands

from verify import LOGGER, TOKEN, EXTENSIONS, BOT_NAME_TAG_VER, CommandInt

async def status_task():
    while True:
        try:
            await bot.change_presence(
                activity = discord.Game (f"{len(bot.guilds)}개의 서버에서 놀고있어요!"),
                status = discord.Status.online,
            )
            await asyncio.sleep(10)
        except Exception:
            pass

class VerifyBot (commands.Bot) :
    def __init__ (self) :
        super().__init__ (
            command_prefix=CommandInt,
            intents=intents
        )
        self.remove_command("help")
        for i in EXTENSIONS :
            self.load_extension("verify.cogs." + i)

    async def on_ready (self) :
        LOGGER.info(BOT_NAME_TAG_VER)
        await self.change_presence(
            status = discord.Status.online,
        )
        bot.loop.create_task(status_task())

    async def on_message (self, message) :
        if message.author.bot:
            return
        await self.process_commands (message)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = VerifyBot ()
bot.run(TOKEN)