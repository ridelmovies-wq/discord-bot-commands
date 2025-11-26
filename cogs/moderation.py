import discord
from discord.ext import commands
from datetime import timedelta

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', help='Kick a user from the server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title='Member Kicked', color=0xFF6B6B)
        embed.add_field(name='User', value=member.mention)
        embed.add_field(name='Reason', value=reason or 'No reason provided')
        await ctx.send(embed=embed)

    @commands.command(name='ban', help='Ban a user from the server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title='Member Banned', color=0xFF6B6B)
        embed.add_field(name='User', value=member.mention)
        embed.add_field(name='Reason', value=reason or 'No reason provided')
        await ctx.send(embed=embed)

    @commands.command(name='unban', help='Unban a user from the server')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, user):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = user.split('#')
        for ban_entry in banned_users:
            user_obj = ban_entry.user
            if (user_obj.name, user_obj.discriminator) == (member_name, member_disc):
                await ctx.guild.unban(user_obj)
                await ctx.send(f'Unbanned {user_obj.mention}')
                return

    @commands.command(name='mute', help='Mute a user')
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        await member.edit(mute=True)
        await ctx.send(f'{member.mention} has been muted. Reason: {reason or "No reason provided"}')

    @commands.command(name='unmute', help='Unmute a user')
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        await member.edit(mute=False)
        await ctx.send(f'{member.mention} has been unmuted')

    @commands.command(name='warn', help='Warn a user')
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(title='User Warned', color=0xFFD700)
        embed.add_field(name='User', value=member.mention)
        embed.add_field(name='Reason', value=reason or 'No reason')
        await ctx.send(embed=embed)

    @commands.command(name='clear', help='Clear messages')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Cleared {amount} messages', delete_after=5)

    @commands.command(name='slowmode', help='Set slowmode for channel')
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f'Slowmode set to {seconds} seconds')

    @commands.command(name='lock', help='Lock a channel')
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send('Channel locked')

    @commands.command(name='unlock', help='Unlock a channel')
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=None)
        await ctx.send('Channel unlocked')

async def setup(bot):
    await bot.add_cog(Moderation(bot))
