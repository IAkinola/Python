# Game Logic

import random


class bcolors:
    HEADER = '\003[95m'
    OKBLUE = '\003[94m'
    OKGREEN = '\003[92m'
    WARNING = '\003[93m'
    FAIL = '\003[91m'
    ENDC = '\003[0m'
    BOLD = '\003[1m'
    UNDERLINE = '\003[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def choose_action(self):
        i = 1
        print("\n" + self.name)
        print("ACTIONS:")
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + "MAGIC:")
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + "ITEMS:")
        for item in self.items:
            print("    " + str(i) + ".", item["item"].name + ":", item["item"].description, " (x5)")
            i += 1

    # Enemy HP Bar
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                       __________________________________________________")
        print(self.name + "    "
              + current_hp + " |" + hp_bar + "|")

    # Making UI for the game
    def get_stats(self):
        # HP Bar
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        # MP BAR
        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        # Dealing with White Spaces in the HP UI
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                    _________________________             __________")
        print(self.name + "    " + current_hp + " |" + hp_bar + "|   " + current_mp + " |" + mp_bar + "|")
