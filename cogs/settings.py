import discord
from discord.ext import commands

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings = {}

    @commands.command(name='setprefix', help='Set bot prefix')
    async def set_prefix(self, ctx, prefix: str):
        self.settings['prefix'] = prefix
        await ctx.send(f'Prefix set to `{prefix}`')

    @commands.command(name='setwelcome', help='Set welcome message')
    async def set_welcome(self, ctx, *, message: str):
        self.settings['welcome_msg'] = message
        await ctx.send('Welcome message set!')

    @commands.command(name='setnotifications', help='Enable or disable notifications')
    async def set_notifications(self, ctx, setting: str):
        if setting.lower() in ['on', 'off']:
            self.settings['notifications'] = setting.lower()
            await ctx.send(f'Notifications turned {setting.lower()}')
        else:
            await ctx.send('Use `on` or `off`')

    @commands.command(name='setlanguage', help='Set bot language')
    async def set_language(self, ctx, lang: str):
        self.settings['language'] = lang
        await ctx.send(f'Language set to {lang}')

    @commands.command(name='settheme', help='Set bot theme')
    async def set_theme(self, ctx, theme: str):
        if theme in ['light', 'dark', 'auto']:
            self.settings['theme'] = theme
            await ctx.send(f'Theme set to {theme}')
        else:
            await ctx.send('Theme must be light, dark, or auto')

    @commands.command(name='getprefix', help='Get current prefix')
    async def get_prefix(self, ctx):
        prefix = self.settings.get('prefix', '!')
        await ctx.send(f'Current prefix: `{prefix}`')

    @commands.command(name='getsettings', help='View all settings')
    async def get_settings(self, ctx):
        embed = discord.Embed(title='Bot Settings', color=discord.Color.blue())
        for key, value in self.settings.items():
            embed.add_field(name=key.replace('_', ' ').title(), value=str(value), inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='resetsettings', help='Reset all settings to default')
    async def reset_settings(self, ctx):
        self.settings = {}
        await ctx.send('All settings have been reset to default!')

async def setup(bot):
    await bot.add_cog(Settings(bot))
