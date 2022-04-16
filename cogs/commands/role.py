import discord
from discord.ext import commands
import datetime

class role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(invoke_without_command=True, aliases=["r"])
    async def role(self, ctx):
        embed=discord.Embed(color=0x2f3136)

        embed.set_author(name="lean", icon_url="https://media.discordapp.net/attachments/957739904354377728/964007833748271174/Screenshot_2022-04-08_191516.png?width=674&height=676")
        embed.add_field(name="__Role__", value=f"**addrole:** (.r add @swift nameofrole)\n**removerole:** (.r remove @swift nameofrole)\n**createrole:** (.r create nameofrole)\n**deleterole:** (.r delete nameofrole)", inline=True)
        await ctx.send(embed=embed)

    @role.command()
    async def add(self, ctx, member: discord.Member, *, rolename: str = None):
        if not member and rolename is None:
            return await ctx.send('Please mention a user.')

        if rolename is not None:
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                return await ctx.send('That role does not exist.')
            try:
                await member.add_roles(role)
                embed = discord.Embed(title="__Role Add__", description=f"Added role **{role.name}** to **{member.display_name}**", color=0x2f3136, timestamp=datetime.datetime.utcnow())
                await ctx.send(embed=embed)
            except:
                await ctx.send("I don't have the perms to add that role.")

        else:
            return await ctx.send('Please mention the member and role to give them.')

    @role.command()
    async def remove(self, ctx, member: discord.Member, *, rolename: str):
        role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
        if not role:
            return await ctx.send('That role does not exist.')
        try:
            await member.remove_roles(role)
            embed = discord.Embed(title="__Role Remove__", description=f"Removed role **{role.name}** from **{member.display_name}**", color=0x2f3136, timestamp=datetime.datetime.utcnow())
            await ctx.send(embed=embed)
        except:
            await ctx.send("I don't have the perms to remove that role.")

    @role.command()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def create(self, ctx, role: str):
        await ctx.guild.create_role(name=role)
        embed = discord.Embed(title="__Role Create__", description=f"Role **{role}** has been **created**.", colour=0xffffff, timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=embed)

    @role.command()
    @commands.cooldown(1,3,commands.BucketType.user)
    async def delete(self, ctx, role: str):
        role = discord.utils.get(ctx.guild.roles, name=role)
        await role.delete()
        embed = discord.Embed(title="__Role Delete__", description=f"Role **{role}** has been **deleted**.", color=0xffffff, timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=embed)
    
async def setup(bot):
    await bot.add_cog(role(bot))