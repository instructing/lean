import discord
from discord.ext import commands
import asyncio
import random
import datetime
import os
import jishaku
import ok
import logging
from os import _exit
from time import sleep
import sys
import colorama
from colorama import Fore

if sys.platform == "win32":
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")

discord.gateway.DiscordWebSocket.identify = ok.get_mobile()

logging.basicConfig(level=logging.INFO, format= "%(asctime)s %(message)s", datefmt="%H:%M:%S")

intents = discord.Intents.all()

bot = commands.AutoShardedBot(
    help_command=None,
    shard_count=1,
    command_prefix=".",
    intents=intents,
    case_insensitive=True,
)

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

@bot.event
async def on_ready():
    clear()
    logging.info(f"{bot.user} is online")
    await bot.load_extension('jishaku')
    await bot.load_extension('cogs.events.on_message')
    await bot.load_extension('cogs.commands.about')
    await bot.load_extension('cogs.commands.role')
    

bot.run('Token Here')
