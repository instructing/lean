from ast import alias
import discord, logging, datetime, asyncio, psutil
from datetime import datetime
from discord.ext import commands


class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["botinfo", "information", "a"])
    async def about(self, ctx):
        total_Ram = round(round(psutil.virtual_memory().total) / 102400000) / 10
        used_MemoryGB = round(round(psutil.virtual_memory().used) / 102400000) / 10
        CPU_Usage = round(psutil.cpu_percent(), 1)
        embed=discord.Embed(color=0x2f3136)
        embed.add_field(name="__Bot__", value=f"**users:** {sum(g.member_count for g in self.bot.guilds)}\n**guilds:** {len(self.bot.guilds)}\n**cmds:** {len(self.bot.commands)}\n**shard:** {self.bot.shard_count}\n**prefix:** .", inline=True)
        embed.add_field(name="__Network__", value=f"**ram:** {total_Ram}\n**mem:** {used_MemoryGB}\n**cpu:** {CPU_Usage}\n**latency:** {round(self.bot.latency * 500)}ms", inline=True)
        embed.add_field(name="__Information__", value=f"**dev:** swift#4851\n**ver:** beta", inline=True)
        embed.set_author(name="lean", icon_url="https://media.discordapp.net/attachments/957739904354377728/964007833748271174/Screenshot_2022-04-08_191516.png?width=674&height=676")
        # embed.set_thumbnail(url="https://media.discordapp.net/attachments/957739904354377728/964007833748271174/Screenshot_2022-04-08_191516.png?width=674&height=676")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(about(bot))