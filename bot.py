import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    """Bot will say hello to you"""
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def bye(ctx):
    """Bot will say bye to you"""
    await ctx.send(f'Bye!')

@bot.command()
async def rand0m(ctx, left: int, right: int):
    """Choose a random number (type: $random <number1> <number2>)"""
    await ctx.send(random.randint(left, right))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together (type: $add <number1> <number2>)"""
    await ctx.send(left + right)

@bot.command()
async def minus(ctx, left: int, right: int):
    """Deducts from number1 number2 (type: minus <number1> <number2>)"""
    await ctx.send(left - right)

@bot.command()
async def repeat(ctx, times: int, content: str):
    """Repeats a message multiple times (type: $repeat <number>)"""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def heh(ctx, count_heh = 5):
    """Say he (type: $heh <number>)"""
    await ctx.send("he" * count_heh)


async def help(ctx):
    await ctx.send('$hello, $bye, $rand0m <число1> <число2>, $add <число1> <число2>, $minus <число1> <число2>, $repeat <число>, $heh <число>')

bot.run("Token")
