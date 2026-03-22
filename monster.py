import pygame
import random
import animation

class Monster(animation.AnimateSprite):

	def __init__(self, game):
		self.velocity = random.uniform(0.5, 3)
		super().__init__("mummy", self.velocity)
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 5
		self.rect = self.image.get_rect()
		self.rect.x = 1080 + random.randint(0, 300)
		self.rect.y = 540

	def damage(self, amount):
		self.health -= amount
		if self.health <= 0:
			self.rect.x = 1080 + random.randint(0, 300)
			self.velocity = random.uniform(0.2, 2)
			self.health = self.max_health
			if self.game.comet_event.is_full_loaded():
				self.game.all_monsters.remove(self)
				self.game.comet_event.attempt_fall()

	def update_health_bar(self, surface):
		bar_color = (111, 210, 46)
		back_bar_color = (60, 63, 60)
		back_bar_position = [self.rect.x + 10, self.rect.y - 10, self.max_health, 5]
		bar_position = [self.rect.x + 10, self.rect.y - 10, self.health, 5]
		pygame.draw.rect(surface, back_bar_color, back_bar_position)
		pygame.draw.rect(surface, bar_color, bar_position)

	def forward(self):
		if not self.game.check_collision(self, self.game.all_players):
			self.animate(0)
			self.rect.x -= self.velocity
		else:
			self.game.player.damage(self.attack)
			self.animate(1)
