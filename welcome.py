import discord
from discord.ext import commands
from discord.utils import get
import os

BASE_ROLE = os.getenv('BASE_ROLE_NAME')

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='pepito')
    async def test(self,ctx):
        await ctx.send("test!")

    async def set_adherent(self, member):
        role = get(member.guild.roles, name=str(BASE_ROLE))
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            how_cute = "https://media.giphy.com/media/Ae7SI3LoPYj8Q/giphy.gif"
            embed = discord.Embed(
                        title="Bienvenue :smile:",
                        color=discord.Colour.purple()
                    )
            embed.set_image(url=how_cute)
            await channel.send('Voici le discord du BDE {0.mention}. 🥳'.format(member), embed=embed)
            await self.set_adherent(member)

    # @commands.command()
    # async def hello(self, ctx, *, member: discord.Member = None):
    #     """Says hello"""
    #     member = member or ctx.author
    #     if self._last_member is None or self._last_member.id != member.id:
    #         await ctx.send('Hello {0.name}~'.format(member))
    #     else:
    #         await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
    #     self._last_member = member