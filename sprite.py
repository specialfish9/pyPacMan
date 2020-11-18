import pygame

class Sprite():
    STEP = 0.5

    def __init__(self, x, y):
        self.x = x
        self.y =y

    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, dimension):
        self.__dimension = dimension

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y

    def render(self, screen):
        pass

    def moveLeft(self):
        self.x -= self.STEP

    def moveRight(self):
        self.x += self.STEP

    def moveUp(self):
        self.y -= self.STEP

    def moveDown(self):
        self.y += self.STEP

    def setPosition(self, x, y):
        self.x = x
        self.y = y
    
    def getRect(self):
        return pygame.Rect((self.x - self.dimension), (self.y - self.dimension), 2*self.dimension, 2*self.dimension)

    def isCollidedWithSprite(self, sprite):
        pass