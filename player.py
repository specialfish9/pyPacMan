import pygame
from sprite import Sprite

class Player(Sprite):
    STEP = 0.5

    def __init__(self, x, y):
        self.dimension = 10
        super().__init__(x, y)

    def render(self, screen):
        pygame.draw.circle(screen, (255,255,0), (self.x, self.y), self.dimension)

    def checkWalls(self, walls):
        for wall in walls:
            if self.getRect().colliderect(wall):
                self.changeDirection()
                return

    def __isLecitMove(self, x, y, walls):
        r = pygame.Rect(self.x + x, self.y + y, 2*self.dimension,  2*self.dimension);
        for wall in walls:
            if r.colliderect(wall):
                return False
        return True

    def moveUpSafe(self, walls):
        if __isLecitMove(0, -STEP, walls):
            self.moveUp()

