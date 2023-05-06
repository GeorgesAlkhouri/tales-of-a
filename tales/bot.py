from discord import File
import discord
from discord.ext import bridge

from config import Config
from game import Game
from movebuttonview import MoveButtonsView

game = Game()
config = Config()

# TODO : limit to only what is needed..
intents = discord.Intents.all()

bot = bridge.Bot(command_prefix=config.default_prefix, intents=intents)


@bot.bridge_command()
async def tales(ctx):
    global game
    game = Game()
    game.render_map()
    await ctx.respond(f"{ctx.author.mention} started a new game!", file=File("map.png"))


@bot.bridge_command()
async def move(ctx, direction: str):
    response, success = game.move_hero(direction)
    if success:
        game.render_map()
        hero_status = game.get_hero_status()

        embed = discord.Embed(
            title=f"{ctx.author.name} moved {direction}!",
            description=f"{hero_status}",
            color=discord.Color.blue(),
        )
        embed.set_image(url="attachment://map_image.png")

        move_buttons_view = MoveButtonsView(game, ctx)

        await ctx.respond(
            file=discord.File("map.png", filename="map_image.png"),
            embed=embed,
            view=move_buttons_view,
        )
    else:
        await ctx.respond(f"{ctx.author.mention}, {response}")


@bot.bridge_command()
async def map(ctx):
    global game
    if not game:
        await ctx.respond(
            f"{ctx.author.mention}, you need to start a game first using the `>startgame` command."
        )
        return

    game.render_map()
    await ctx.respond(
        f"{ctx.author.mention} here's the current state of the map:",
        file=discord.File("map.png"),
    )


@bot.bridge_command()
async def inventory(ctx):
    global game
    if not game:
        await ctx.respond(
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
        inventory_list = game.player.get_inventory()
        embed.add_field(
            name="Items", value=inventory_list, inline=False
        )

    await ctx.respond(embed=embed)


@bot.bridge_command()
async def version(ctx):
    await ctx.respond(f"Current bot version: {config.version}")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, bridge.CommandNotFound):
        await ctx.send("Unknown command.")
    else:
        await ctx.send(f"Error: {error}")


bot.run(config.bot_token)
