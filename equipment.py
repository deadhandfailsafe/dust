import random
import entity


class Equipment(entity.Entity):
    def __init__(self):
        self.name = name
        self.utility = utility
        

class Firearm(Equipment):
    def __init__(self, name):
        super().__init__(name, utility = 'weapon')
        self.format = format
        self.caliber = caliber
        self.firepower = firepower
        self.firerate = firerate
