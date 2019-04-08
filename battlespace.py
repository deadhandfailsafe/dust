import random
import unit
import data_terrain


class Terrain():
    def __init__(self, terrain_type, terrain_conceal, terrain_cover):
        self.terrain_type = terrain_type
        self.terrain_conceal = terrain_conceal
        self.terrain_cover = terrain_cover
        self.terrain_units = []


class OpenGround(Terrain):
    def __init__(self):
        super().__init__(terrain_type='Open Ground',
                         terrain_conceal=5,
                         terrain_cover=5)


class Woods(Terrain):
    def __init__(self):
        super().__init__(terrain_type='Woods',
                         terrain_conceal=40,
                         terrain_cover=30)


class City(Terrain):
    def __init__(self):
        super().__init__(terrain_type='City',
                         terrain_conceal=70,
                         terrain_cover=60)


def terrainGenerator():
    t_pick = random.randint(1, 3)
    if t_pick == 1:
        return OpenGround()
    elif t_pick == 2:
        return Woods()
    elif t_pick == 3:
        return City()


def TerrainSetRatings(squad):
    location = squad.location
    for unit in squad.squad_box:
        unit.concealment = random.randint(0, location.terrain_conceal)
        unit.cover = random.randint(0, location.terrain_cover)


def TargetSelection(attacker, target):
    i = 0
    while i < len(attacker.squad_box) - 1:
        s_index = random.randint(0, len(target.squad_box) - 1)
        vision_check = random.randint(0, 100) + attacker.squad_box[i].prowess
        if vision_check >= target.squad_box[s_index].concealment:
            attacker.squad_box[i].target = target.squad_box[s_index].uid
        else:
            attacker.squad_box[i].target = 'NONE'
        i += 1


def TargetAttack(attacker, target_squad):
    target_id = attacker.target
    t_index = 0
    for x in target_squad.squad_box:
        if x.uid == target_id:
            t_index = target_squad.squad_box.index(x)
    cover_check = random.randint(0, 100)
    if cover_check >= target_squad.squad_box[t_index].cover:
        print(attacker.name, 'hits his target:',
              target_squad.squad_box[t_index].name, '!')
        print(unit.Body.distribute_damage(
            target_squad.squad_box[t_index], 20))
        print(target_squad.squad_box[t_index].health, '->',
              unit.Body.get_healthpool(target_squad.squad_box[t_index].body))
    else:
        print(attacker.name, 'misses his target!')
