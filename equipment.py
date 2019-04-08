import random
import entity


class Equipment(entity.Entity):
    def __init__(self, box, name, utility):
        super().__init__(box)
        self.name = name
        self.utility = utility


class Firearm(Equipment):
    def __init__(self, box, name, format, caliber, firepower, firerate,
                 magsize,
                 current_ammo):
        super().__init__(box, name, utility='weapon')
        self.format = format
        self.caliber = caliber
        self.firepower = firepower
        self.firerate = firerate
        self.magsize = magsize
        self.current_ammo = current_ammo
        self.serial_number = '{:05}'.format(self.eid)


class Kalashnikov(Firearm):
    def __init__(self, box):
        super().__init__(box,
                         name='AK-74',
                         format='Assault Rifle',
                         caliber='5.45x39mm',
                         firepower='IV',
                         firerate=600,
                         magsize=30,
                         current_ammo=30)


def FireWeapon(weapon):
    if weapon.current_ammo != 0:
        weapon.current_ammo -= 1
    else:
        # reload function
        weapon.current_ammo = weapon.magsize
