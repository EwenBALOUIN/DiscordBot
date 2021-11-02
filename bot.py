# bot.py
import os
import random
import discord
import requests
import json

import welcome
import clean

from discord.ext import commands
from dotenv import load_dotenv
from discord.client import Client

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN_BDE')
MY_USER_ID = os.getenv('MY_USER_ID')


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name='miaou', help='Miaou from an angry Gizmo')
async def miaou(ctx):
    author = ctx.message.author
    miaou = "Miaou 😺"
    await ctx.send(miaou)

@bot.command(name='wouaf', help='Wouaf from an angry Gizmo')
async def wouaf(ctx):
    author = ctx.message.author
    wouaf = "Bon toutou 🐶 @P N#4510"
    await ctx.send(wouaf)

@commands.has_role("BDE-modérateur")
@bot.command(name='wtf', help='WTF')
async def wtf(ctx):
    url = "https://nekobot.xyz/api/image?type=coffee"
    response = requests.get(url)
    data = response.json()
    gif = data["message"]
    embed = discord.Embed(
                title=":rofl: **FUNNY**",
                color=discord.Colour.red()
            )
    embed.set_image(url=gif)
    await ctx.send(embed=embed)

async def not_good_person(author):
        await author.create_dm()
        await author.dm_channel.send(
            "T'as pas le droit FDP"
        )

bot.add_cog(welcome.Greetings(bot))
bot.add_cog(clean.Cleaner(bot))
bot.run(TOKEN)
