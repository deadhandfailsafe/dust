import random
import coremedical
import data_man
import data_ru
import entity


unit_id_max = 9999


class Unit(entity.Entity):
    def __init__(self, box, nation, era):
        super().__init__(box)
        self.nation = nation
        self.era = era


class Man(Unit):
    def __init__(self, box, nation, era):
        super().__init__(box, nation, era)
        self.name = Man.grab_name(nation)
        self.age = random.randint(17, 35)
        self.height = random.randint(60, 80)
        fat_ratio = round(random.uniform(2.3, 3.2), 1)
        self.weight = round(self.height * fat_ratio, 0)

        self.toughness = random.randint(1, 12)
        self.awareness = random.randint(1, 12)
        self.prowess = random.randint(1, 12)

        self.body = coremedical.Body(data_man.data_health_man, self.toughness)
        self.health = coremedical.Body.getCurrentHealth(self.body)
        self.alive = True

        self.occupation = 'CIVILIAN'

        self.abilities = ['THINK', 'BREATHE', 'SMELL', 'SEE', 'HEAR', 'TALK',
                          'ONEHANDGRAB', 'TWOHANDGRAB', 'THROW', 'CLIMB',
                          'STAND', 'CROUCH', 'WALK', 'RUN', 'JUMP']

        self.veterancy = 'UNTRAINED'
        self.morale = 100

        self.loadout = []
        self.equipment = []
        self.uniform = 'Civilian Clothes'

        self.concealment = 0
        self.cover = 0

        self.target = 'NONE'

    @staticmethod
    def grab_name(nation):
        if nation == 'RU':
            data_list = data_ru
            data_found = True
        else:
            data_list = None
            data_found = False
        if data_found is True:
            return data_list.names[random.randint(0, len(data_list.names) - 1)]
        else:
            return 'ERROR!'

    @staticmethod
    def grab_rank(nation, rank_top):
        if nation == 'RU':
            data_list = data_ru
            data_found = True
        else:
            data_list = None
            data_found = False
        if data_found is True:
            return data_list.ranks[random.randint(0, rank_top - 1)]
        else:
            return 'ERROR!'

    def job_hire(self):
        pass


class Rifleman(Man):
    def __init__(self, box, nation, era):
        super().__init__(box, nation, era)
        self.occupation = 'RIFLEMAN'
        self.rank = Man.grab_rank(nation, 2)
        if self.rank != 'PVT':
            self.veterancy = 'GREEN'
        else:
            self.veterancy = 'CONSCRIPT'

        self.abilities += ['SHOOT', 'GRENADE', 'MELEE']

        self.uniform = data_ru.camo_patterns[random.randint(
            0, len(data_ru.camo_patterns) - 1)] + ' Camo Uniform'


class Squad(Unit):
    def __init__(self, box, nation, era, squad_size):
        super().__init__(box, nation, era)
        self.squad_size = squad_size
        self.location = 'Open Ground'
        self.squad_box = []
