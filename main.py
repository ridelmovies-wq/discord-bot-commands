import discord
from discord.ext import commands
import os
from config import TOKEN, PREFIX

# Initialize bot
bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

# Load all command cogs
async def load_cogs():
    cog_files = [
        'cogs.moderation',
        'cogs.music',
        'cogs.utility',
        'cogs.fun',
        'cogs.admin',
        'cogs.info'
    ]
    for cog in cog_files:
        try:
            await bot.load_extension(cog)
            print(f'Loaded {cog}')
        except Exception as e:
            print(f'Failed to load {cog}: {e}')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game(name=f'{PREFIX}help | 50+ commands'))

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server!')

@bot.command(name='ping')
async def ping(ctx):
    """Check bot latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! {latency}ms')

@bot.command(name='status')
async def status(ctx):
    """Check bot status"""
    embed = discord.Embed(title='Bot Status', color=discord.Color.green())
    embed.add_field(name='Status', value='Online')
    embed.add_field(name='Latency', value=f'{round(bot.latency * 1000)}ms')
    embed.add_field(name='Servers', value=len(bot.guilds))
    embed.add_field(name='Users', value=len(list(bot.get_all_members())))
    await ctx.send(embed=embed)

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
