import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll', help='Roll a dice')
    async def roll(self, ctx, dice: str = '1d6'):
        try:
            rolls, limit = map(int, dice.split('d'))
            if rolls > 100:
                await ctx.send('Too many rolls!')
                return
            result = [random.randint(1, limit) for _ in range(rolls)]
            await ctx.send(f'Rolls: {result} | Total: {sum(result)}')
        except:
            await ctx.send('Invalid format! Use: 1d6')

    @commands.command(name='coinflip', help='Flip a coin')
    async def coinflip(self, ctx):
        result = random.choice(['Heads', 'Tails'])
        embed = discord.Embed(title='Coin Flip', description=result, color=discord.Color.gold())
        await ctx.send(embed=embed)

    @commands.command(name='joke', help='Tell a joke')
    async def joke(self, ctx):
        jokes = [
            'Why did the scarecrow win an award? He was outstanding in his field!',
            'What do you call a bear with no teeth? A gummy bear!',
            'Why don\'t scientists trust atoms? Because they make up everything!'
        ]
        await ctx.send(random.choice(jokes))

    @commands.command(name='8ball', help='Ask the magic 8 ball')
    async def eightball(self, ctx, *, question=None):
        if not question:
            await ctx.send('Ask a question!')
            return
        responses = ['Yes', 'No', 'Maybe', 'Ask again later', 'Definitely', 'Not likely']
        await ctx.send(f'{random.choice(responses)}')

    @commands.command(name='choose', help='Choose between options')
    async def choose(self, ctx, *choices):
        if len(choices) < 2:
            await ctx.send('Provide at least 2 choices!')
            return
        await ctx.send(f'I choose: {random.choice(choices)}')

    @commands.command(name='rps', help='Rock Paper Scissors')
    async def rps(self, ctx, user_choice: str):
        choices = ['rock', 'paper', 'scissors']
        bot_choice = random.choice(choices)
        await ctx.send(f'I chose: {bot_choice}')

    @commands.command(name='reverse', help='Reverse text')
    async def reverse(self, ctx, *, text):
        await ctx.send(f'Reversed: {text[::-1]}')

    @commands.command(name='ascii', help='Convert to ASCII art')
    async def ascii(self, ctx, *, text):
        if len(text) > 20:
            await ctx.send('Text too long!')
            return
        await ctx.send(f'```{text}```')

    @commands.command(name='hug', help='Hug someone')
    async def hug(self, ctx, member: discord.Member):
        embed = discord.Embed(description=f'{ctx.author.mention} hugs {member.mention}!', color=discord.Color.magenta())
        await ctx.send(embed=embed)

    @commands.command(name='slap', help='Slap someone')
    async def slap(self, ctx, member: discord.Member):
        embed = discord.Embed(description=f'{ctx.author.mention} slaps {member.mention}!', color=discord.Color.red())
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))
