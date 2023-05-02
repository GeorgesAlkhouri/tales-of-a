from discord import Intents, File
from discord.ext import commands
import random

from config import Config
from game import Game

game = Game()
config = Config()

# TODO : limit to only what is needed..
intents = Intents.all()

bot = commands.Bot(command_prefix=config.default_prefix, intents=intents)


@bot.command(name='tales')
async def start_game(ctx):
    global game
    game = Game()
    game.render_map()
    await ctx.send(f"{ctx.author.mention} started a new game!", file=File("map.png"))


@bot.command(name='move')
async def move_hero(ctx, direction: str):
    response, success = game.move_hero(direction)
    if success:
        game.render_map()
        await ctx.send(f"{ctx.author.mention} moved {direction}!", file=File("map.png"))
        await ctx.send(f"{game.get_hero_status()}")
    else:
        await ctx.send(f"{ctx.author.mention}, {response}")


@bot.command(name='guess')
async def guess_number(ctx, number: int):
    target_number = random.randint(1, 10)
    if number == target_number:
        await ctx.send(f'Congratulations {ctx.author.mention}! You guessed the number correctly!')
    else:
        await ctx.send(f'Sorry {ctx.author.mention}, the correct number was {target_number}. Better luck next time!')


@guess_number.error
async def guess_number_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention}, you need to provide a number between 1 and 10.')
    elif isinstance(error, commands.BadArgument):
        await ctx.send(f'{ctx.author.mention}, your input is not a valid integer.')
    else:
        raise error


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.run(config.bot_token)
