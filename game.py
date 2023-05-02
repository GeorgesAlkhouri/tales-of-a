import random
from PIL import Image, ImageDraw, ImageFont

from player import Player

icons = {
    "hero": "assets/images/hero.png",
    "grass": "assets/images/grass.png",
    "water": "assets/images/water.png",
    "forest": "assets/images/forrest.png",
    "mountain": "assets/images/mountain.png",
    "plateau": "assets/images/plateau.png"
}


class Game:

    def __init__(self):
        self.game_map = []
        self.hero_position = (5, 5)
        self.player = Player(health=12, energy=12)
        self.generate_map()

    def get_hero_status(self):
        return self.player.get_status()

    def generate_map(self):
        self.game_map = []

        terrain_choices = ["grass", "water", "forest", "mountain", "plateau"]

        for i in range(10):
            row = []
            for j in range(10):
                terrain = random.choice(terrain_choices)
                row.append(terrain)
            self.game_map.append(row)

        self.game_map[5][5] = "hero"

    def render_map(self):
        print(f'render_map() called')
        tile_size = 128
        map_width = tile_size * 10
        map_height = tile_size * 10

        map_image = Image.new("RGBA", (map_width, map_height))
        ImageDraw.Draw(map_image)

        for i, row in enumerate(self.game_map):
            for j, terrain in enumerate(row):
                icon_image = Image.open(icons[terrain])
                map_image.paste(icon_image, (j * tile_size, i * tile_size))

        map_image.save("map.png", "PNG")
        print(f'render_map() finished')

    def move_hero(self, direction):
        x, y = self.hero_position
        new_x, new_y = x, y

        if direction.lower() == "up":
            new_x -= 1
        elif direction.lower() == "down":
            new_x += 1
        elif direction.lower() == "left":
            new_y -= 1
        elif direction.lower() == "right":
            new_y += 1
        else:
            return "Invalid direction", False

        if new_x < 0 or new_x > 9 or new_y < 0 or new_y > 9:
            return "Invalid move", False

        self.game_map[x][y] = "grass"
        self.game_map[new_x][new_y] = "hero"
        self.hero_position = (new_x, new_y)

        # Decrease energy
        self.player.decrease_energy()

        if self.player.health <= 0:
            # End the game if health is depleted
            return "You have no health left. Game Over!", False

        return self.render_map(), True
