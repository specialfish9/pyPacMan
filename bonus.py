import pygame
from sprite import Sprite

class Bonus(Sprite):

    def __init__(self, x, y):
        self.dimension = 5
        self.__points = 10
        super().__init__(x, y)

    def render(self, screen):
        #pygame.draw.circle(screen, (0,0,0), (self.x, self.y), 15)
        pygame.draw.circle(screen, (255,255,0), (self.x, self.y), self.dimension)

    @property
    def points(self):
        return self.__points

    def isCollidedWithSprite(self, sprite):
        return self.getRect().colliderect(sprite.getRect())
