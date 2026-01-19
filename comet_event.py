import pygame

class CometFallEvent():

	def __init__(self):
		self.percent = 0
		self.percent_speed = 5

	def add_percent(self):
		self.percent += self.percent_speed / 100

	def is_full_loaded(self):
		return self.percent >= 100
	
	def reset_percent(self):
		self.percent = 0

	def attempt_fall(self):
		if self.is_full_loaded():
			print("Comet bar full")
			self.reset_percent()

	def update_bar(self, surface):
		self.add_percent()
		self.attempt_fall()
		pygame.draw.rect(
			surface, 
			(0, 0, 0), 
			[0, surface.get_height() - 10, 
			surface.get_width(), 
			10])
		pygame.draw.rect(
			surface, 
			(187, 11, 11), 
			[0, surface.get_height() - 10, 
			(surface.get_width() / 100) * self.percent,
			  10])