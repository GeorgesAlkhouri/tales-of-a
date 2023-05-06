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
    'Demon': '<:Demon:1096696395697754182>',
    'Demon4': '<:Demon4:1104429614836764792>',
    'Chest': '<:Chest:1104429086601908234>'
}



class Player:
    def __init__(self, health, energy, strength, dexterity, defense):
        self.health = health
        self.max_health = health
        self.energy = energy
        self.max_energy = energy
        self.strength = strength
        self.dexterity = dexterity
        self.defense = defense
        self.world_stage = 1
        self.inventory = {"Wood": 3, "Stone": 5, "Iron": 6, "Water": 6, "Herbs": 2}
        self.weapon = "Bow"
        self.max_weapon_durability = 10
        self.armor = ""
        self.traits = {"Lumberjack": 1, "Druid": 1, "Wanderer": 1}

    def decrease_energy(self):
        self.energy -= 1
        if self.energy <= 0:
            self.energy = 0
            self.decrease_health()

    def decrease_health(self):
        self.health -= 1
        if self.health <= 0:
            self.health = 0
    
    def regen_health(self):
        self_health = self.max_health
    
    def regen_energy(self):
        self_energy = self.max_energy

    def get_status(self):
        print(f"Health: {self.health} | Energy: {self.energy}")
        return f"**{self.health}/{self.max_health}** {icons['health']} Health /n**{self.energy}/{self.max_energy}** {icons['energy']} Energy"
    

    def get_inventory(self):
        if not self.inventory:
            inventory_list = "Your inventory is empty."
        else:
            inventory_list = ""
            for key, value in self.inventory.items():
                              
                inventory_list += f"{icons[key]} • `{key}` • **{value}** \n"
        
        return inventory_list
    
    def get_weapon(self):
        if not self.inventory:
            weapon_list = "You are unarmed."
        else:
            item = self.weapon
            max_weapon_durability = self.max_weapon_durability
            weapon_list = f"{icons[item]} • `{item}` • **10/{max_weapon_durability}** \n"
        
        return weapon_list
    
    def get_attributes(self):
        strength = self.strength
        defense = self.defense
        dexterity = self.dexterity
        world_stage = self.world_stage
        attributes_list = f"{icons['Strength']} • `Strength` • **{strength}** \n{icons['Defense']} • `Defense` • **{defense}** \n{icons['Dexterity']} • `Dexterity` • **{dexterity}** \n{icons['WorldStage']} • `World Stage` • **{world_stage}** \n"
        
        return attributes_list
    
    def get_constitution(self):
        health = self.health
        energy = self.energy
        max_health = self.max_health
        max_energy = self.max_energy
        constitution_list = f"{icons['Health']} • `Health` • **{health}/{max_health}** \n{icons['Energy']} • `Energy` • **{energy}/{max_energy}**"
        
        return constitution_list
        
    def get_traits(self):
        if not self.traits:
            traits_list = "You got no active traits."
        else:
            trait_list = ""
            for key, value in self.traits.items():
                              
                traits_list += f"{icons["Buff"]} • `{key}` • **{value}** \n"
        
        return traits_list
