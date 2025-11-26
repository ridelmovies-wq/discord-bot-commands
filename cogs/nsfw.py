import discord
from discord.ext import commands

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='meme', help='Get a random meme')
    @commands.is_nsfw()
    async def meme(self, ctx):
        await ctx.send(f'{ctx.author.mention}, here is a random meme!')

    @commands.command(name='hug', help='Give someone a hug')
    async def hug(self, ctx, member: discord.Member = None):
        if member:
            await ctx.send(f'{ctx.author.mention} hugs {member.mention} 🤗')
        else:
            await ctx.send(f'{ctx.author.mention} hugs everyone! 🤗')

    @commands.command(name='kiss', help='Send a kiss')
    async def kiss(self, ctx, member: discord.Member = None):
        if member:
            await ctx.send(f'{ctx.author.mention} kisses {member.mention} 💋')
        else:
            await ctx.send(f'{ctx.author.mention} blows a kiss! 💋')

    @commands.command(name='slap', help='Slap someone')
    async def slap(self, ctx, member: discord.Member = None):
        if member:
            await ctx.send(f'{ctx.author.mention} slapped {member.mention}! 👋')
        else:
            await ctx.send('Please specify a member to slap')

    @commands.command(name='cuddle', help='Cuddle someone')
    async def cuddle(self, ctx, member: discord.Member = None):
        if member:
            await ctx.send(f'{ctx.author.mention} cuddles with {member.mention} 😘')
        else:
            await ctx.send(f'{ctx.author.mention} is looking for someone to cuddle!')

    @commands.command(name='insult', help='Get an insult')
    async def insult(self, ctx, member: discord.Member = None):
        insults = ['Is that your face or did your neck throw up?', 'I would roast you, but I can only do that to things that can hear me']
        import random
        insult = random.choice(insults)
        if member:
            await ctx.send(f'{member.mention}: {insult}')
        else:
            await ctx.send(insult)

    @commands.command(name='compliment', help='Give a compliment')
    async def compliment(self, ctx, member: discord.Member = None):
        compliments = ['You are awesome!', 'Your smile is great!', 'You are brilliant!', 'You light up the room!']
        import random
        compliment = random.choice(compliments)
        if member:
            await ctx.send(f'{member.mention}: {compliment}')
        else:
            await ctx.send(f'{ctx.author.mention}: {compliment}')

async def setup(bot):
    await bot.add_cog(NSFW(bot))
