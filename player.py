import pygame
from sprite import Sprite

class Player(Sprite):
    STEP = 1

    def __init__(self, x, y):
        self.dimension = 10
        super().__init__(x, y)

    def render(self, screen):
        pygame.draw.circle(screen, (255,255,0), (self.x, self.y), self.dimension)

    def checkWalls(self, walls):
        for wall in walls:
            if self.getRect().colliderect(wall):
                print("wall collided with player")
                return

    def __isLecitMove(self, x, y, walls):
        r = pygame.Rect(self.x + x, self.y + y, 2*self.dimension,  2*self.dimension);
        for wall in walls:
            if r.colliderect(wall):
                return False
        return True

    def moveUpSafe(self, walls):
        if self.__isLecitMove(0, -(self.STEP), walls):
            self.moveUp()

    def moveDownSafe(self, walls):
        if self.__isLecitMove(0, self.STEP, walls):
            self.moveDown()

    def moveLeftSafe(self, walls):
        if self.__isLecitMove(-(self.STEP), 0, walls):
            self.moveLeft()

    def moveRightSafe(self, walls):
        if self.__isLecitMove(self.STEP, 0, walls):
            self.moveRight()

