import unit
import battlespace
import coremedical

unit_box = []
terrain_box = []

player_squad = unit.Squad(unit_box, 'RU', 1990, 5)
i = 0
player_squad.location = battlespace.terrainGenerator()
while i < player_squad.squad_size:
    soldat = unit.Rifleman(unit_box, 'RU', 1990)
    unit_box.append(soldat)
    player_squad.squad_box.append(soldat)
    i += 1
battlespace.TerrainSetRatings(player_squad)

enemy_squad = unit.Squad(unit_box, 'RU', 1990, 5)
i = 0
enemy_squad.location = battlespace.terrainGenerator()
while i < enemy_squad.squad_size:
    soldat = unit.Rifleman(unit_box, 'RU', 1990)
    unit_box.append(soldat)
    enemy_squad.squad_box.append(soldat)
    i += 1
battlespace.TerrainSetRatings(enemy_squad)

print(player_squad.location.terrain_type)
for soldier in player_squad.squad_box:
    print(soldier.name, '// Concealment:', soldier.concealment, '// Cover', soldier.cover)
print(enemy_squad.location.terrain_type)
for soldier in enemy_squad.squad_box:
    print(soldier.name, '// Concealment:', soldier.concealment, '// Cover', soldier.cover)
