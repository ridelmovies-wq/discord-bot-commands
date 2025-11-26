import discord
from discord.ext import commands
import time

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', help='Show help command')
    async def help(self, ctx):
        embed = discord.Embed(title='Bot Commands', color=discord.Color.blue())
        embed.add_field(name='Moderation', value='!kick !ban !mute !clear !lock', inline=False)
        embed.add_field(name='Fun', value='!meme !joke !roll !coinflip', inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='userinfo', help='Get user information')
    async def userinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        embed = discord.Embed(title=f'{member.name}', color=discord.Color.green())
        embed.add_field(name='ID', value=member.id)
        embed.add_field(name='Joined', value=member.joined_at)
        embed.add_field(name='Roles', value=len(member.roles))
        await ctx.send(embed=embed)

    @commands.command(name='serverinfo', help='Get server information')
    async def serverinfo(self, ctx):
        embed = discord.Embed(title=ctx.guild.name, color=discord.Color.purple())
        embed.add_field(name='Members', value=ctx.guild.member_count)
        embed.add_field(name='Channels', value=len(ctx.guild.channels))
        embed.add_field(name='Owner', value=ctx.guild.owner)
        embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else '')
        await ctx.send(embed=embed)

    @commands.command(name='avatar', help='Get user avatar')
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        embed = discord.Embed(title=f'{member.name} Avatar', color=discord.Color.random())
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name='invite', help='Get bot invite link')
    async def invite(self, ctx):
        invite = discord.utils.oauth_url(self.bot.user.id, permissions=discord.Permissions(administrator=True))
        await ctx.send(f'[Invite Bot]({invite})')

    @commands.command(name='latency', help='Check bot latency')
    async def latency(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command(name='uptime', help='Check bot uptime')
    async def uptime(self, ctx):
        await ctx.send(f'Bot is online!')

    @commands.command(name='membercount', help='Get member count')
    async def membercount(self, ctx):
        embed = discord.Embed(title=f'{ctx.guild.name} Members', color=discord.Color.gold())
        embed.add_field(name='Total', value=ctx.guild.member_count)
        embed.add_field(name='Humans', value=sum(1 for m in ctx.guild.members if not m.bot))
        embed.add_field(name='Bots', value=sum(1 for m in ctx.guild.members if m.bot))
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
