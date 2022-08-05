import sys
import pygame
from Settings import Settings
from Ship import Ship
import Game_functions as gf

#create the main screen for game
def run_game():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
    
    # make a ship
	ship=Ship(ai_settings,screen)

    #manage the events
	while True:
		gf.check_events(ship)
		ship.update()

		gf.update_screen(ai_settings, screen, ship)

		# drawing ship onscreen
		ship.blitme()
		
        #display the most recent screen
		pygame.display.flip()
run_game()
