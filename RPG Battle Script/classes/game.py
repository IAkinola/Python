import random

class bColors:
    HEADER = '\003[95m'
    OKBLUE = '\003[94m'
    OKGREEN = '\003[92m'
    WARNING = '\003[93m'
    FAIL = '\003[91m'
    ENDC = '\003[0m'
    BOLD = '\003[1m'
    UNDERLINE = '\003[4m'

class Person:
    def __int__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack, Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)
