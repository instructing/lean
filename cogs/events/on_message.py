import discord, logging, datetime, datetime, asyncio
import colorama
from colorama import Fore, init
from discord.ext import commands

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX


class termlogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        logging.info(f"{message.content}")


async def setup(bot):
    await bot.add_cog(termlogs(bot))