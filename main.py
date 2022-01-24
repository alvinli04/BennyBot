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

@bot.event
async def on_message(message):
    if not message.author.bot:
        msg = message.content
        msgl = msg.lower()
        if "im" in msgl:
            idx = msgl.index("im") + 2
            await message.channel.send(f"Hi{msg[idx:]}, I'm dad!")
        elif "i'm" in msgl:
            idx = msgl.index("i'm") + 3
            await message.channel.send(f"Hi{msg[idx:]}, I'm dad!")
    await bot.process_commands(message)

@bot.command(name='dad')
async def dad(ctx):
    await ctx.send(f"Hi {str(ctx.author)[:-5]}, I'm dad!")

@bot.command(name='praise')
async def praise(ctx):
    words_of_praise = [
            'GAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHH!!!!!!!',
            'DIE DIE DIE DIE DIE!',
            'I love you.',
            'AAARGHH!!1!',
            'BWWWWAAAAAAHH'
    ]
    response = random.choice(words_of_praise)
    await ctx.send(response)

@bot.command(name='flip')
async def flip(ctx):
    await ctx.send(('Heads.' if random.randint(0,1) else 'Tails.'))

@bot.command(name='maketeams')
async def maketeams(ctx, n: int, *people):
    shuffled_people = random.sample(people, len(people))
    if len(people) < n:
        await ctx.send('Not enough people!')
        return
    chunks = [people[i::n] for i in range(n)]
    response = ''
    for i in range(len(chunks)):
        response += 'Team' + str(i+1) + ': '
        response += ', '.join(chunks[i])
        if i < len(chunks)-1:
            response += '\n'
    await ctx.send(response)

@bot.command(name='24')
async def twentyfour(ctx):
    await ctx.send('24')

@bot.command(name='wordle')
async def wordle(ctx):
    await ctx.send('wordle')

bot.run(TOKEN)
