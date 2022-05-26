from Unit import Unit

class Character(Unit):

    def __init__(self, unittype, hp, lv, attack):
        self.hp = hp 
        self.lv = lv
        self.attack = attack

    def takeHpUp(self, amount):
        self.hp += amount

    def takeDamage(self, damage):
        self.hp -= damage
        if(self.hp < 0):
            self.hp = 0

