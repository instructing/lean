import discord, logging, datetime, datetime, asyncio
import colorama
from colorama import Fore, init
from discord.ext import commands

class termlogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        logging.info(f"{message.content}")


async def setup(bot):
    await bot.add_cog(termlogs(bot))