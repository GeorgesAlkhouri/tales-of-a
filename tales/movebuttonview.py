import discord.ui

class MoveButtonsView(discord.ui.View):
    def __init__(self, game, ctx):
        super().__init__()
        self.game = game
        self.ctx = ctx
        self.icons = {
            'Up': '<:Up:1099599316684910604>',
            'Down': '<:Down:1099595210855559300>',
            'Left': '<:Left:1099599703567503460>',
            'Right': '<:Right:1099599811533094962>',
        }
        
        self.move_left.emoji = self.icons['Left']
        self.move_up.emoji = self.icons['Up']
        self.move_down.emoji = self.icons['Down']
        self.move_right.emoji = self.icons['Right']

    @discord.ui.button(label="Left", style=discord.ButtonStyle.primary)
    async def move_left(self, button, interaction):
        await self.move("left", interaction)

    @discord.ui.button(label="Up", style=discord.ButtonStyle.primary)
    async def move_up(self, button, interaction):
        await self.move("up", interaction)

    @discord.ui.button(label="Down", style=discord.ButtonStyle.primary)
    async def move_down(self, button, interaction):
        await self.move("down", interaction)

    @discord.ui.button(label="Right", style=discord.ButtonStyle.primary)
    async def move_right(self, button, interaction):
        await self.move("right", interaction)

    async def move(self, direction, interaction):
        response, success = self.game.move_hero(direction)
        if success:
            self.game.render_map()
            hero_status = self.game.get_hero_status()

            embed = discord.Embed(
                title=f"{self.ctx.author.name} moved {direction}!",
                description=f"{hero_status}",
                color=discord.Color.blue(),
            )
            embed.set_image(url="attachment://map_image.png")

            await interaction.response.edit_message(
                file=discord.File("map.png", filename="map_image.png"),
                embed=embed,
                view=self
            )
        else:
            await interaction.response.send_message(f"{self.ctx.author.mention}, {response}")