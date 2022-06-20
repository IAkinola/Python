from classes.game import Person, bColors

magic = [{"name": "Fire", "cost":10, "dmg": 60},
         {"name": "Thunder", "cost":10, "dmg": 60},
         {"name": "Blizzard", "cost":10, "dmg": 60}]

player = Person(400, 65, 60, 34, magic)

print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())