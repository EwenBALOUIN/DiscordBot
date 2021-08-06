# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MY_USER_ID = os.getenv('MY_USER_ID')

bot = commands.Bot(command_prefix='$')

@bot.command(name='miaou', help='Miaou from an angry Gizmo')
async def miaou(ctx):
    author = ctx.message.author
    if author.id != int(MY_USER_ID):
        await not_good_person(author)
        return
    miaou = "Miaou 😺"
    await ctx.send(miaou)

@bot.command(name='wouaf', help='Wouaf from an angry Gizmo')
async def wouaf(ctx):
    author = ctx.message.author
    if author.id != int(MY_USER_ID):
        await not_good_person(author)
        return
    wouaf = "Bon toutou 🐶"
    await ctx.send(wouaf)


async def not_good_person(author):
        await author.create_dm()
        await author.dm_channel.send(
            "T'as pas le droit FDP"
        )


bot.run(TOKEN)
