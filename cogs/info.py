import discord
from discord.ext import commands
import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='about', help='About the bot')
    async def about(self, ctx):
        embed = discord.Embed(title='About Bot', description='Advanced Discord Bot with 50+ commands', color=discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.command(name='version', help='Get bot version')
    async def version(self, ctx):
        await ctx.send('Version 1.0.0')

    @commands.command(name='credits', help='Show credits')
    async def credits(self, ctx):
        embed = discord.Embed(title='Credits', description='Made with Discord.py', color=discord.Color.magenta())
        await ctx.send(embed=embed)

    @commands.command(name='roleinfo', help='Get role information')
    async def roleinfo(self, ctx, *, role: discord.Role):
        embed = discord.Embed(title=role.name, color=role.color)
        embed.add_field(name='ID', value=role.id)
        embed.add_field(name='Created', value=role.created_at)
        embed.add_field(name='Permissions', value=len(role.permissions))
        await ctx.send(embed=embed)

    @commands.command(name='channelinfo', help='Get channel information')
    async def channelinfo(self, ctx, *, channel: discord.TextChannel):
        embed = discord.Embed(title=channel.name, color=discord.Color.green())
        embed.add_field(name='ID', value=channel.id)
        embed.add_field(name='Created', value=channel.created_at)
        embed.add_field(name='Topic', value=channel.topic or 'None')
        await ctx.send(embed=embed)

    @commands.command(name='time', help='Get current time')
    async def time(self, ctx):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        await ctx.send(f'Current time: {current_time}')

    @commands.command(name='ping', help='Get bot ping')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command(name='stats', help='Get bot statistics')
    async def stats(self, ctx):
        embed = discord.Embed(title='Bot Stats', color=discord.Color.orange())
        embed.add_field(name='Guilds', value=len(self.bot.guilds))
        embed.add_field(name='Commands', value='50+')
        await ctx.send(embed=embed)

    @commands.command(name='source', help='Get bot source')
    async def source(self, ctx):
        await ctx.send('Source: https://github.com/ridelmovies-wq/discord-bot-commands')

    @commands.command(name='perms', help='Check user permissions')
    async def perms(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        perms = ', '.join([p[0] for p in member.guild_permissions if p[1]])
        await ctx.send(f'{member.mention} permissions: {perms[:100]}...')

    @commands.command(name='prefix', help='Show bot prefix')
    async def prefix(self, ctx):
        await ctx.send('Bot prefix: !')

async def setup(bot):
    await bot.add_cog(Info(bot))
