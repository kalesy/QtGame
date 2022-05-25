from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import random

class Board(QFrame):

    def __init__(self, parent):
        self.boardWidth = 15
        self.boardHeight = 15
        super().__init__(parent)
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

    def drawBoard(self, painter):

        # 设置画笔颜色
        painter.setPen(QColor(0,0,0))
        # 游戏网格
        for x in range(self.boardWidth):
            for y in range(self.boardHeight):
                gridX = x * 32 + 8
                gridY = y * 32 + 8
                if(self[x, y] == 9):
                    painter.fillRect(gridX, gridY, 32, 32, QColor(0, 0, 0))
                elif(self[x, y] == 'p'):
                    painter.fillRect(gridX, gridY, 32, 32, QColor(0, 0, 255))
                elif(self[x, y] == 8):
                    painter.fillRect(gridX, gridY, 32, 32, QColor(255, 0, 0))
                elif(self[x, y] == 'w'):
                    painter.fillRect(gridX, gridY, 32, 32, QColor(153, 153, 153))
                elif(self[x, y] == 'e'):
                        painter.fillRect(gridX, gridY, 32, 32, QColor(0, 153, 0))
                        


                #画格子
                painter.drawRect(gridX, gridY, 32, 32)

        # 状态界面
        rightPanelStartX = self.boardWidth * 32 + 8
        rightPanelStartY = 8

        painter.drawRect(rightPanelStartX, rightPanelStartY, 200, self.boardHeight * 32)

        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 20, Qt.AlignCenter, 40, 40, f"玩  家")
        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 60, Qt.AlignCenter, 40, 40, f"生命值：{99}")
        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 100, Qt.AlignCenter, 40, 40, f"攻击力：{99}")
        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 140, Qt.AlignCenter, 40, 40, f"等  级：{99}")

        enemy_text_offset = 300
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 20, Qt.AlignCenter, 40, 40, f"敌  人")
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 60, Qt.AlignCenter, 40, 40, f"生命值：{99}")
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 100, Qt.AlignCenter, 40, 40, f"攻击力：{99}")
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 140, Qt.AlignCenter, 40, 40, f"等  级：{99}")


    def move(self, direction:tuple, posFrom):
        posEnd = direction[0] + self.boardWidth * direction[1] + posFrom
        if(posEnd < self.boardWidth or posEnd > (self.boardWidth * (self.boardHeight - 1))):
            return

