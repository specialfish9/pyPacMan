import pygame

class Scoreboard:

    def __init__(self, p, l):
        self.points = p
        self.lives = l

    def set_points(self, p):
        self.points = p

    def set_lives(self, l):
        self.lives = l
    
    def get_points(self):
        return self.points

    def get_lives(self):
        return self.lives

    def render(self, screen, font):
        s = font.render(str(self.points) + " " + str(self.lives), False, (255,255,255))
        screen.blit(s, (0,0))

