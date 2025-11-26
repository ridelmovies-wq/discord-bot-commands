import discord
from discord.ext import commands
from datetime import datetime

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logs = []

    @commands.command(name='log', help='Log a message')
    async def log_message(self, ctx, *, message: str):
        log_entry = f'[{datetime.now()}] {ctx.author}: {message}'
        self.logs.append(log_entry)
        await ctx.send(f'Logged: {message}')

    @commands.command(name='logs', help='View recent logs')
    async def view_logs(self, ctx, count: int = 5):
        recent_logs = self.logs[-count:]
        log_text = '\n'.join(recent_logs)
        await ctx.send(f'```{log_text}```')

    @commands.command(name='clearlog', help='Clear all logs')
    async def clear_logs(self, ctx):
        self.logs = []
        await ctx.send('All logs have been cleared!')

    @commands.command(name='logcount', help='Count total logs')
    async def log_count(self, ctx):
        await ctx.send(f'Total logs: {len(self.logs)}')

    @commands.command(name='exportlogs', help='Export logs to file')
    async def export_logs(self, ctx):
        if not self.logs:
            await ctx.send('No logs to export!')
            return
        log_text = '\n'.join(self.logs)
        await ctx.send(f'Logs count: {len(self.logs)}')

    @commands.command(name='adlog', help='Admin log message')
    async def admin_log(self, ctx, user: discord.Member, *, action: str):
        log_entry = f'[ADMIN] {user.name}: {action}'
        self.logs.append(log_entry)
        await ctx.send(f'Admin action logged: {action}')

    @commands.command(name='searchlog', help='Search logs')
    async def search_logs(self, ctx, *, query: str):
        results = [log for log in self.logs if query.lower() in log.lower()]
        if results:
            log_text = '\n'.join(results[:5])
            await ctx.send(f'Found {len(results)} results:\n```{log_text}```')
        else:
            await ctx.send('No logs found matching that query')

    @commands.command(name='filterlog', help='Filter logs by user')
    async def filter_logs(self, ctx, user: str = None):
        if user:
            filtered = [log for log in self.logs if user in log]
            if filtered:
                log_text = '\n'.join(filtered[-3:])
                await ctx.send(f'```{log_text}```')
        else:
            await ctx.send('Please specify a user to filter')

    @commands.command(name='logsummary', help='Get logs summary')
    async def logs_summary(self, ctx):
        embed = discord.Embed(title='Logs Summary', color=discord.Color.green())
        embed.add_field(name='Total Entries', value=len(self.logs), inline=False)
        if self.logs:
            embed.add_field(name='Latest Entry', value=self.logs[-1], inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Logging(bot))
