from PyQt5.QtCore import Qt
from Unit import Player

class Game:

    def __init__(self, board):
        self.board = board
        self.player = Player()
        self.currentEnemy = None

    def keyevent(self, key):
        if(key == Qt.Key_Left or key == Qt.Key_A):
            self.board.move([-1, 0])
        elif(key == Qt.Key_Right or key == Qt.Key_D):
            self.board.move([1, 0])
        elif(key == Qt.Key_Up or key == Qt.Key_W):
            self.board.move([0, -1])
        elif(key == Qt.Key_Down or key == Qt.Key_S):
            self.board.move([0, 1])

    def update(self):
        if(self.player.hp < 1):
            return 'gameover'

    def engage(self, enemy):
        self.currentEnemy = enemy
        if(self.player.hp < 1):
            return 'playerDown'
        if(self.currentEnemy.hp < 1):
            self.player.gainExp(self.currentEnemy.expOnKill)
            return 'enemyDown'
        self.player.takeDamage(self.currentEnemy.attack)
        self.currentEnemy.takeDamage(self.player.attack)



