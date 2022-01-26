import os
import discord
import random
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from utils import *

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
    await ctx.send(f"Hi {str(ctx.author.display_name)}, I'm dad!")

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
    chunks = [shuffled_people[i::n] for i in range(n)]
    response = ''
    for i in range(len(chunks)):
        response += 'Team ' + str(i+1) + ': '
        response += ', '.join(chunks[i])
        if i < len(chunks)-1:
            response += '\n'
    await ctx.send(response)

@bot.command(name='24')
async def twentyfour(ctx):
    
    nums = [random.randint(1,9) for _ in range(4)]
    await ctx.send("Your numbers are: " + ', '.join([str(i) for i in nums]))
    
    chk = lambda m : m.author == ctx.author and m.channel == ctx.channel
     
    ans = solve24([str(n) for n in nums])
    while ans == 'No solution found.':
        nums = [random.randint(1,9) for _ in range(4)]
        ans = solve24([str(n) for n in nums])

    try:
        sol = await bot.wait_for("message", check=chk, timeout=80)
    except asyncio.TimeoutError:
        await ctx.send(f"Time's up, {ctx.author.display_name}. I'm not waiting 2 years. A possible solution was " + ans + ".")
        return

    def sanitize(s, wl = '0123456789/*+-()'):
        return ''.join([c for c in s if c in wl])

    sol = sanitize(sol.content)
    if sorted(nums) == sorted([int(c) for c in sol if c.isnumeric()]) and eval(sol) == 24:
        await ctx.send(f"Good job, {ctx.author.display_name}. Have a cookie :cookie:")
    else:
        await ctx.send(f"{ctx.author.display_name}, that's wrong kid. Don't you know how to count? A possible solution was " + ans + ".")


@bot.command(name='wordle')
async def wordle(ctx):
    await ctx.send('wordle')

#########################################################
# Fas fax commands
#########################################################

@bot.command(name='fasfax')
async def fasfax(ctx, *args):
    chk = lambda m : m.channel == ctx.channel
    while True:
        resp = await bot.wait_for("message", check=chk, timeout=None)
        if resp.content == 'stop':
            return
        else:
            await ctx.send(resp.content)


bot.run(TOKEN)
