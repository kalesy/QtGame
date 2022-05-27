import random
from Item import Item, Weapon, HpUp

class Unit:

    def __init__(self, unittype):
        self.unittype = unittype

class Character(Unit):

    def __init__(self, unittype, hp, lv, attack):
        self.hp = hp 
        self.lv = lv
        self.attack = attack

    def takeDamage(self, damage):
        self.hp -= damage
        if(self.hp < 0):
            self.hp = 0

class Enemy(Character):
    
    BaseHP = 20
    BaseAttack = 2
    BaseExpOnKill = 20

    def __init__(self, layer, imgoffset):
        hp = int((1.03 ** layer) * Enemy.BaseHP * random.uniform(1.0, 2.0))
        attack = int((1.02 ** layer) * Enemy.BaseAttack * random.uniform(1.0, 3.0))
        self.expOnKill = int((1.05 ** layer) * Enemy.BaseExpOnKill * random.uniform(1.0, 1.5))
        print(self.expOnKill)
        self.imgoffset = imgoffset
        super().__init__('enemy', hp, 0, attack)

class Player(Character):

    def __init__(self, hp = 50, lv = 1, exp = 0, attack = 5, lvUpExp = 100):
        super().__init__('player', hp, lv, attack)
        self.unittype = 'player'
        self.exp = exp
        self.lvUpExp = lvUpExp

    def takeHpUp(self, amount):
        self.hp += amount

    def gainExp(self, exp):
        self.exp += exp
        print(self.exp)
        if(self.exp > self.lvUpExp):
            self.levelUp()
            self.exp -= self.lvUpExp

    def levelUp(self):
        self.hp += random.randint(3, 8)
        self.lv += 1
        self.attack += random.randint(2, 5)

    def takeItem(self, item):
        if(item.itemtype == 'hpup'):
            self.hp += item.hpup
        elif(item.itemtype == 'weapon'):
            self.attack += item.attack

class Wall(Unit):
    
    def __init__(self):
        self.breakable = False


class FakeWall(Unit):

    def __init__(self, layer):
        self.breakable = True
        if(random.random() > 0.75):
            self.item = HpUp(layer)
        else:
            self.item = Weapon(layer)

    def getItem(self, layer):
        return self.item
