import pygame
import random

from sprite import Sprite

class Ghost(Sprite):

    STEP = 0.5
    UP = 0
    DOWN = 2
    LEFT = 1
    RIGHT = 3

    def __init__(self, x, y, color):
        self.color = color
        self.dimension = 15
        self.direction = random.randint(0, 3)
        super().__init__(x=x, y=y)

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
        self.__direction = direction

    def render(self,screen):
        rx = self.x + self.dimension 
        ry = self.y + self.dimension
        pygame.draw.circle(screen, self.color, (rx, ry), self.dimension)

    def isCollidedWithSprite(self, sprite):
        return self.getRect().colliderect(sprite.getRect())

    def move(self, walls):
        if self.__canChangeDirection:
            # Decide wheter to change direction or not
            random.seed()
            v = random.randint(0, 500)
            if v == 1:
                self.changeDirection()
            else: 
                if self.direction == Ghost.UP:
                    if self.__isLecitMove(0, -(self.STEP), walls):
                        self.moveUp()
                    else:
                        self.changeDirection();
                elif self.direction == Ghost.DOWN:
                    if self.__isLecitMove(0, self.STEP, walls):
                        self.moveDown()
                    else:
                        self.changeDirection();
                elif self.direction == Ghost.RIGHT:
                    if self.__isLecitMove(self.STEP, 0, walls):
                        self.moveRight()
                    else:
                        self.changeDirection();
                elif self.direction == Ghost.LEFT:
                    if self.__isLecitMove(-(self.STEP), 0, walls):
                        self.moveLeft()
                    else:
                        self.changeDirection();

    def changeDirection(self):
        random.seed()
        v = self.direction
        while v % 2 == self.direction % 2:
            v = random.randint(0, 3)
        self.direction = v

    def __canChangeDirection(self, direction):
        result = True
        # Right 
        result = result and self.__isLecitMove(self.STEP,0, walls)
        # Left
        result = result and self.__isLecitMove(-(self.STEP),0, walls)
        # Down
        result = result and self.__isLecitMove(0,-(self.STEP), walls)
        # Up 
        result = result and self.__isLecitMove(0,self.STEP, walls)
        return result

    def __isLecitMove(self, x, y, walls):
        r = pygame.Rect(self.x + x, self.y + y, 2*self.dimension,  2*self.dimension);
        for wall in walls:
            if r.colliderect(wall):
                return False
        return True
