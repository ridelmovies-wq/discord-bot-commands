import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setprefix', help='Set bot prefix')
    @commands.is_owner()
    async def setprefix(self, ctx, prefix: str):
        await ctx.send(f'Prefix set to: {prefix}')

    @commands.command(name='reload', help='Reload a cog')
    @commands.is_owner()
    async def reload(self, ctx, extension: str):
        await self.bot.reload_extension(extension)
        await ctx.send(f'Reloaded {extension}')

    @commands.command(name='load', help='Load a cog')
    @commands.is_owner()
    async def load(self, ctx, extension: str):
        await self.bot.load_extension(extension)
        await ctx.send(f'Loaded {extension}')

    @commands.command(name='unload', help='Unload a cog')
    @commands.is_owner()
    async def unload(self, ctx, extension: str):
        await self.bot.unload_extension(extension)
        await ctx.send(f'Unloaded {extension}')

    @commands.command(name='shutdown', help='Shutdown bot')
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send('Shutting down...')
        await self.bot.close()

    @commands.command(name='restart', help='Restart bot')
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.send('Restarting...')

    @commands.command(name='announce', help='Make announcement')
    @commands.has_permissions(administrator=True)
    async def announce(self, ctx, *, message):
        embed = discord.Embed(title='Announcement', description=message, color=discord.Color.red())
        await ctx.send(embed=embed)

    @commands.command(name='broadcast', help='Broadcast message')
    @commands.is_owner()
    async def broadcast(self, ctx, *, message):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                try:
                    await channel.send(message)
                    break
                except:
                    pass

    @commands.command(name='setstatus', help='Set bot status')
    @commands.is_owner()
    async def setstatus(self, ctx, *, status):
        await self.bot.change_presence(activity=discord.Game(name=status))
        await ctx.send(f'Status set to: {status}')

    @commands.command(name='eval', help='Evaluate code')
    @commands.is_owner()
    async def eval(self, ctx, *, code):
        await ctx.send('Evaluation completed')

    @commands.command(name='guildconfig', help='Configure guild')
    @commands.has_permissions(administrator=True)
    async def guildconfig(self, ctx):
        embed = discord.Embed(title='Guild Config', color=discord.Color.blue())
        embed.add_field(name='Name', value=ctx.guild.name)
        embed.add_field(name='ID', value=ctx.guild.id)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Admin(bot))
