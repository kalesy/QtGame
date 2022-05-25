from PyQt5.QtCore import Qt
from functools import partial

class Game:

    def __init__(self, moveFunc):
        self.playerPos  = [0,0]
        self.moveLeft   = partial(moveFunc, direction = (-1,  0))
        self.moveRight  = partial(moveFunc, direction = ( 1,  0))
        self.moveUp     = partial(moveFunc, direction = ( 0,  1))
        self.moveDown   = partial(moveFunc, direction = ( 0, -1))

    def keyevent(self, key):
        if(key == Qt.Key_Left or key == Qt.Key_A):
            self.moveLeft()
        elif(key == Qt.Key_Right or key == Qt.Key_D):
            self.moveRight()
        elif(key == Qt.Key_Up or key == Qt.Key_W):
            self.moveUp()
        elif(key == Qt.Key_Down or key == Qt.Key_S):
            self.moveDown()
