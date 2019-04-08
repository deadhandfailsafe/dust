import random


class Body():
    def __init__(self, data_health, toughness):
        self.health = dict(data_health)
        self.max_hp = 0
        for part in self.health:
            self.health[part] += toughness
            self.max_hp += self.health[part]

    def getCurrentHealth(self):
        current_hp = 0
        for part in self.health:
            current_hp += self.health[part]
        return current_hp

    @staticmethod
    def getHitLocation(data_prob, location, lr):
        if location is 'NONE':
            location_roll = random.randint(1, 100)
            lr_split = random.randint(0, 1)
        else:
            location_roll = location
            lr_split = lr
        p_index = 0
        for part in data_prob:
            p_index += data_prob[part]
            if location_roll <= p_index:
                if part == 'arm':
                    if lr_split == 0:
                        part = 'right_arm'
                    else:
                        part = 'left_arm'
                elif part == 'leg':
                    lr_split = random.randint(0, 1)
                    if lr_split == 0:
                        part = 'right_leg'
                    else:
                        part = 'left_leg'
                location_hit = part
                return location_hit

    def distributeShotSpread(self, data_prob, amount, s_range, damage):
        location_rolls = []
        amount -= 1
        location_roll = random.randint(1, 100)
        lr_split = random.randint(0, 1)
        location_rolls.append(location_roll)
        while amount > 0:
            spread_roll = location_roll + \
                random.randint(-(s_range), s_range)
            if spread_roll > 100:
                spread_roll = 100
            elif spread_roll < 1:
                spread_roll = 1
            location_rolls.append(spread_roll)
            amount -= 1
        locations = []
        for roll in location_rolls:
            locations.append(Body.getHitLocation(
                data_prob, roll, lr_split))
        print(locations)
        for location in locations:
            self.distributeDamage(damage, location)

    def distributeDamageFragments(self, data_prob, amount, damage):
        locations = []
        while amount > 0:
            locations.append(Body.getHitLocation(data_prob, 'NONE', 0))
            amount -= 1
        for location in locations:
            self.distributeDamage(damage, location)

    def distributeDamage(self, damage, location):
        if self.body.health[location] == 0:
            Body.distributeHeavyDamage(self, damage)
        elif self.body.health[location] > 0:
            check_limit = self.body.health[location] - damage
            if check_limit < 0:
                self.body.health[location] = 0
                extra_damage = abs(check_limit)
                Body.distributeHeavyDamage(self, extra_damage)
            elif check_limit >= 0:
                self.body.health[location] -= damage

    def distributeHeavyDamage(self, damage):
        heavy_damage = damage * 2
        heavy_distribute = Body.getSpreadDamage(self, heavy_damage)
        for part in self.body.health:
            if self.body.health[part] != 0:
                self.body.health[part] -= heavy_distribute
            if self.body.health[part] <= 0:
                self.body.health[part] = 0

    def getSpreadDamage(self, damage):
        damage_divide = 0
        for part in self.body.health:
            if self.body.health[part] != 0:
                damage_divide += 1
        bleed = int(damage / damage_divide)
        if bleed == 0:
            return 1
        else:
            return bleed

    def distributeBleed(self, location, bleed):
        if self.body.health[location] != 0:
            self.body.health[location] -= bleed
        else:
            bleed_distribute = Body.getSpreadDamage(self, bleed)
            for part in self.body.health:
                if self.body.health[part] != 0:
                    self.body.health[part] -= bleed_distribute
        if self.body.health[location] < 0:
            self.body.health[location] = 0

    def limbChecks(self):
        if self.body.health['head'] == 0 or self.body.health['neck'] == 0:
            self.alive = False

        if self.body.health['right_arm'] == 0 and \
                self.body.health['left_arm'] == 0:
            abilities = ['TWOHANDGRAB', 'ONEHANDGRAB', 'CLIMB', 'THROW']
            for ability in abilities:
                if ability in self.abilities:
                    self.abilities.remove(ability)
        elif self.body.health['right_arm'] == 0 or \
                self.body.health['left_arm'] == 0:
            abilities = ['TWOHANDGRAB', 'CLIMB']
            for ability in abilities:
                if ability in self.abilities:
                    self.abilities.remove(ability)

        if self.body.health['upper_torso'] == 0:
            abilities = ['BREATHE', 'TALK', 'THROW', 'CLIMB']
            for ability in abilities:
                if ability in self.abilities:
                    self.abilities.remove(ability)

        if self.body.health['lower_torso'] == 0:
            abilities = ['STAND', 'CROUCH', 'WALK', 'RUN', 'JUMP']
            for ability in abilities:
                if ability in self.abilities:
                    self.abilities.remove(ability)

        if self.body.health['pelvis'] == 0:
            abilities = ['CLIMB', 'STAND', 'CROUCH', 'WALK', 'RUN',
                         'JUMP']
            for ability in abilities:
                if ability in self.abilities:
                    self.abilities.remove(ability)

        if self.body.health['right_leg'] == 0 and \
                self.body.health['left_leg'] == 0:
            abilities = ['CLIMB', 'STAND', 'CROUCH', 'WALK', 'RUN',
                         'JUMP']
            for ability in abilities:
                if ability in self.abilities:
                    self.abilities.remove(ability)
        elif self.body.health['right_leg'] == 0 or \
                self.body.health['left_leg'] == 0:
            abilities -= ['CLIMB', 'CROUCH', 'RUN', 'JUMP']
            for ability in abilities:
                if ability in self.abilities:
                    self.abilities.remove(ability)
