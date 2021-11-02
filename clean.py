import discord
from discord.ext import commands
from discord.utils import get
from discord.client import Client
import os
import asyncio

class Cleaner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.has_role("BDE-modérateur")
    @commands.command(name='clear')
    async def clear_channel(self, ctx, number=1):
        deleted_all = 0
        cleaner=0
        while cleaner < number:
            deleted = await ctx.channel.purge(limit=100)
            cleaner+=1
            deleted_all += len(deleted)
        await ctx.channel.send('Deleted {} message(s)🗑'.format(deleted_all))