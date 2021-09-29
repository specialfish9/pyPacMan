import pygame
import random

import ui as ui
from player import Player
from ghost import Ghost
from bonus import Bonus

INITIAL_PLAYER_LIVES = 3

def render_ghosts(ghosts, screen):
    for ghost in ghosts:
        ghost.render(screen)

def move_ghost(ghosts, walls):
    for ghost in ghosts:
        ghost.move(walls)

def check_collision(player, ghosts):
    exist = False
    for ghost in ghosts:
        exist = exist or ghost.isCollidedWithSprite(player)
    return exist

def create_ghosts(number):
    ghosts = []
    random.seed()
    for i in range(number):
        x = random.randint(0, ui.SCREEN_WIDTH)
        y = random.randint(0, ui.SCREEN_HEIGHT)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        ghosts.append(Ghost(ui.SCREEN_HEIGHT / 2, ui.SCREEN_WIDTH /2, (r, g, b)))
    return ghosts

def should_add_ghost(points, number_of_ghosts):
    return number_of_ghosts <= int(points / 200)


def check_player_position(walls, player):
        if player.x < 0:
            player.x = ui.SCREEN_WIDTH
            return
        elif player.x > ui.SCREEN_WIDTH:
            player.x = 0
            return
        elif player.y <= 0:
            player.y = 0
            return
        elif player.y >= ui.SCREEN_HEIGHT:
            player.y = ui.SCREEN_HEIGHT
            return
        collided = player.checkWalls(walls)
        if collided:
            player.set

def render_bonus(bonus, screen):
    for b in bonus:
        b.render(screen)

def check_bonus(bonus, player):
    p = 0
    for b in bonus:
        if b.isCollidedWithSprite(player):
          p += b.points  
          bonus.remove(b)
    if len(bonus) == 0:
        win()
    return p

def init_bonus():
    bonus = []
    f = open("grid.txt", "r")
    
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '-':
                x = (j * ui.WALL_DIM) + (ui.WALL_DIM / 2)
                y = (i * ui.WALL_DIM) + (ui.WALL_DIM / 2)
                bonus.append(Bonus(x, y))
    f.close()
    return bonus

def init_player():
    f = open("grid.txt", "r")
    
    for i, line in enumerate(f):
        for j, c in enumerate(line):
            if c == '@':
                x = (j * ui.WALL_DIM) 
                y = (i * ui.WALL_DIM)
                f.close()
                return (x,y)

def win():
    print("YOU WON")
    while True:
        a = 1
