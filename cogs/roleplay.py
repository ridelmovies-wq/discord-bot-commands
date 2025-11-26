import discord
from discord.ext import commands
import random

class Roleplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='punch', help='Punch someone')
    async def punch(self, ctx, member: discord.Member = None):
        if member:
            await ctx.send(f'{ctx.author.mention} punches {member.mention}! 👊')
        else:
            await ctx.send('Please specify a member to punch')

    @commands.command(name='kick', help='Kick someone')
    async def kick(self, ctx, member: discord.Member = None):
        if member:
            await ctx.send(f'{ctx.author.mention} kicks {member.mention}! 👛')
        else:
            await ctx.send('Please specify a member to kick')

    @commands.command(name='dance', help='Dance')
    async def dance(self, ctx):
        await ctx.send(f'{ctx.author.mention} is dancing! 🕵')

    @commands.command(name='laugh', help='Laugh')
    async def laugh(self, ctx):
        await ctx.send(f'{ctx.author.mention} is laughing! 😂')

    @commands.command(name='cry', help='Cry')
    async def cry(self, ctx):
        await ctx.send(f'{ctx.author.mention} is crying! 😢')

    @commands.command(name='wave', help='Wave at someone')
    async def wave(self, ctx, member: discord.Member = None):
        if member:
            await ctx.send(f'{ctx.author.mention} waves at {member.mention}! 👋')
        else:
            await ctx.send(f'{ctx.author.mention} waves at everyone! 👋')

    @commands.command(name='jump', help='Jump')
    async def jump(self, ctx):
        await ctx.send(f'{ctx.author.mention} jumps! 😷')

    @commands.command(name='scream', help='Scream')
    async def scream(self, ctx):
        await ctx.send(f'{ctx.author.mention} screams! 😬')

    @commands.command(name='freeze', help='Freeze someone')
    async def freeze(self, ctx, member: discord.Member = None):
        if member:
            await ctx.send(f'{member.mention} is frozen! ❄')
        else:
            await ctx.send(f'{ctx.author.mention} freezes! ❄')

    @commands.command(name='yawn', help='Yawn')
    async def yawn(self, ctx):
        await ctx.send(f'{ctx.author.mention} yawns 🙱')

async def setup(bot):
    await bot.add_cog(Roleplay(bot))
