from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen, QImage
import sys, random, math

from Board import Board
from Game import Game
from Resource import Resource

class RandomDungeon(QMainWindow):

    DEBUG = True

    def __init__(self):
        super().__init__()
        self.cellSize = 64
        self.setWindowTitle("随机地牢")
        res = Resource(
                sand   = {  'floor':        QImage('imgs/brickfloor.png'), 
                            'wall':         QImage('imgs/brickwall.png'),
                            'outerWall':    QImage('imgs/outerWall.png')},

                player = {  'knight':       QImage('imgs/player.png')},
                mobs   = {  'mobs':         QImage('imgs/mobs.png')},
                icons  = {  'icons':        QImage('imgs/icons.png')} 
                )
        self.board = Board(self, self.cellSize, res)
        self.game = Game(self.board)
        self.board.game = self.game
        self.setCentralWidget(self.board)

        #self.resize(self.board.boardWidth * self.cellSize + 16 + 200, self.board.boardHeight * self.cellSize + 16)
        self.setFixedSize(self.board.boardWidth * self.cellSize + 16 + 200, self.board.boardHeight * self.cellSize + 16)

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        #self.move(int((screen.width()-size.width())/2), int(screen.height()-size.height()/2))
        self.show()

    def keyPressEvent(self, event):
        self.update()
        gameevent = self.game.update()
        if(gameevent == 'gameover'):
            self.gameover()
        else:
            self.game.keyevent(event.key())

    def gameover(self):
        QMessageBox.information(self, "Information", "游戏结束")
        QApplication.exit(0)


    def paintEvent(self, event):
        painter = QPainter()

        # 开始画图
        painter.begin(self)

        self.board.drawBoard(painter)
        # 结束画图
        painter.end()



if __name__ == '__main__':
    app = QApplication([])
    randomDungeon = RandomDungeon()
    sys.exit(app.exec_())

