icons = {
    'health': '<:Health:1096466288081125406>',
    'energy': '<:Energy:1096482735465451591>',
    'Demon2': '<:Demon2:1102704473182310400>',
    'Vorlund': '<:Vorlund:1102704400557953087>',
    'Demon3': '<:Demon3:1102707791778566214>',
    'Locked': '<:Locked:1099641756645085184>',
    'Unlocked': '<:Unlocked:1099641805655523358>',
    'Enter': '<:Enter:1099592232102801469>',
    'Shield': '<:Shield:1096409320717029508>',
    'Stone': '<:Stone:1096462305757241425>',
    'Strength': '<:Strength:1097471663165149184>',
    'Tower': '<:Tower:1096354661822369802>',
    'Water': '<:Water:1096350127272230972>',
    'Wood': '<:Wood:1096456485074112562>',
    'WorldStage': '<:WorldStage:1097469806988505168>',
    'Dig': '<:Dig:1099426110795690155>',
    'Herbs': '<:Herbs:1097414618370019378>',
    'Hero': '<:Hero:1096366440136855572>',
    'Iron': '<:Iron:1097414116039204914>',
    'Leather': '<:Leather:1096742270008565801>',
    'Mountain': '<:Mountain:1096356006155517982>',
    'NPC': '<:NPC:1096375256316399656>',
    'Plateau': '<:Plateau:1096740594958737498>',
    'Potion': '<:Potion:1096436574255857695>',
    'Dexterity': '<:Dexterity:1097473506742116472>',
    'Energy': '<:Energy:1096482735465451591>',
    'Ether': '<:Ether:1097463624731213925>',
    'Fire': '<:Fire:1096347475079602206>',
    'Forest': '<:Forest:1096346247637499945>',
    'Gold': '<:Gold:1096516142652195017>',
    'Grass': '<:Grass:1096740548028665949>',
    'Health': '<:Health:1096466288081125406>',
    'Arrow': '<:Arrow:1097080604169867274>',
    'Bow': '<:Bow:1096409369383555152>',
    'Buff': '<:Buff:1097469879357034516>',
    'Camp': '<:Camp:1098896576589611068>',
    'Chop': '<:Chop:1099424386546683944>',
    'Club': '<:Club:1096410443037278281>',
    'Defense': '<:Defense:1097394054070808717>',
    'Demon': '<:Demon:1096696395697754182>'
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
        else:
            inventory_list = ""
            for item in self.inventory:
                              
                inventory_list += f"{icons[item]} • `{item}` • **4** \n"
        
        return inventory_list
