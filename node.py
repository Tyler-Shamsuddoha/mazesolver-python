import pygame.draw_py


class Node:
    xPos = 0
    yPos = 0
    isWall = False
    isStart = False
    isGoal = False
    isVisited = False

    def __init__(self, xPos, yPos, isWall):
        self.xPos = xPos
        self.yPos = yPos
        self.isWall = isWall

    def draw(self):
        if self.isWall:
            pygame.draw.rect(50, 50, 50, 50)

    def __str__(self):
        return f'Person({self.xPos},{self.yPos},{self.isWall})'
