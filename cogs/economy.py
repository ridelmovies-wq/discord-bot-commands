import discord
from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.balances = {}

    @commands.command(name='balance', help='Check your balance')
    async def balance(self, ctx):
        user_id = ctx.author.id
        bal = self.balances.get(user_id, 0)
        embed = discord.Embed(title='Balance', description=f'You have ${bal}', color=discord.Color.gold())
        await ctx.send(embed=embed)

    @commands.command(name='daily', help='Claim daily reward')
    async def daily(self, ctx):
        user_id = ctx.author.id
        self.balances[user_id] = self.balances.get(user_id, 0) + 100
        await ctx.send(f'{ctx.author.mention} claimed $100 daily reward!')

    @commands.command(name='weekly', help='Claim weekly reward')
    async def weekly(self, ctx):
        user_id = ctx.author.id
        self.balances[user_id] = self.balances.get(user_id, 0) + 500
        await ctx.send(f'{ctx.author.mention} claimed $500 weekly reward!')

    @commands.command(name='work', help='Work to earn money')
    async def work(self, ctx):
        user_id = ctx.author.id
        reward = 50
        self.balances[user_id] = self.balances.get(user_id, 0) + reward
        await ctx.send(f'{ctx.author.mention} worked and earned ${reward}!')

    @commands.command(name='transfer', help='Transfer money to user')
    async def transfer(self, ctx, member: discord.Member, amount: int):
        if amount <= 0:
            await ctx.send('Amount must be positive')
            return
        user_id = ctx.author.id
        if self.balances.get(user_id, 0) < amount:
            await ctx.send('Insufficient funds')
            return
        self.balances[user_id] -= amount
        self.balances[member.id] = self.balances.get(member.id, 0) + amount
        await ctx.send(f'{ctx.author.mention} transferred ${amount} to {member.mention}')

    @commands.command(name='rob', help='Rob a user')
    async def rob(self, ctx, member: discord.Member):
        victim_bal = self.balances.get(member.id, 0)
        if victim_bal == 0:
            await ctx.send(f'{member.mention} has no money to rob')
            return
        steal_amount = min(victim_bal // 2, 100)
        self.balances[member.id] -= steal_amount
        self.balances[ctx.author.id] = self.balances.get(ctx.author.id, 0) + steal_amount
        await ctx.send(f'{ctx.author.mention} robbed ${steal_amount} from {member.mention}!')

    @commands.command(name='leaderboard', help='View money leaderboard')
    async def leaderboard(self, ctx):
        sorted_balances = sorted(self.balances.items(), key=lambda x: x[1], reverse=True)[:10]
        embed = discord.Embed(title='Money Leaderboard', color=discord.Color.green())
        for i, (user_id, bal) in enumerate(sorted_balances, 1):
            embed.add_field(name=f'#{i}', value=f'<@{user_id}>: ${bal}', inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='bet', help='Bet money on coin flip')
    async def bet(self, ctx, amount: int):
        user_id = ctx.author.id
        if self.balances.get(user_id, 0) < amount:
            await ctx.send('Insufficient funds')
            return
        import random
        result = random.choice(['win', 'lose'])
        if result == 'win':
            self.balances[user_id] += amount
            await ctx.send(f'You won! ${amount} added to your balance')
        else:
            self.balances[user_id] -= amount
            await ctx.send(f'You lost! ${amount} removed from your balance')

    @commands.command(name='gamble', help='Gamble money')
    async def gamble(self, ctx, amount: int):
        await ctx.invoke(self.bot.get_command('bet'), amount)

async def setup(bot):
    await bot.add_cog(Economy(bot))
