class Player:

    def __init__(self, hp, lv, exp, attack, lvUpExp):
        self.hp = hp 
        self.lv = lv
        self.exp = exp
        self.attack = attack
        self.lvUpExp = lvUpExp

    def takeDamage(self, damage):
        pass

    def gainExp(self, exp):
        result = self.exp + exp - self.lvUpExp
        if(result < 0):
            self.levelUp()
            self.exp = - result


    def levelUp(self):
        pass
