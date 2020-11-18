import pygame
import random

from sprite import Sprite

class Ghost(Sprite):

    STEP = 0.7
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, x, y, color):
        self.color = color
        self.dimension = 20
        self.direction = random.randint(0, 3)
        super().__init__(x=x, y=y)

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    def render(self,screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.dimension)

    def isCollidedWithSprite(self, sprite):
        return self.getRect().colliderect(sprite.getRect())

    def move(self):
        if self.direction == Ghost.UP:
            self.moveUp()
        elif self.direction == Ghost.DOWN:
            self.moveDown()
        elif self.direction == Ghost.RIGHT:
            self.moveRight()
        elif self.direction == Ghost.LEFT:
            self.moveLeft()

    def changeDirection(self):
        self.direction = random.randint(0, 3)

    def checkWalls(self, walls):
        for wall in walls:
            if self.getRect().colliderect(wall):
                self.changeDirection()
                return