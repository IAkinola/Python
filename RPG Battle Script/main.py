from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 12, 120, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Creating Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade]

# Instantiate Characters
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print("AN ENEMY ATTACKS!")

while running:
    print("======================================")
    player.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1

# Attacking with normal Attacks
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")

# Attacking with magic
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1

        # To go up the menu
        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_spell_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print("\nNot enough MP")
            continue
        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print("\n" + spell.name + " heals for", str(magic_dmg), "HP.")
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print("\n" + spell.name + " deals", str(magic_dmg), "points of damage")


# Using Items
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose Item: ")) - 1

        # To go up the menu
        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.effect == "potion":
            player.heal(item.prop)
            print("\n" + item.name + " heals for", str(item.effect), "HP.")

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    print("________________________________")
    print("Enemy HP:" + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + "\n")

    print("Your HP:" + str(player.get_hp()) + "/" + str(player.get_max_hp()))
    print("Your MP:" + str(player.get_mp()) + "/" + str(player.get_max_mp()) + "\n")

    if enemy.get_hp() == 0:
        print("You Win!")
        running = False
    elif player.get_hp() == 0:
        print("Your Enemy has defeated you!")
        running = False
