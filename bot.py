# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(name='miaou', help='Miaou from an angry Gizmo')
async def miaou(ctx):
    miaou = "Miaou 😺"
    await ctx.send(miaou)

@bot.command(name='wouaf', help='Wouaf from an angry Gizmo')
async def wouaf(ctx):
    wouaf = "Bon toutou 🐶"
    await ctx.send(wouaf)

bot.run(TOKEN)
