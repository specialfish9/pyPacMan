import pygame
import random

import engine as engine
import ui as ui
from player import Player
from ghost import Ghost
from bonus import Bonus
from scoreboard import Scoreboard


def main():
    pygame.init()
    screen = ui.init()
    pygame.font.init()
    game_font = pygame.font.SysFont('Comic Sans MS', 30)
    running = True

    # initial player x and y
    px, py = engine.init_player();
    player = Player(px, py)

    # init scoreboard
    g_points = 0
    g_lives = engine.INITIAL_PLAYER_LIVES 
    scoreboard = Scoreboard(g_points, g_lives)

    # init ghosts and bonus
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
            g_lives -= 1
            player.jumpTo(px, py)
            scoreboard.set_lives(g_lives)
            if g_lives == 0: 
                print("MORTO")
                while(True):
                    a = 1

        if engine.should_add_ghost(g_points, len(ghosts)):
            new_ghost = engine.create_ghosts(1)
            for g in new_ghost:
                ghosts.append(g)
        # Update score
        g_points += engine.check_bonus(bonus, player)
        print("POINTS: " + str(g_points))
        scoreboard.set_points(g_points)
        scoreboard.render(screen, game_font)

        pygame.display.flip()

    pygame.quit()    

if __name__ == "__main__":
    main()
