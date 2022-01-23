import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='b!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='dad')
async def dad(ctx):
    await ctx.send(f"Hi {str(ctx.author)[:-5]}, I'm dad!")

@bot.command(name='praise')
async def praise(ctx):
    words_of_praise = [
            'GAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHH!!!!!!!',
            'DIE DIE DIE DIE DIE!',
            'I love you.'
    ]
    response = random.choice(words_of_praise)
    await ctx.send(response)

@bot.command(name='flip')
async def flip(ctx):
    await ctx.send(('Heads.' if random.randint(0,1) else 'Tails.'))

bot.run(TOKEN)
