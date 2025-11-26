import discord
from discord.ext import commands
import random

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='guess', help='Guess the number game')
    async def guess_number(self, ctx):
        number = random.randint(1, 100)
        await ctx.send(f'{ctx.author.mention}, guess a number between 1 and 100!')
        try:
            guess = await self.bot.wait_for('message', timeout=30.0, check=lambda m: m.author == ctx.author)
            if int(guess.content) == number:
                await ctx.send(f'Correct! The number was {number}')
            else:
                await ctx.send(f'Wrong! The number was {number}')
        except:
            await ctx.send('Timeout!')

    @commands.command(name='coin', help='Flip a coin')
    async def coin_flip(self, ctx):
        result = random.choice(['Heads', 'Tails'])
        await ctx.send(f'{ctx.author.mention} flipped a coin and got **{result}**!')

    @commands.command(name='dice', help='Roll a dice')
    async def roll_dice(self, ctx, sides: int = 6):
        result = random.randint(1, sides)
        await ctx.send(f'{ctx.author.mention} rolled a d{sides} and got **{result}**!')

    @commands.command(name='roulette', help='Russian roulette game')
    async def roulette(self, ctx):
        result = random.randint(1, 6)
        if result == 1:
            await ctx.send(f'{ctx.author.mention} played Russian roulette... 💀')
        else:
            await ctx.send(f'{ctx.author.mention} survived this time!')

    @commands.command(name='trivia', help='Answer a trivia question')
    async def trivia(self, ctx):
        questions = {
            'What is the capital of France?': 'paris',
            'What is 2+2?': '4',
            'Who wrote Romeo and Juliet?': 'shakespeare'
        }
        question = random.choice(list(questions.keys()))
        answer = questions[question]
        await ctx.send(f'{ctx.author.mention}, {question}')
        try:
            response = await self.bot.wait_for('message', timeout=30.0, check=lambda m: m.author == ctx.author)
            if response.content.lower() == answer:
                await ctx.send('Correct!')
            else:
                await ctx.send(f'Wrong! The answer was {answer}')
        except:
            await ctx.send('Timeout!')

    @commands.command(name='hangman', help='Play hangman')
    async def hangman(self, ctx):
        words = ['python', 'discord', 'hangman', 'coding']
        word = random.choice(words)
        guessed = set()
        await ctx.send(f'{ctx.author.mention}, hangman game started!')
        await ctx.send('_ ' * len(word))

    @commands.command(name='slots', help='Play slot machine')
    async def slots(self, ctx):
        emojis = ['🍎', '🍊', '🍋', '🍌', '🍉']
        result = [random.choice(emojis) for _ in range(3)]
        await ctx.send(f'{ctx.author.mention}: {" ".join(result)}')
        if result[0] == result[1] == result[2]:
            await ctx.send('Jackpot! 🎉')
        else:
            await ctx.send('No match!')

    @commands.command(name='blackjack', help='Play blackjack')
    async def blackjack(self, ctx):
        await ctx.send(f'{ctx.author.mention}, blackjack game started!')
        await ctx.send('You got: [5 ♠] [10 ♥]')

    @commands.command(name='connectfour', help='Challenge to connect four')
    async def connect_four(self, ctx, opponent: discord.Member = None):
        if opponent is None:
            await ctx.send('Please specify an opponent!')
            return
        await ctx.send(f'{ctx.author.mention} challenged {opponent.mention} to Connect Four!')

    @commands.command(name='higherlower', help='Higher or lower game')
    async def higher_lower(self, ctx):
        number = random.randint(1, 100)
        await ctx.send(f'{ctx.author.mention}, I am thinking of a number between 1 and 100')
        await ctx.send('Is it higher or lower than 50?')

async def setup(bot):
    await bot.add_cog(Games(bot))
