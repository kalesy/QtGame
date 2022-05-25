from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from Cell import Cell
import random

class Board(QFrame):

    def __init__(self, parent, cellSize):
        self.cellSize = cellSize
        self.boardWidth = 15
        self.boardHeight = 15
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.createStage()
        self.game = None

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
    def getPlayerPos(self, dimension):
        for i in range(len(self.grid)):
            if(self.grid[i] == 'p'):
                if(dimension == 2):
                    return [i % self.boardWidth, i // self.boardWidth]
                elif(dimension == 1):
                    return i

    def createStage(self):
        self.grid = [0 for x in range(self.boardWidth * self.boardHeight)]

        # 生成玩家
        start_2d = [random.randint(1, self.boardWidth - 2), random.randint(1, self.boardHeight - 2)]
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
        self.grid[x_y[0] + self.boardWidth * x_y[1]] = board_cell_data

    def drawBoard(self, painter):

        # 设置画笔颜色
        painter.setPen(QColor(0,0,0))
        # 游戏网格
        for x in range(self.boardWidth):
            for y in range(self.boardHeight):
                gridX = x * self.cellSize + 8
                gridY = y * self.cellSize + 8
                if(self[x, y] == 9):
                    painter.fillRect(gridX, gridY, self.cellSize, self.cellSize, QColor(0, 0, 0))
                elif(self[x, y] == 'p'):
                    painter.fillRect(gridX, gridY, self.cellSize, self.cellSize, QColor(0, 0, 255))
                elif(self[x, y] == 8):
                    painter.fillRect(gridX, gridY, self.cellSize, self.cellSize, QColor(255, 0, 0))
                elif(self[x, y] == 'w'):
                    painter.fillRect(gridX, gridY, self.cellSize, self.cellSize, QColor(153, 153, 153))
                elif(self[x, y] == 'e'):
                    painter.fillRect(gridX, gridY, self.cellSize, self.cellSize, QColor(100, 100, 100))
                    #painter.fillRect(gridX, gridY, self.cellSize, self.cellSize, QColor(0, 153, 0))
                        


                #画格子
                painter.drawRect(gridX, gridY, self.cellSize, self.cellSize)

        # 状态界面
        rightPanelStartX = self.boardWidth * self.cellSize + 8
        rightPanelStartY = 8

        painter.drawRect(rightPanelStartX, rightPanelStartY, 200, self.boardHeight * self.cellSize)

        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 20, Qt.AlignCenter, 40, 40, f"玩  家")
        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 60, Qt.AlignCenter, 40, 40, f"生命值：{99}")
        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 100, Qt.AlignCenter, 40, 40, f"攻击力：{99}")
        painter.drawText(rightPanelStartX + 60, rightPanelStartY + 140, Qt.AlignCenter, 40, 40, f"等  级：{99}")

        enemy_text_offset = 300
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 20, Qt.AlignCenter, 40, 40, f"敌  人")
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 60, Qt.AlignCenter, 40, 40, f"生命值：{99}")
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 100, Qt.AlignCenter, 40, 40, f"攻击力：{99}")
        painter.drawText(rightPanelStartX + 60, enemy_text_offset + rightPanelStartY + 140, Qt.AlignCenter, 40, 40, f"等  级：{99}")


    def move(self, direction:tuple):
        playerPos = self.getPlayerPos(2)
        endPos = [playerPos[0] + direction[0], playerPos[1] + direction[1]]
        if(endPos[0] < 0 or endPos[0] > 14 or endPos[1] < 0 or endPos[1] > 14):
            return
        elif(self[endPos[0], endPos[1]] == 0):
            self.grid[self.getPlayerPos(1)] = 0
            self[endPos[0], endPos[1]] = 'p'

            
        #if(posEnd > self.boardWidth or posEnd < (self.boardWidth * (self.boardHeight - 1))):

