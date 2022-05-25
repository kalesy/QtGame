from PyQt5.QtCore import Qt
from functools import partial

class Game:

    def __init__(self, board):
        self.board = board

    def keyevent(self, key):
        if(key == Qt.Key_Left or key == Qt.Key_A):
            self.board.move([-1, 0])
        elif(key == Qt.Key_Right or key == Qt.Key_D):
            self.board.move([1, 0])
        elif(key == Qt.Key_Up or key == Qt.Key_W):
            self.board.move([0, -1])
        elif(key == Qt.Key_Down or key == Qt.Key_S):
            self.board.move([0, 1])


    #def 
