import pygame

class AnimateSprite(pygame.sprite.Sprite):

	def __init__(self, sprite_name, speed):
		super().__init__()
		self.image = pygame.image.load(f'assets/{sprite_name}.png')
		self.current_image = 0
		self.count = 0
		self.images = self.animations.get(sprite_name)
		self.speed = speed

	def animate(self, state):
		if state == 0:
			self.count += self.speed
			if (self.count >= 1.5):
				self.count = 0
				self.current_image += 1
			if self.current_image == len(self.images):
				self.current_image = 0
			self.image = self.images[self.current_image]
		else:
			self.image = self.images[0]

	def load_animation_images(sprite_name):
		images = []
		path = f"assets/{sprite_name}/{sprite_name}"
		for num in range(1, 25):
			image_path = path + str(num) + ".png"
			images.append(pygame.image.load(image_path))

		return images
	
	animations = {
		'mummy': load_animation_images('mummy')
	}