import random
import time

print(" _____      _            ")
print("/__   \__ _| | ___  ___  ")
print("  / /\/ _` | |/ _ \/ __| ")
print(" / / | (_| | |  __/\__ \ ")
print(" \/   \__,_|_|\___||___/ ")
print("                 _       ")
print("          __    \_/      ")
print("    ___  / _|   /_\      ")
print("   / _ \| |_   //_\\     ")
print("  | (_) |  _| /  _  \    ")
print("   \___/|_|   \_/ \_/    ")

# Define world stage and story stage
world_stage = 1
story_stage = 1

# tower
tower_hunter = 0
tower_alchemist = 0
tower_merchant = 0
tower_smith = 0
tower_occultist = 0

# Define the width and height of the map
width = 10
height = 10

# define stats
energy = 12
max_energy = 12
health = 12
max_health = 12
base_strength = 1
base_dex = 1
base_defense = 1
camp_bonus = 0
logging_bonus = 0
druid_bonus = 0
weapon = "none"

# define inventory
stone = 0
wood = 0
potion = 0
iron = 0
gold = 0
ether = 0
herbs = 0
water = 0
leather = 0
arrow = 0

# alchemy effects

ice_skin = False
reapers_rum = False

# define mining parameter
mining_rng = 0
mine_level = 0
chest_rng = 0

meals = {
    "apple": {"healthheal": 0, "energyheal": 1},
    "carrot": {"healthheal": 1, "energyheal": 0},
    "stew": {"healthheal": 1, "energyheal": 1},
    "dwarven ale": {"healthheal": 1, "energyheal": 2},
    "Honey Pot": {"healthheal": 0, "energyheal": 3},
    "Roastbeef": {"healthheal": 2, "energyheal": 1},
    "Bread": {"healthheal": 0, "energyheal": 3},
    "cheese": {"healthheal": 2, "energyheal": 0}
}

# define creatures
# habitat 0all 1mine 2forest
# droptype 0general 1forest 2mine
# special 0none 1thief 2

creatures = {
    "Filthy Rat": {"strength": 1, "defense": 1, "droprate": 1, "habitat": 0, "droptype": 0, "special": 0},
    "Giant Rat": {"strength": 3, "defense": 2, "droprate": 3, "habitat": 1, "droptype": 0, "special": 0},
    "Bat": {"strength": 1, "defense": 1, "droprate": 1, "habitat": 0, "droptype": 0, "special": 0},
    "Thorn-winged Bat": {"strength": 2, "defense": 1, "droprate": 2, "habitat": 0, "droptype": 0, "special": 0},
    "Knife Bug": {"strength": 3, "defense": 1, "droprate": 2, "habitat": 2, "droptype": 0, "special": 0},
    "Scaled Hornet": {"strength": 2, "defense": 3, "droprate": 3, "habitat": 2, "droptype": 0, "special": 0},
    "Spiked Centipede": {"strength": 2, "defense": 3, "droprate": 3, "habitat": 2, "droptype": 0, "special": 0},
    "Giant Centipede": {"strength": 4, "defense": 4, "droprate": 5, "habitat": 2, "droptype": 0, "special": 0},
    "Limbing Minecrawler": {"strength": 3, "defense": 3, "droprate": 3, "habitat": 1, "droptype": 0, "special": 0},
    "Angry Minecrawler": {"strength": 4, "defense": 4, "droprate": 5, "habitat": 1, "droptype": 0, "special": 0},
    "Blood Fly": {"strength": 2, "defense": 1, "droprate": 2, "habitat": 2, "droptype": 0.02, "special": 0},
    "Young Wyvern": {"strength": 6, "defense": 6, "droprate": 7, "habitat": 1, "droptype": 0, "special": 0},
    "Wolf": {"strength": 3, "defense": 3, "droprate": 4, "habitat": 2, "droptype": 0, "special": 0},
    "Black Wolf": {"strength": 4, "defense": 4, "droprate": 5, "habitat": 2, "droptype": 0, "special": 0},
    "Goblin Scout": {"strength": 2, "defense": 3, "droprate": 3, "habitat": 0, "droptype": 0, "special": 0},
    "Goblin Warrior": {"strength": 3, "defense": 3, "droprate": 3, "habitat": 1, "droptype": 0, "special": 0},
    "Goblin Warchief": {"strength": 5, "defense": 5, "droprate": 7, "habitat": 1, "droptype": 0, "special": 0},
    "Goblin Thief": {"strength": 2, "defense": 2, "droprate": 4, "habitat": 0, "droptype": 0, "special": 1},
    "Ghastly specter": {"strength": 6, "defense": 3, "droprate": 6, "habitat": 0, "droptype": 0, "special": 0},
    "Malicious wraith": {"strength": 7, "defense": 5, "droprate": 6, "habitat": 1, "droptype": 0, "special": 0},
    "Tree Sprite": {"strength": 2, "defense": 3, "droprate": 3, "habitat": 2, "droptype": 0, "special": 0},
    "Howling Branch Beast": {"strength": 5, "defense": 3, "droprate": 4, "habitat": 2, "droptype": 0, "special": 0},
    "Prowling Ogre": {"strength": 6, "defense": 8, "droprate": 7, "habitat": 2, "droptype": 0, "special": 0},
    "Skelleton Archer": {"strength": 2, "defense": 2, "droprate": 2, "habitat": 0, "droptype": 0, "special": 0},
    "Armoured Skelleton": {"strength": 3, "defense": 4, "droprate": 4, "habitat": 0, "droptype": 0, "special": 0},
    "Skelleton Warrior": {"strength": 4, "defense": 3, "droprate": 3, "habitat": 0, "droptype": 0, "special": 0},
    "Skelleton Scout": {"strength": 2, "defense": 3, "droprate": 2, "habitat": 0, "droptype": 0, "special": 0},
    "Skelleton Thief": {"strength": 2, "defense": 3, "droprate": 4, "habitat": 0, "droptype": 0, "special": 1},
    "Torture Ghoul": {"strength": 7, "defense": 1, "droprate": 6, "habitat": 2, "droptype": 0, "special": 0},
    "Cave Troll": {"strength": 7, "defense": 8, "droprate": 2, "habitat": 1, "droptype": 0, "special": 0},
    "Dark Spirit": {"strength": 6, "defense": 3, "droprate": 5, "habitat": 2, "droptype": 0, "special": 0}
}

# Define Creature Rarity
creature_rarity = {
    "Filthy Rat": 0.05,
    "Giant Rat": 0.02,
    "Bat": 0.05,
    "Thorn-winged Bat": 0.03,
    "Knife Bug": 0.02,
    "Scaled Hornet": 0.03,
    "Spiked Centipede": 0.03,
    "Giant Centipede": 0.01,
    "Limbing Minecrawler": 0.01,
    "Angry Minecrawler": 0.02,
    "Blood Fly": 0.02,
    "Young Wyvern": 0.01,
    "Wolf": 0.04,
    "Black Wolf": 0.02,
    "Goblin Scout": 0.04,
    "Goblin Warrior": 0.03,
    "Goblin Warchief": 0.01,
    "Goblin Thief": 0.02,
    "Ghastly specter": 0.01,
    "Malicious wraith": 0.01,
    "Tree Sprite": 0.04,
    "Howling Branch Beast": 0.01,
    "Prowling Ogre": 0.01,
    "Skelleton Archer": 0.02,
    "Armoured Skelleton": 0.01,
    "Skelleton Warrior": 0.02,
    "Skelleton Scout": 0.01,
    "Skelleton Thief": 0.02,
    "Torture Ghoul": 0.01,
    "Cave Troll": 0.01,
    "Dark Spirit": 0.01
}

# Define the characters that will be used to represent different map features
tiles = {
    "plateau": "🗻",
    "grass": "🌿",
    "water": "💧",
    "mountain": "🌋",
    "forest": "🌲",
    "npc": "👤",
    "building": "🏠",
    "demon": "🐉"
}

# Define the probability of each tile type appearing
probabilities = {
    "plateau": 0.12,
    "grass": 0.18,
    "water": 0.07,
    "mountain": 0.33,
    "forest": 0.3,
    "npc": 0,
    "building": 0,
    "demon": 0
}

# Generate the map
npc_x = random.randint(0, width - 1)
npc_y = random.randint(0, height - 1)
map_data = [[None for y in range(height)] for x in range(width)]
for x in range(width):
    for y in range(height):
        tile_type = random.choices(list(tiles.keys()), weights=list(probabilities.values()))[0]
        map_data[x][y] = tiles[tile_type]
        if x == npc_x and y == npc_y:
            map_data[x][y] = tiles["npc"]

# Define the player character's starting position
player_x = random.randint(0, width - 1)
player_y = random.randint(0, height - 1)

# Define a dictionary that maps commands to their corresponding movement vectors
movement_vectors = {
    "up": (0, -1),
    "down": (0, 1),
    "right": (1, 0),
    "left": (-1, 0),
    "w": (0, -1),
    "s": (0, 1),
    "d": (1, 0),
    "a": (-1, 0)
}

print("")

print("")

print("Choose your starter class!")

print()

print("")
print("•TANK•")
print("-high defense and health")
print("•MERCHANT•")
print("-starts with filled inventory")
print("•LUMBERJACK•")
print("-fast and efficient logging")
print("•DRUID•")
print("-restores at springs")
print("•WANDERER•")
print("-high energy and good camper")
print("•DEPRIVED•")
print("-no starter gifts and skills")
print("")
while True:

    user_input = input("")
    user_input = user_input.lower()
    print("")
    if user_input == "tank":
        print("")
        base_defense += 1
        max_health += 4
        health += 4
        break
    elif user_input == "merchant":
        print("")
        wood = 6
        stone = 10
        gold = 5
        iron = 3
        herbs = 5
        water = 3
        potion = 5
        break
    elif user_input == "lumberjack":
        print("")
        wood += 15
        logging_bonus += 2
        break
    elif user_input == "druid":
        print("")
        druid_bonus += 1
        herbs = 5
        break
    elif user_input == "wanderer":
        print("")
        max_energy += 5
        energy += 5
        camp_bonus = 1
        break
    elif user_input == "deprived":
        break

    else:
        print("Invalid Input!")


# Define a function that moves the player character and updates the map
def move_player(dx, dy):
    global player_x, player_y, energy
    new_x = player_x + dx
    new_y = player_y + dy

    if new_x >= 0 and new_x < width and new_y >= 0 and new_y < height:
        player_x = new_x
        player_y = new_y
        energy -= 1
        print_map()


# camp command
def camp():
    global wood, health, energy
    if wood >= world_stage + 2:
        # remove grass from map
        map_data[player_x][player_y] = tiles["plateau"]
        wood -= world_stage + 2
        energy += 8 + world_stage + camp_bonus
        health += 2 + world_stage + camp_bonus
        if energy >= max_energy:
            energy = max_energy
        if health >= max_health:
            health = max_health

        print(
            f"You use {world_stage + 2} WOOD to build a temporary shelter. You restored {camp_bonus + 7 + world_stage} ENERGY and {camp_bonus + 2 + world_stage} HEALTH.")
    else:

        print(f"You don't have enough WOOD in your inventory to build a temporary shelter! ({wood}/{world_stage + 2}) ")


# chest event
def chest():
    global water, herbs, energy, stone, health, gold, potion, iron, max_health, ether, wood, max_energy, leather, arrow
    chest_rng = random.randint(2 + world_stage, 10 * world_stage / 2)
    if chest_rng >= world_stage * 10 / 2:
        max_health += 1
    print("You find a tressure chest.")
    print("It contains:")
    print(f"{chest_rng} GOLD")
    gold += chest_rng
    if chest_rng % 2 == 0:
        print(f"{world_stage * 2 + 1} IRON")
        iron += world_stage * 2 + 1
    else:
        print(f"{world_stage * 2} WOOD")
        wood += world_stage * 2 + 4
        print("1 LEATHER")
        leather += 1
    if weapon == "bow":
        numberofarrows = random.randint(2, 6 + world_stage)
        print(f"{numberofarrows} ARROWS")
        arrow += numberofarrows

    print(f"{world_stage} POTION")
    potion += world_stage
    if chest_rng >= world_stage * 10 / 2:
        print("LIFE RING (Max HEALTH +1)")


# death event
def death():
    global max_energy, max_health, health, energy, gold
    print("THE REAPER:")
    print(
        "Oh Å, how tragic to see you are on the brink of death. But fear not, for I have an offer for you. I can grant you a second chance at life, but in return, you must make a pact with me!")

    if reapersrum == True:
        reapersrum = False
        "Reapers Rum Safe Text"
    else:

        max_health -= 1
        if max_energy >= 8:
            max_energy -= 1
            energy = max_energy
            print("Max ENERGY - 1")

        if max_health >= 8:
            max_health -= 1
            health = max_health
            print("Max HEALTH - 1")

        if gold >= 1:
            print("THE REAPER:")
            print("'Take better care! And let me take care of your GOLD!'")
            print(f"GOLD - {gold}")
            gold = 0


# define the tower function
def tower():
    global tower_alchemist, tower_hunter, tower_necromancer, tower_smith, gold, herbs, water, potion, story_stage

    if story_stage == 4:
        print("VORLUND:")
        print("much proud")
        story_stage + 1

    # tower information
    print("TOWER")
    print("-------------------")
    print("Hunter Level:")
    print("Alchemist Level: {tow}")
    print("Occultist Level:")
    print("Trader Level:")

    while True:

        user_input = input("What do you want to do? (hunter, alchemist, occultist, trader, leave)")
        user_input = user_input.lower()
        if user_input == "trader":
            print("not available yet")

        if user_input == "occultist":
            print("not available yet")

        elif user_input == "hunter":
            hunterintower()

        elif user_input == "alchemist":
            alchemy()

        elif user_input == "leave":
            print("You leave the Tower.")
            break
        else:
            print("Invalid Input!")


def alchemy():
    global tower_alchemist

    if tower_alchemist == 0:
        print("You haven't found an Alchemist yet.")
    elif tower_alchemist == 1:
        print("LYSANDRIA:")
        print(
            "'I apologize for the state of my workshop, it's not as tidy as I would like it to be. Please don't let the mess deter you from my knowledge and expertise in alchemy.")

        print(
            "I must confess that my resources are limited, and if only I had more leather and iron, I could improve my workshop and craft even more potent potions - like the one VORLUND is looking for.''")
        tower_alchemist += 1
    if tower_alchemist >= 2:
        while True:
            print("What do you want to do?")
            user_input = input("upgrade/brew/leave")
            user_input = user_input.lower()
            if user_input == "brew":
                brew()


            elif user_input == "leave":
                print("You leave Lysandria's Workshop.")
                break
            elif user_input == "upgrade":

                if tower_alchemist == 2:
                    # INPROGRESS
                    print("LYSANDRIA:")
                    print("To upgrade the workshop, we will need the following:")
                    print("")
                    print(f"10 🧱 STONE - {stone}/10")
                    print(f"4 🪵 WOOD - {wood}/4")
                    print(f"3 ⛓ IRON - {iron}/3")
                    print(f"3 🟫 LEATHER - {leather}/3")
                    print("")
                    print("LYSANDRIA:")

                    if stone >= 10 and wood >= 4 and iron >= 3 and leather >= 3:

                        print("'Terrific, you gathered all we need to improve the workshop!'")
                        stone -= 10
                        wood -= 4
                        iron -= 3
                        leather -= 3
                        tower_alchemist += 1

                    else:

                        print("'Come back, when you have found all the materials, we need!'")
                    break

            else:
                print("Invalid Input!")


def setdemon(demontype):
    if demontype == 0:
        print("")

    while True:
        y = random.randint(2, 9)
        x = random.randint(2, 9)

        if x != player_x or y != player_y:
            if map_data[x][y] != tiles["building"]:
                map_data[x][y] = tiles["demon"]
                break


def brew():
    global tower_alchemist, gold, herbs, water, potion, iron, ether, max_energy, max_energy

    if tower_alchemist >= 2:
        print("What do you want to brew?")
        print("----------")
        print("•POTION•")
        print(f"{world_stage + 4} HERBS, 1 WATER")
        print("Restores HEALTH and ENERGY (item)")
        print("----------")
        print("•ENERGY-RING•")
        print(f"{2 + world_stage} POTION, {3 + world_stage * 2} ETHER")
        print("Raises Max ENERGY by 1 (buff)")
        print("----------")
        print("•LIFE-RING•")
        print(f"{2 + world_stage} POTION, {max_health} IRON")
        print("Raises Max HEALTH by 1 (buff)")
        print("----------")
        if tower_alchemist >= 3:
            print("•REAPERS-RUM•")
            print(f"{2 + world_stage} POTION, {max_health - 7} ETHER")
            print("A way to bribe death (status effect)")
            print("----------")
            print("•ICE-SKIN•")
            print(f"{2} POTION, {20} STONE")
            print("A way to resist fire (status effect)")
            print("----------")
        print("(or leave)")
        while True:
            user_input = input("")
            user_input = user_input.lower()
            nums = user_input.split()
            if len(nums) == 2:
                brewitem, brewamount = user_input.split()
                try:
                    int(brewamount)
                except ValueError:
                    brewamount = 1

            else:
                brewamount = 1
            brewamount = int(brewamount)
            if brewamount <= 0:
                print("Amount must be at least 1.")
                user_input = "invalid"
                brewitem = "invalid"

            if user_input == "potion" or brewitem == "potion":
                if herbs >= brewamount * world_stage + 4 * brewamount and water >= brewamount * 1:
                    herbs -= brewamount * world_stage + 5 * brewamount
                    water -= brewamount * 1
                    potion += brewamount
                    print(f"{brewamount} POTION successfully brewed!")
                else:
                    print("You are lacking ingredients!")
                    print(f"HERBS {herbs}/{brewamount * world_stage + 4 * brewamount}")
                    print(f"WATER {water}/{1 * brewamount}")

                break
            elif user_input == "energy-ring" or brewitem == "energy-ring":

                if potion >= (2 + world_stage) * brewamount and ether >= (3 + world_stage * 2) * brewamount:
                    potion -= (2 + world_stage) * brewamount
                    ether -= (3 + world_stage * 2) * brewamount
                    max_energy += 1 * brewamount
                    print(f"{brewamount} ENERGY-RING successfully crafted!")
                else:
                    print("You are lacking ingredients!")
                    print(f"POTION {potion}/{(2 + world_stage) * brewamount}")
                    print(f"ETHER {ether}/{(3 + world_stage * 2) * brewamount}")

                break
            elif user_input == "life-ring" or brewitem == "life-ring":
                count = -1
                addcost = 0
                while True:
                    count += 1
                    addcost += count
                    if brewamount - 1 == count:
                        break
                if potion >= (2 + world_stage) * brewamount and iron >= max_health * brewamount + addcost:
                    potion -= (2 + world_stage) * brewamount
                    iron -= (max_health * brewamount) + addcost
                    max_life += 1 * brewamount
                    print(f"{brewamount} LIFE-RING successfully crafted!")
                else:
                    print("You are lacking ingredients!")
                    print(f"POTION {potion}/{(2 + world_stage) * brewamount}")
                    print(f"IRON {iron}/{max_health * brewamount + addcost}")
                break
            elif user_input == "leave":
                break
            else:
                print("Invalid Input!")


def drink_potion():
    global potion, health, energy
    if potion >= 1:
        potion -= 1
        energy += 5
        health += 7
        if energy >= max_energy:
            energy = max_energy
        if health >= max_health:
            health = max_health

        print(f"You drink 1 POTION and restore 5 ENERGY and 7 HEALTH.")
    else:

        print("You don't have a POTION in your INVENTORY!")


# Define a fight function
def fight(location):
    global water, herbs, energy, stone, health, potion, gold, iron, max_health, ether, wood, max_energy, arrow

    while True:
        creature = random.choices(list(creatures.keys()), weights=list(creature_rarity.values()))[0]

        creature_stats = creatures[creature]
        droptype = creature_stats["droptype"]
        if creature_stats["habitat"] == location or creature_stats["habitat"] == 0:
            break

    print(f"You are being attacked by a {creature}!")
    print("Strength: " + str(creature_stats["strength"]))
    print("Defense: " + str(creature_stats["defense"]))
    print("Loot Rarity: " + str(creature_stats["droprate"]))
    creature_shield = creature_stats["defense"]
    energyloss = 1

    while True:
        action = "none"
        actionamount = "none"
        user_input = input(f"(combat/range/run)")
        user_input = user_input.lower()
        nums = user_input.split()
        if len(nums) == 2:
            action, actionamount = user_input.split()
            try:
                int(actionamount)
            except ValueError:
                actionamount = 1

        else:
            actionamount = 1
        actionamount = int(actionamount)
        if actionamount <= 0:
            print("Amount must be at least 1.")
            user_input = "invalid"
            action = "invalid"

        if user_input == "range" or action == "range":
            if weapon == "bow":
                projectile = "ARROW"
                weaponrangebonus = 1 + base_dex
            else:
                projectile = "STONE"
                weaponrangebonus = 0

            if weapon == "bow" and arrow >= actionamount or weapon != "bow" and stone >= actionamount:

                while True:
                    actionamount -= 1
                    energyloss += 1
                    arrow_rng = random.randint(0, 2 + weaponrangebonus)
                    if arrow_rng == 0:
                        print(f"Your {projectile} misses the {creature}.")
                        if weapon == "bow":
                            print("ARROW - 1")
                            arrow -= 1
                        if weapon != "bow":
                            print("STONE - 1")
                            stone -= 1
                    else:
                        arrow_effect = random.randint(1, 1 + weaponrangebonus)
                        print(f"Your {projectile} hits the {creature} and decreases its DEFENSE by {arrow_effect}.")
                        if weapon == "bow":
                            print("ARROW - 1")
                            arrow -= 1
                        if weapon != "bow":
                            print("STONE - 1")
                            stone -= 1
                        creature_shield -= 1
                    if actionamount == 0:
                        break
            else:

                print(f"You don't have enough {projectile}.")




        elif user_input == "combat":

            if base_strength >= creature_shield:
                creature_strength = creature_stats["strength"]
                lifeloss_max = world_stage + creature_strength - base_defense
                if lifeloss_max <= 1:
                    lifeloss_max = 2
                lifeloss = random.randint(1, lifeloss_max)

                health -= lifeloss
                energy -= energyloss

                if creature_stats["special"] == 1:
                    print(
                        f"You defeat the {creature}, but lose {lifeloss} HEALTH, {energyloss} ENERGY and {world_stage} GOLD.")
                    gold -= world_stage
                    if gold <= 0:
                        gold = 0
                else:
                    print(f"You defeat the {creature}, but lose {lifeloss} HEALTH and {energyloss} ENERGY.")
                droprate = creature_stats["droprate"]
                loot_drop(droprate, droptype)
                break
            else:
                print(
                    f"The {creature}'s DEFENSE ({creature_shield}) is higher than your STRENGTH ({base_strength}). You need to weaken it first!")


        elif user_input == "run":

            run_rng = random.randint(1, 2)
            energy -= run_rng
            print(f"You are able to outrun the {creature}. ENERGY - {run_rng}!")
            break

        else:
            print("Invalid Input!")


# Loot Drop Function
def loot_drop(droprate, droptype):
    global wood, stone, iron, gold, ether, potion, leather, arrow

    droprate += random.randint(world_stage, 2 * world_stage + tower_occultist)

    while True:
        if droprate >= 12:
            print(f"ETHER + {world_stage}")
            ether += world_stage
            droprate /= 2
        elif droprate >= 10:
            print(f"GOLD + {world_stage * 2 + 2}")
            gold += world_stage * 2 + 2
            droprate -= 4
        elif droprate >= 7:
            print(f"IRON + {world_stage * 2}")
            iron += world_stage * 2
            droprate -= 4
        elif droprate >= 4:
            print(f"POTION + 1")
            potion += 1
            droprate -= 2
            if weapon == "bow" and player_x % 2 != 0:
                numberofarrows = random.randint(2, 2 + world_stage)
                arrow += numberofarrows
                print(f"ARROW + {numberofarrows}")
                droprate -= 1
        elif droprate >= 2:
            droprate -= 2
            if droptype == 1:
                print(f"STONE + {world_stage + 2}")
                stone += world_stage + 2
            else:
                print(f"LEATHER + {world_stage}")
                leather += world_stage
        else:
            droprate = 0
            if droptype == 2:
                print(f"WOOD + {world_stage + 1}")
                wood += world_stage + 1
            else:
                print(f"STONE + {world_stage + 1}")
                stone += world_stage + 1
            break


def wanderer():
    global water, herbs, mining_rng, logging_bonus, arrow
    creature = random.choice(list(creatures.keys()))
    print("WANDERER:")
    print(
        f"'Excuse me, do you have any water to spare? I'm in dire need. I've been attacked by a {creature} and left all my belongings behind...'")
    while True:
        user_input = input("(give/decline)")
        user_input = user_input.lower()
        if user_input == "give":
            if water >= 1:
                water -= 1
                mining_rng = random.randint(0, 3)
                if weapon == bow and mining_rng == 2:
                    print("WANDERER:")
                    print(
                        "'This is a lifesaver. You're a true hero - I can give you nothing but this quiver of ARROWS. I won't need them, since I left my bow behind...' ")
                    print("ARROW + 10")
                    arrow += 10
                elif logging_bonus <= world_stage and mining_rng == 3:
                    print("WANDERER:")
                    print(
                        "'This is a lifesaver. You're a true hero - Let me sharpen your tools in return for your generosity!' ")
                    print("LOGGING + 1")
                    logging_bonus += 1
                else:
                    print("WANDERER:")
                    print("'This is a lifesaver. You're a true hero - take this a sign of my gratefulness...'")
                    print(f"WANDERER gives you {1 + druid_bonus + world_stage} HERBS ")
                    herbs += 1 + druid_bonus + world_stage
            else:
                print("You got no water in your inventory.")
            break
        elif user_input == "decline":
            print("WANDERER:")
            print("'I see. Farewell then, stingy gnome!'")
            break


        else:
            print("Invalid Input")


def occultist():
    global tower_occultist, max_energy, max_health, gold, energy, health, ether, reapers_rum
    print("much occult")
    if tower_occultist == 0:
        print(
            "As you wander through the dense darkness, you come across the decaying remains of a large animal. You can't help but wonder what kind of creature it once was, and what caused its demise. As you investigate further, you notice something  circling the area, ready to make a meal out of the carcass.")

        while True:
            user_input = input("(range/approach)")
            user_input = user_input.lower()
            if user_input == "range":
                print(
                    "The scavenger flees and you discover the rotting corpse of a deer. It is surrounded by a faint blue light, but as you try to investigate further, the light faints. Laying in front of the remains you find an ornament of GOLD coins.")
                print("GOLD + 8")
                gold += 8
                tower_occultist += 1
                break
            elif user_input == "approach":
                print(
                    "What looked like a scavenger from afar, turns out to be a hooded man, engrossed in some kind of ritual. When he catches sight of you, you hear a deep, sacred voice murmuring incantations in foreign tongues in your direction. You suddenly feel weak and in a moment of carelessness, he flees the scene.")
                print("Max ENERGY - 1")
                max_energy -= 1
                tower_occultist += 1
                break
            else:
                print("Invalid Input")
            energy -= 1
    elif tower_occultist == 1:

        print(f"You find the skelletal remains of a mine worker.")
        energy -= 1
        while True:
            user_input = input("(examine/pray)")
            user_input = user_input.lower()
            if user_input == "examine":
                print(
                    "As you look at the skelleton, you find small, tangled carvings covering the bones. When suddenly a shadow flits by.")
                tower_occultist += 1
                break
            elif user_input == "pray":
                print(
                    "As you pray for the soul of the miner, you can hear faint whispers echoing from the tunnel's humid walls.")
                tower_occultist += 1
                break
            else:
                print("Invalid Input!")
            print("A DEEP, SACRED VOICE:")
            print(
                "Once more I see you stumbling upon my rituals. I must caution you that this is a sacred practice, not to be interrupted. Take this and leave!")
            print("ETHER + 1")
            ether += 1

    elif tower_occultist == 2:
        print(
            "As you move forward cautiously, a glowing mist rises from the ground, swirling around you in a spiral pattern. The mist takes shape and reveals a sinister figure with glowing eyes, holding a staff that emits an otherworldly aura. The figure speaks with a deep, sacred voice - commanding you to kneel.")
        energy -= 1
        while True:
            user_input = input("(kneel/refuse)")
            user_input = user_input.lower()
            if user_input == "kneel":
                break
                print("A DEEP, SACRED VOICE:")
                print(
                    "'You have proven yourselves worthy! May you use the artifact wisely, and with the knowledge that great power brings great responsibility.'")
                print("REAPER'S RUM granted!")
                reapers_rum = True
            if user_input == "refuse":
                break
                print(
                    "You feel an intense pain spreading out in your bones. Forcing you to kneel and close your eyes. As you open your eyes again, the mist and the figure are gone - leaving nothing a small glowing object.")
                print("ETHER + 1")
                print("HEALTH - 1")
                ether += 1
                health -= 1

            else:
                print("Invalid Input!")
        tower_occultist += 1


    elif tower_occultist == 3:
        print("occultist 4")
        tower_occultist += 1

    elif tower_occultist == 4:
        print("occultist 5")
        tower_occultist += 1


def hunter():
    global gold, tower_hunter, base_dex, max_energy, max_health, base_defense

    if tower_hunter == 0:
        print("SYLVARIS:")
        print(
            "Greetings! What a rare sight... Not often do strangers cross these lands. My name is SYLVARIS, the hunter.")

    if tower_hunter <= 3:
        print("SYLVARIS:")
        if tower_hunter <= 3:
            while True:
                user_input = input(
                    f"'You look like you need some guidance! {tower_hunter + 1} GOLD for some helpful information?(agree/decline)")
                user_input = user_input.lower()
                if user_input == "agree":
                    if gold >= tower_hunter + 1:
                        print(f"You give the HUNTER {tower_hunter + 1} GOLD.")
                        gold -= tower_hunter + 1
                        print("SYLVARIS:")
                        if tower_hunter == 0:
                            print(
                                "'Listen well!  If you seek to hunt in these lands, you must remember to never go after prey that is too strong for you. It is a foolish mistake that will cost you dearly. Take your time, build your strength, and hone your skills before attempting such a feat. When you go on explorations, always make sure you have enough health. You never know what dangers may lie ahead...'")
                            print("Max ENERGY + 1")
                            max_energy += 1
                            tower_hunter += 1
                        elif tower_hunter == 1:
                            print(
                                "Some enemies must be weakened with arrows before you try to strike a hit in close combat. When shooting a bow, stand perpendicular to the target and hold the bow with your non-dominant hand. Grip the bowstring with your dominant hand and draw it back until you anchor it against your face. Then, aim with your dominant eye and release the string to shoot the arrow. ")
                            print("DEXTERITY + 1")
                            base_dex += 1
                            tower_hunter += 1
                        elif tower_hunter == 2:
                            print(
                                "'In hunting and archery, efficient movement through difficult terrain is crucial for success. It takes strength, agility, and balance to navigate forests, hills, and rocks quietly and quickly. Skill in archery is important, but being able to move like a predator in the wild is essential for a skilled hunter.'")
                            print("MAX ENERGY + 1")
                            max_energy += 1
                            tower_hunter += 1
                        elif tower_hunter == 3:
                            print("Text4")
                            max_health += 1
                            tower_hunter += 1

                    else:
                        print("SYLVARIS:")
                        print(''"Not enough GOLD?! That's a shame...'")
                    break
                if user_input == "decline":
                    print("SYLVARIS:")
                    print("'Farewell then!'")
                    break



    elif tower_hunter == 4:
        print(
            "My young friend, you have come a long way. I have taught you all I can, and I am proud of the hunter you have become. But there is still much to learn, and I offer my services to you once more. If you need me, I will be at your side. I will move to the tower!")
        tower_hunter += 1
    else:
        fight(0)


def hunterintower():
    if tower_hunter <= 4:
        print("You haven't found a Hunter yet.")


def food():
    global health, energy
    meal = random.choice(list(meals.keys()))
    mealeffect = meals[meal]
    meal = meal.upper()
    healthgain = mealeffect["healthheal"]
    energygain = mealeffect["energyheal"]
    print(f"{meal} ")
    if healthgain != 0:
        print(f"HEALTH + {healthgain}")
        health += healthgain
        if health > max_health:
            health = max_health
    if energygain != 0:
        print(f"ENERGY + {energygain}")
        energy += energygain
        if energy > max_energy:
            energy = max_energy


def hike():
    global water, herbs, energy, stone, health, gold, iron, max_health, ether, wood, max_energy

    mine_level = random.randint(0 + world_stage, 4 + world_stage)
    print(f"You find a LEVEL {mine_level} FOREST.")

    # remove mine from map
    map_data[player_x][player_y] = tiles["grass"]

    while True:
        user_input = input("What do you want to do?(explore/chop/leave)")
        user_input = user_input.lower()
        if user_input == "leave" or user_input == "chop" or user_input == "explore" or user_input == "x":
            break
        else:
            print("Invalid command!")

    # explore table
    if user_input == "explore" or user_input == "x":
        mining_rng = random.randint(0 + mine_level, 12)
        if mining_rng <= 3:
            energy -= 1
            print("The forest is all dry and dead. You grab a small stack of wood before leaving.")
            print(f"WOOD + {world_stage + logging_bonus}")
            wood += world_stage + logging_bonus

        if mining_rng == 4:
            energy -= 1
            food()

        if mining_rng == 5:
            energy -= 1
            wood += 1 + world_stage + logging_bonus
            print(f"On your walk through the calm forest you pickup {2 + world_stage + logging_bonus} WOOD.")

        if mining_rng == 6:
            herbs += 1 + world_stage + druid_bonus
            energy -= 1
            print(f"You find {1 + druid_bonus + world_stage} HERBS on a clearing.")
            if player_x % 2 == 0:
                print("The fresh air there also restores some of your ENERGY.")
                print(f"ENERGY + {world_stage + logging_bonus - 1}")
                energy += world_stage + logging_bonus

        if mining_rng == 7:
            energy -= 1
            wanderer()

        if mining_rng == 8:
            water += world_stage
            energy = max_energy

            print(f"You find a magic creek and gather {world_stage} water and restore your energy. ")

        if mining_rng == 9:
            energy -= 1
            hunter()

        if mining_rng == 10:
            energy -= 1
            chest()

        if mining_rng == 11:
            fight(2)

        if mining_rng == 12:
            if player_x % 2 == 0:
                if player_y % 2 == 0:
                    occultist()




            else:
                fight(2)

    if user_input == "chop":

        # check for logging_bonus
        energy_payback = random.randint(0, 4)
        if energy_payback < logging_bonus:
            print("Due to your logging experience it consumed no ENERGY to chop.")
        else:
            energy -= 1

        mining_rng = random.randint(int(world_stage + mine_level / 2), mine_level + world_stage)
        print(f"You gathered {mining_rng + logging_bonus} WOOD.")
        wood += mining_rng + logging_bonus

        if mining_rng >= mine_level + world_stage * 0.9:
            if player_x % 2 == 1:
                print(f"You also find {world_stage} HERBS on the tree trunk!")
                herbs += world_stage
            else:
                if ether <= 2:
                    print(f"Hidden in the bark, you also find {world_stage} ETHER!")
                    ether += world_stage

    if user_input == "leave":
        energy -= 1
        print("You back track to the forest's entrance...")

        map_data[player_x][player_y] = tiles["forest"]


# Define a function for the mine event
def mine():
    global water, herbs, energy, stone, health, gold, iron, max_health, ether, potion

    mine_level = random.randint(0 + world_stage, 4 + world_stage)
    print(f"You found a LEVEL {mine_level} MINE.")

    # remove mine from map
    map_data[player_x][player_y] = tiles["plateau"]

    # Get the user's input
    while True:
        user_input = input("What do you want to do?(explore/dig/leave)")
        user_input = user_input.lower()
        if user_input == "leave" or user_input == "dig" or user_input == "explore" or user_input == "x":
            break
        else:
            print("Invalid command!")

    # explore table
    if user_input == "explore" or user_input == "x":
        mining_rng = random.randint(0 + mine_level, 12)
        if mining_rng < 5:
            energy -= 1

            print("The mine is abandoned and empty.")

        if mining_rng == 5:
            iron += 1
            energy -= 1

            print(f"You find an ore vein and gather 1 IRON .")

        if mining_rng == 6:
            herbs += 2 + world_stage
            energy -= 1

            print(f"You find {2 + world_stage} HERBS on the cavern walls.")

        if mining_rng == 7:
            water += world_stage
            energy = max_energy

            print(
                f"You find a magic spring deep inside the mountain. You gather {world_stage} water and restore your energy. ")

        if mining_rng == 8:
            stone += world_stage * 3
            energy -= 1
            lifeloss = int(mine_level / 2)
            lifeloss = lifeloss.round()
            health -= lifeloss

            print(
                f"You are being surprised by a rockfall. You lose {lifeloss} HEALTH, but also gather {world_stage * 3} STONE.")

        if mining_rng == 9:
            occultist()

        if mining_rng == 10:
            energy -= 1
            chest()

        if mining_rng == 11 or mining_rng == 12:
            fight(1)

    if user_input == "dig":
        energy -= 1

        mining_rng = random.randint(world_stage, mine_level + world_stage)
        print(f"You gathered {mining_rng} STONE.")
        print("------------")

        stone += mining_rng
        if mining_rng >= mine_level + world_stage * 0.9 and ether == 0:
            print(f"Hidden in the rubble, you also find {world_stage} ETHER!")
            ether += world_stage
            print("------------")

    if user_input == "leave":
        energy -= 1

        print("You ascend back to the day light...")
        map_data[player_x][player_y] = tiles["mountain"]


def npc():
    global story_stage, potion, tower_alchemist
    if story_stage == 1:
        print("Vorlund:")
        print(
            "'Greetings adventurer, I am Vorlund, a wizard who has been searching for someone with the courage and skill to complete a most important task. I have been seeking a hero who can construct a tower, unlike any other in the land. This tower serves a unique purpose - it will house a portal that I will create, leading to a new and unexplored realm. However, only a skilled builder can construct this tower, and I have chosen you for this task. Are you ready to embark on this great adventure, Å? Well then, take these plans!'")

        print("To build a basic tower you need:")
        print("--------")
        print(f"22 🧱 STONE - {stone}/22")
        print(f"12 🪵 WOOD - {wood}/12")
        print(f"5 ⛓ IRON - {iron}/5")
        print(f"3 🟫 LEATHER - {leather}/3")
        print(f"1 🪬 ETHER - {ether}/1")

        while True:
            y = random.randint(2, 9)
            x = random.randint(2, 9)
            if x != player_x or y != player_y:
                if map_data[x][y] != tiles["building"]:
                    map_data[x][y] = tiles["npc"]
                    break
        map_data[player_x][player_y] = tiles["forest"]

        story_stage += 1
    elif story_stage == 2:
        print("An old woman is picking herbs and whispering indistinct sounds. She doesn't respond to you.")
    elif story_stage == 3:
        print("LYSANDRIA:")
        print(
            "'Welcome, adventurer! I am LYSANDRIA, the alchemist - always looking out for rare HERBS and mystical ingredients. I can create potions to heal your wounds, enhance your strength and dexterity, and even grant you temporary immortality. My knowledge of alchemy is as deep as the ocean and dark as the night. Whatever your needs may be, I am confident, I can assist you.'")

        while True:
            user_input = input("(agree/decline)")
            user_input = user_input.lower()
            if user_input == "agree":

                map_data[player_x][player_y] = tiles["forest"]

                print("LYSANDRIA:")
                print("'Very well! I will move to the tower and prepare my workshop.'")
                story_stage += 1
                tower_alchemist += 1
                break

            elif user_input == "decline":

                map_data[player_x][player_y] = tiles["forest"]

                print("LYSANDRIA:")
                print("'It looks like you need taste of what I'm capable of...'")
                print("You receive 3 POTIONs!")
                potion += 3
                print("LYSANDRIA:")
                print("'Glad that you changed your mind...")
                print("I will move to the tower and prepare my workshop there!'")
                story_stage += 1  # liegt danach bei 4
                tower_alchemist += 1
                break


            else:
                print("Invalid Input!")


# Define a function that prints the map and the player character's position
def spring():
    global water, energy
    mining_rng = random.randint(0, 10)
    if mining_rng <= 8:
        print(f"You find a spring and collect {world_stage} WATER!")
        water += 1
        if druid_bonus >= 1:
            energy = max_energy
            print("Due to the wisdom of the druid, you restore your ENERGY.")
        map_data[player_x][player_y] = tiles["grass"]
    elif mining_rng >= 9:
        print(
            "You wade through muddy, shallow swamp. As you peer along the troubled water reflecting the dim sunlight you see dark shapes darting back and forth beneath some tangled roots.")
        while True:
            user_input = input("(approach/leave)")
            user_input = user_input.lower()

            if user_input == "approach":
                eel()
                break


            elif user_input == "leave":
                print("")
                print("After a long exhausting walk you finally reach the swamps outskirts. (ENERGY-2)")
                energy -= 2
                break
            else:
                print("Invalid Input!")


def eel():
    global base_strength, energy, health
    if base_strength <= world_stage:
        print(
            "As you approach you see a swarm of Sword Eels fleeing - revealing a light-floated artifact. The occult might of the object regenerates and heals your body and grants you STRENGTH.")
        print("STRENGTH + 1")
        energy = max_energy
        health = max_health
        base_strength += 1
    else:
        print("As you approach, something sneaks up from behind...")
        fight(0)


def print_map():
    global energy, health
    forest_count = 0
    mountain_count = 0
    water_count = 0
    for y in range(height):
        for x in range(width):
            if x == player_x and y == player_y:
                print(pad_emoji("🧝🏽"), end="")
            else:
                print(pad_emoji(map_data[x][y]), end="")
                if map_data[x][y] == tiles["forest"]:
                    forest_count += 1
                if map_data[x][y] == tiles["mountain"]:
                    mountain_count += 1
                if map_data[x][y] == tiles["water"]:
                    water_count += 1

        print()
    current_tile = map_data[player_x][player_y]
    for current_tile_name, value in tiles.items():
        if value == current_tile:
            break

    time.sleep(0.3)
    if energy < 0:
        print("You run out of ENERGY and lose HEALTH!")
        energy = 0
        health -= 1
        time.sleep(0.3)
    print("----------------------------------------")
    print(f"{health}/{max_health} ❤️ Health		X:{player_x + 1} Y:{player_y + 1} {current_tile}{current_tile_name}")
    print(f"{energy}/{max_energy} 🩸 Energy		🧪:{potion} 💰: {gold}")
    print("----------------------------------------")

    if mountain_count <= 8:
        regrowmountain()


def regrowmountain():
    mountain_count = 0

    while True:

        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if map_data[x][y] == tiles["plateau"]:
            map_data[x][y] = tiles["mountain"]
            mountain_count += 1
        if mountain_count == 7:
            print(
                "Suddenly, the ground beneath your feet begins to tremble and shake violently. The very earth seems to split open, sending massive boulders and chunks of rock hurtling through the air. As the quake subsides, you look up to see majestic towering peaks rising up where there was once nothing but flat ground.")
            break


def regrowforest():
    forest_count = 0

    while True:

        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if map_data[x][y] == tiles["plateau"] and x % 2 == 0:
            map_data[x][y] = tiles["grass"]
        if map_data[x][y] == tiles["grass"]:
            map_data[x][y] = tiles["forest"]
            forest_count += 1
        if forest_count == 7:
            print(
                "You can hear the ethers murmur echoing, as suddenly the earth trembles and breaks apart, but from the magic powers within, forests and fields bloom in its wake, creating new life and wonder, even amidst the chaos.")
            break


def pad_emoji(emoji, width=2):
    return emoji + " " * (width - len(emoji.encode('utf-16-le')) // 2)


# Print the initial map and player position
print_map()

# Game Loop
while True:

    if health <= 0:
        death()

    # Get the user's input
    user_input = input("Enter a command! (Try 'commands' for help) ")
    user_input = user_input.lower()

    if user_input == "enter" or user_input == "e":
        if map_data[player_x][player_y] == tiles["mountain"]:
            mine()
        if map_data[player_x][player_y] == tiles["forest"]:
            hike()
        if map_data[player_x][player_y] == tiles["npc"]:
            npc()
        if map_data[player_x][player_y] == tiles["water"]:
            spring()
        if map_data[player_x][player_y] == tiles["building"]:
            tower()

    if user_input == "camp":
        if map_data[player_x][player_y] == tiles["grass"]:
            camp()
        else:
            print("You can only camp in grass fields! (,)")
            time.sleep(0.3)

    if user_input == "potion":
        drink_potion()

    if user_input == "map" or user_input == "m":
        print_map()

    if user_input == "plant":
        if map_data[player_x][player_y] == tiles["grass"]:
            if herbs >= 5:
                print("You made this world a better place! And this grassy patch became a forest.")
                herbs -= 5
                map_data[player_x][player_y] = tiles["forest"]
            else:
                print("You need at least 5 HERBS to plant a forest.")
        else:
            print("You can only plant on grass.")

    if user_input == "build":
        if map_data[player_x][player_y] == tiles["plateau"]:
            if stone >= 22 and wood >= 12 and iron >= 5 and leather >= 3 and ether >= 1 and story_stage == 2:
                print("VORLUND:")
                print(
                    "'Å, young adventurer, I must say that I am impressed by your work. This tower you have built is no ordinary structure - it will serve as a portal to new realms, and it is a feat that not many can achieve. You have my congratulations and my thanks.'")

                print(
                    "'However, do not think that your journey ends here. To activate this portal, you will need the help of a skilled alchemist - one who can mix the right ingredients and perform the necessary rituals. It will not be an easy task, and the road ahead will be filled with danger and challenges.'")

                stone -= 22
                wood -= 12
                iron -= 5
                leather -= 3
                ether -= 1
                map_data[player_x][player_y] = tiles["building"]
                story_stage = 3
                tower()
            elif story_stage <= 1:
                print("You need a plan in order to build a tower.")
            elif story_stage >= 3:
                print("You already built a tower!")
            else:
                print("To build a basic tower you need:")
                print("--------")
                print(f"22 🧱 STONE - {stone}/22")
                print(f"12 🪵 WOOD - {wood}/12")
                print(f"5 ⛓ IRON - {iron}/5")
                print(f"3 🟫 LEATHER - {leather}/3")
                print(f"1 🪬 ETHER - {ether}/1")


        else:
            print("You can only build a tower on plateau.")

    # inventory command
    if user_input == "inventory" or user_input == "i":
        print("--------")
        print("INVENTORY")
        print("--------")
        time.sleep(0.2)
        print(f"🪵 WOOD - {wood}")
        time.sleep(0.2)
        print(f"🧱 STONE - {stone}")
        time.sleep(0.2)
        print(f"⛓ IRON - {iron}")
        time.sleep(0.2)
        print(f"💰 GOLD - {gold}")
        time.sleep(0.2)
        print(f"🪬 ETHER - {ether}")
        time.sleep(0.2)
        print(f"💧 WATER - {water}")
        time.sleep(0.2)
        print(f"🌱 HERBS - {herbs}")
        time.sleep(0.2)
        print(f"🧪 POTION - {potion}")
        time.sleep(0.2)
        print(f"🟫 LEATHER - {leather}")
        time.sleep(0.2)
        if weapon == "bow":
            print(f"📌 ARROW - {arrow}")
            time.sleep(0.2)
        print("--------")

    if user_input == "stats":
        print("--------")
        print("STATS")
        print("--------")
        time.sleep(0.2)
        print(f"🛡 DEFENSE - {base_defense}")
        time.sleep(0.2)
        print(f"⚔️ STRENGTH - {base_strength}")
        time.sleep(0.2)
        print(f"🏹 DEXTERITY - {base_dex}")
        time.sleep(0.2)
        print(f"🔮 WORLD STAGE - {world_stage}")
        time.sleep(0.2)
        print("--------")

    # list command
    if user_input == "commands" or user_input == "c":
        # print("Here is a list of commands: up, down, left, right, stats, inventory, camp, hunt, mine, lumber, build, help ")
        print("--------")
        print("MOVEMENT")
        print("--------")
        time.sleep(0.2)
        print("'up' - You move one step north. Moving consumes energy.")
        time.sleep(0.2)
        print("'down' - You move one step south. Moving consumes energy.")
        time.sleep(0.2)
        print("'right' - You move one step east. Moving consumes energy.")
        time.sleep(0.2)
        print("'left' - You move one step west. Moving consumes energy.")
        time.sleep(0.2)

        print("--------")
        print("ADVENTURE")
        print("--------")
        time.sleep(0.2)
        print("'enter' - Interact with FORESTS (🌲), MOUNTAINS (🌋), GRASS (🌿) and WATER (💧) you currently stand on.")
        time.sleep(0.2)
        print(
            f"'camp' - Rest in a small, single-use camp build on grass (🌿). Requires {world_stage + 2} WOOD, but restores Energy and Health.")
        time.sleep(0.2)
        print("--------")
        print("MISC")
        print("--------")
        time.sleep(0.2)
        print("'build' - A material consuming milestone on your way to the next map.")
        time.sleep(0.2)
        print("'plant' - Consumes 5 herbs to plant a forest. Only available on grass. (🌿)")
        time.sleep(0.2)
        print("'potion' - Consumes 1 potion and regenerates the adventurers body.")
        time.sleep(0.2)

    if user_input in movement_vectors:
        # Move the player character
        dx, dy = movement_vectors[user_input]
        move_player(dx, dy)

    # testcommands:
    if user_input == "test fight 1":
        fight(1)

    if user_input == "test fight 2":
        fight(2)

    if user_input == "test camp":
        camp()

    if user_input == "test hike":
        hike()

    if user_input == "test mine":
        mine()

    if user_input == "test hunter":
        hunter()

    if user_input == "test spring":
        spring()

    if user_input == "test eel":
        eel()

    if user_input == "test npc":
        npc()

    if user_input == "test tower":
        tower()

    if user_input == "test wanderer":
        wanderer()

    if user_input == "test death":
        death()

    if user_input == "test regrow m":
        regrowmountain()

    if user_input == "test regrow f":
        regrowforest()

    if user_input == "test bow":
        weapon = "bow"

    if user_input == "test chest":
        chest()

    if user_input == "test food":
        food()

    if user_input == "test occultist":
        occultist()

    if user_input == "test setdemon":
        setdemon()

    if user_input == "test brew":
        tower_alchemist = 2
        brew()

    if user_input == "test items":
        gold += 99
        water += 99
        wood += 99
        stone += 99
        ether += 99
        herbs += 99
        iron += 99
        potion += 99
        leather += 99

    if user_input == "test":
        print(
            "items, death, wanderer, tower, npc, hunter, occultist, eel, spring, fight 1, fight 2, camp, chest, hike, mine, regrow m, regrow f, bow")

