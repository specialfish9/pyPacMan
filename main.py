import pygame
import random

import engine as engine
import ui as ui
from player import Player
from ghost import Ghost
from bonus import Bonus


def main():
    pygame.init()
    screen = ui.init()
    running = True
    
    g_points = 0

    px, py = engine.init_player();
    player = Player(px, py)

    ghosts = engine.create_ghosts(4)
    bonus = engine.init_bonus()

    while running:
        ui.draw(screen)
        walls = ui.render_grid_from_file(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.moveLeftSafe(walls)
        elif keys[pygame.K_RIGHT]:
            player.moveRightSafe(walls)
        elif keys[pygame.K_UP]:
            player.moveUpSafe(walls)
        elif keys[pygame.K_DOWN]:
            player.moveDownSafe(walls)

        engine.render_bonus(bonus, screen)
        player.render(screen)
        engine.move_ghost(ghosts, walls)
        engine.render_ghosts(ghosts, screen)
        #check_player_position(player=player, walls=walls)

        if engine.check_collision(player, ghosts):
            print("MORTO")
            while(True):
                a =1
        g_points += engine.check_bonus(bonus, player)
        print("POINTS: " + str(g_points))
        pygame.display.flip()

    pygame.quit()    

if __name__ == "__main__":
    main()
