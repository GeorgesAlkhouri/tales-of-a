from discord import Intents, File
import discord
from discord.ext import commands
import random

from config import Config
from game import Game

game = Game()
config = Config()

# TODO : limit to only what is needed..
intents = Intents.all()

bot = commands.Bot(command_prefix=config.default_prefix, intents=intents)


@bot.command(name="tales")
async def start_game(ctx):
    global game
    game = Game()
    game.render_map()
    await ctx.send(f"{ctx.author.mention} started a new game!", file=File("map.png"))


@bot.command(name="move", aliases=["m"])
async def move_hero(ctx, direction: str):
    response, success = game.move_hero(direction)
    if success:
        game.render_map()
        await ctx.send(f"{ctx.author.mention} moved {direction}!", file=File("map.png"))
        await ctx.send(f"{game.get_hero_status()}")
    else:
        await ctx.send(f"{ctx.author.mention}, {response}")


@bot.command(name="map")
async def show_map(ctx):
    global game
    if not game:
        await ctx.send(
            f"{ctx.author.mention}, you need to start a game first using the `>startgame` command."
        )
        return

    game.render_map()
    await ctx.send(
        f"{ctx.author.mention} here's the current state of the map:",
        file=discord.File("map.png"),
    )


@bot.command(name="inventory", aliases=["i"])
async def list_inventory(ctx):
    global game
    if not game:
        await ctx.send(
            f"{ctx.author.mention}, you need to start a game first using the `startgame` command."
        )
        return

    embed = discord.Embed(
        title=f"__**{ctx.author.name}'s Inventory**__", color=discord.Color.blue()
    )
    embed.set_thumbnail(url=ctx.author.avatar)

    if not game.player.inventory:
        embed.description = "Your inventory is empty."
    else:
        for item in game.player.inventory:
            embed.add_field(
                name=item, value="Item description or quantity", inline=False
            )

    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command.")
    else:
        await ctx.send(f"Error: {error}")


bot.run(config.bot_token)
