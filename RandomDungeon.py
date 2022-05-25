from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPixmap, QPen
import sys, random, math

debug = True

class RandomDungeon(QMainWindow):

    def __init__(self):
        super().__init__()

        self.board = Board(self)
        self.setCentralWidget(self.board)


        self.resize(self.board.boardWidth * 32 + 16 + 200, self.board.boardHeight * 32 + 16)

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QColor(0,0,0))

        # 画图循环

        # 游戏网格
        for x in range(self.board.boardWidth):
            for y in range(self.board.boardHeight):

                if(self.board[x, y] == 9):
                    painter.fillRect(x * 32 + 8, y * 32 + 8, 32, 32, QColor(0, 0, 0))
                elif(self.board[x, y] == 'p'):
                    painter.fillRect(x * 32 + 8, y * 32 + 8, 32, 32, QColor(0, 0, 255))
                elif(self.board[x, y] == 8):
                    painter.fillRect(x * 32 + 8, y * 32 + 8, 32, 32, QColor(255, 0, 0))
                elif(self.board[x, y] == 'w'):
                    painter.fillRect(x * 32 + 8, y * 32 + 8, 32, 32, QColor(153, 153, 153))
                elif(self.board[x, y] == 'e'):
                    if(debug):
                        painter.fillRect(x * 32 + 8, y * 32 + 8, 32, 32, QColor(0, 153, 0))
                    else:
                        painter.fillRect(x * 32 + 8, y * 32 + 8, 32, 32, QColor(153, 153, 153))


                painter.drawRect(x * 32 + 8, y * 32 + 8, 32, 32)

        # 状态界面
        rightPanelStartX = self.board.boardWidth * 32 + 8
        rightPanelStartY = 8

        painter.drawRect(rightPanelStartX, rightPanelStartY, 200, self.board.boardHeight * 32)

        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 20, Qt.AlignCenter, 40, 40, f"玩  家")
        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 60, Qt.AlignCenter, 40, 40, f"生命值：{99}")
        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 100, Qt.AlignCenter, 40, 40, f"攻击力：{99}")
        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 140, Qt.AlignCenter, 40, 40, f"等  级：{99}")

        enemy_text_offset = 300
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 20, Qt.AlignCenter, 40, 40, f"敌  人")
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 60, Qt.AlignCenter, 40, 40, f"生命值：{99}")
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 100, Qt.AlignCenter, 40, 40, f"攻击力：{99}")
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 140, Qt.AlignCenter, 40, 40, f"等  级：{99}")

        painter.end()

class Board(QFrame):

    def __init__(self, parent):
        self.boardWidth = 15
        self.boardHeight = 15
        super().__init__(parent)
        self.timer = QBasicTimer()
        self.setFocusPolicy(Qt.StrongFocus)

        self.createStage()

    # 除了墙其他的东西
    # 8 怪
    # 7 
    # 6 
    # 5 
    # 4 
    # 3 
    # 2 回血道具
    # 1 武器
    # 0 空
    # p 玩家
    # w 内墙
    def createStage(self):
        self.grid = [0 for x in range(self.boardWidth * self.boardHeight)]

        # 生成玩家
        start_2d = (random.randint(1, self.boardWidth - 2), random.randint(1, self.boardHeight - 2))
        start_1d = start_2d[0] + self.boardWidth * start_2d[1]
        # 生成终点
        while(True):
            end_2d = (random.randint(1, self.boardWidth - 2), random.randint(1, self.boardHeight - 2))
            if(end_2d == start_2d):
                continue
            elif(abs(end_2d[0] - start_2d[0]) + abs(end_2d[1] - start_2d[1]) < 6):
                continue
            else:
                break
        end_1d = end_2d[0] + self.boardWidth * end_2d[1]

        self.grid[start_1d] = 'p'
        self.grid[end_1d] = 'e'

        for i in range(len(self.grid)):
            # 画墙
            if(i % self.boardWidth == 0):
                self.grid[i] = 9
            elif(i < self.boardWidth):
                self.grid[i] = 9
            elif((i + 1) % self.boardHeight == 0):
                self.grid[i] = 9
            elif(i > self.boardWidth * ( self.boardHeight - 1)):
                self.grid[i] = 9
            else:
                if(self.grid[i] != 0):
                    continue
                if(random.random() < 0.1):
                    self.grid[i] = 8
                elif(random.random() < 0.2):
                    self.grid[i] = 'w'

    def __getitem__(self, x_y):
        return self.grid[x_y[0] + self.boardWidth * x_y[1]]

    def __setitem__(self, x_y:tuple, board_cell_data):
        self.grid[x_y[0] + self.width * x_y[1]] = board_cell_data

    # 找到出口触发的函数
    def triggerEnd(self):
        pass

class Game():
    pass


if __name__ == '__main__':
    app = QApplication([])
    randomDungeon = RandomDungeon()
    sys.exit(app.exec_())

