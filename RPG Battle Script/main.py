from classes.game import Person, bColors

magic = [{"name": "Fire", "cost":10, "dmg": 60},
         {"name": "Thunder", "cost":10, "dmg": 70},
         {"name": "Blizzard", "cost":10, "dmg": 80}]

player = Person(460, 65, 60, 34, magic)

print(player.generate_damage())
print(player.generate_spell_damage(1))
