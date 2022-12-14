import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

	# a class to represent a single alien in the fleet

	def __init__(self,ai_settings,screen):
		# initialize the alien and set its starting position
		super(Alien,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings

		# load the alien image and set its rect attribute.
		self.image=pygame.image.load("alien.bmp")
		self.rect=self.image.get_rect()

		# start each new alien near the top of the screen
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height

		# store the alien's exact position
		self.x=float(self.rect.x)

	def blitme(self):
		# draw the alien at its current location
		self.screen.blit(self.image,self.rect)

	# checking whether an alien has hit the edge
	def check_edges(self):
		# return True if aliens is at the edge of the screen
		screen_rect=self.screen.get_rect()
		if (self.rect.right>=screen_rect.right):
			return True
		elif self.rect.left<=0:
			return True

	# for moving the aliens
	def update(self):
		# move the alien right
		self.x+=(self.ai_settings.alien_speed*self.ai_settings.fleet_direction)
		self.rect.x=self.x
