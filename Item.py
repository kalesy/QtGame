import random

class Item:

    def __init__(self, itemtype):
        self.itemtype = itemtype


class Weapon(Item):

    BaseAttack = 3

    def __init__(self, layer):
        super().__init__('weapon')
        self.attack = int((1.1 ** layer) * Weapon.BaseAttack * random.uniform(1.0, 1.3))

class HpUp(Item):

    BaseHp = 5
    def __init__(self, layer):
        super().__init__('hpup')
        self.hpup = int((1.2 ** layer) * HpUp.BaseHp * random.uniform(1.0, 1.3))

