icons = {
    "health": "<:Health:1096466288081125406>",
    "energy": "<:Energy:1096482735465451591>"
}


class Player:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        self.inventory = ["Sword", "Shield", "Potion"]

    def decrease_energy(self):
        self.energy -= 1
        if self.energy <= 0:
            self.energy = 0
            self.decrease_health()

    def decrease_health(self):
        self.health -= 1
        if self.health <= 0:
            self.health = 0

    def get_status(self):
        print(f"Health: {self.health} | Energy: {self.energy}")
        return f"{icons['health']} Health: {self.health} {icons['energy']} Energy: {self.energy}"

    def get_inventory(self):
        if not self.inventory:
            return "Your inventory is empty."
        
        inventory_str = "Your inventory contains:\n"
        for item in self.inventory:
            inventory_str += f"- {item}\n"
        
        return inventory_str