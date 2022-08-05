import sys
import pygame
from Settings import Settings
from Ship import Ship
import Game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


#create the main screen for game
def run_game():
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
    
    # make a ship
	ship=Ship(ai_settings,screen)

	# make a group to store bullets in
	bullets=Group()

	# make an alien
	aliens=Group()

	# create the fleet of aliens
	gf.create_fleet(ai_settings,screen,ship,aliens)

	# create an instance to store game statistics
	stats=GameStats(ai_settings)

	# start the main loop
    #manage the events
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		gf.update_screen(ai_settings, screen, ship, aliens,bullets)

		# drawing ship onscreen
		ship.blitme()
		
        #display the most recent screen
		pygame.display.flip()
run_game()
